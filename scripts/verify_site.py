"""Check the actual Jekyll output: python scripts/verify_site.py [_site]."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
ORIGIN = 'https://www.trevorkems.com'
POSTS = [
    '/dlink-movienite/', '/new-site/', '/IASG-presentation/',
    '/dlink-movienite-part-2/', '/coms-309/', '/cpre-186/',
    '/operation-big-brother-iot-camera/',
]
PAGES = ['/', '/research/', '/projects/', '/talks/', '/experience/',
         '/blog/', '/blog/page2/', '/about/', '/categories/',
         '/search/', '/seniordesign/']
REDIRECTS = {'/employment/': '/experience/', '/resume/': '/experience/',
             '/page2/': '/blog/page2/', '/404/': '/404.html'}
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def target(path):
    candidate = ROOT / unquote(path).lstrip('/')
    if candidate.is_dir():
        candidate /= 'index.html'
    if not candidate.exists() and not candidate.suffix:
        candidate = candidate.with_suffix('.html')
    return candidate


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = []
        self.links = []
        self.canonicals = []
        self.h1s = 0
        self.main = 0
        self.lang = None
        self.descriptions = 0
        self.og_titles = 0
        self.refresh = None
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'html':
            self.lang = a.get('lang')
        self.h1s += tag == 'h1'
        self.main += tag == 'main'
        if tag == 'img':
            check(bool(a.get('alt')), f'{self.path}: image needs descriptive alt text')
        if tag == 'meta':
            self.descriptions += a.get('name') == 'description'
            self.og_titles += a.get('property') == 'og:title'
            if a.get('http-equiv', '').lower() == 'refresh':
                self.refresh = a.get('content')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a.get('href'))
        for attr in ('href', 'src'):
            if a.get(attr):
                self.links.append(a[attr])


if not ROOT.is_dir():
    sys.exit(f'Missing Jekyll output: {ROOT}. Run bundle exec jekyll build first.')
documents = {p.resolve(): Document(p) for p in ROOT.rglob('*.html')}

for path in POSTS + PAGES + list(REDIRECTS) + ['/404.html']:
    check(target(path).is_file(), f'Missing preserved or required URL: {path}')

for file, doc in documents.items():
    relative = '/' + file.relative_to(ROOT).as_posix()
    page_url = relative[:-10] if relative.endswith('index.html') else relative
    check(doc.lang == 'en', f'{relative}: missing English language declaration')
    check(doc.h1s == 1, f'{relative}: expected one h1, found {doc.h1s}')
    check(doc.main == 1, f'{relative}: expected one main landmark')
    check(len(doc.canonicals) == 1, f'{relative}: expected one canonical')
    check(not [i for i, n in Counter(doc.ids).items() if n > 1], f'{relative}: duplicate IDs')
    if not doc.refresh:
        check(doc.descriptions == 1, f'{relative}: expected one meta description')
        check(doc.og_titles == 1, f'{relative}: expected one OpenGraph title')
        check(doc.canonicals == [ORIGIN + page_url], f'{relative}: incorrect canonical {doc.canonicals}')
    for link in doc.links:
        parsed = urlsplit(urljoin(ORIGIN + page_url, link))
        if parsed.scheme not in ('http', 'https') or parsed.netloc != 'www.trevorkems.com':
            continue
        dest = target(parsed.path)
        check(dest.is_file(), f'{relative}: broken local link {link}')
        if parsed.fragment and dest.resolve() in documents:
            check(unquote(parsed.fragment) in documents[dest.resolve()].ids,
                  f'{relative}: missing anchor {link}')

for old, new in REDIRECTS.items():
    doc = documents.get(target(old).resolve())
    check(doc is not None and doc.canonicals == [ORIGIN + new], f'{old}: wrong redirect canonical')
    check(doc is not None and doc.refresh and new in doc.refresh, f'{old}: missing redirect')

blog = documents.get(target('/blog/').resolve())
archive = documents.get(target('/blog/page2/').resolve())
if blog and archive:
    first_posts = set(blog.links) & set(POSTS)
    older_posts = set(archive.links) & set(POSTS)
    check(len(first_posts) == 6 and len(older_posts) == 1 and not first_posts & older_posts,
          'Blog pagination must list six posts, then the remaining post without overlap')
    check(first_posts | older_posts == set(POSTS), 'Posts missing from blog pagination')
    check('/blog/page2/' in blog.links and '/blog/' in archive.links, 'Broken pagination navigation')

check(not (ROOT / 'docs' / 'Trevor-Kems-Resume.pdf').exists(),
      'Resume PDF should not be published')
private_email = 'trevorkems' + '@' + 'gmail.com'
public_text = [*ROOT.rglob('*.html'), *ROOT.rglob('*.xml'), *ROOT.rglob('*.json'),
               *ROOT.rglob('*.txt'), *ROOT.rglob('*.css')]
check(not any(private_email in path.read_text(encoding='utf-8', errors='ignore')
              for path in public_text),
      'Personal email address is present in generated output')
check(any('contact@tkems.io' in path.read_text(encoding='utf-8', errors='ignore')
          for path in ROOT.rglob('*.html')), 'Public contact email missing')

for xml_file in ('sitemap.xml', 'feed.xml'):
    try:
        ET.parse(ROOT / xml_file)
    except (OSError, ET.ParseError) as exc:
        errors.append(f'{xml_file}: {exc}')
sitemap_path = ROOT / 'sitemap.xml'
if sitemap_path.exists():
    sitemap = sitemap_path.read_text(encoding='utf-8')
    for post in POSTS:
        check(ORIGIN + post in sitemap, f'Post missing from sitemap: {post}')
    for old in REDIRECTS:
        check(f'<loc>{ORIGIN}{old}</loc>' not in sitemap, f'Redirect indexed in sitemap: {old}')
    check('http://www.trevorkems.com' not in sitemap, 'HTTP URLs in sitemap')
try:
    entries = json.loads((ROOT / 'search.json').read_text(encoding='utf-8'))
    check(set(POSTS).issubset({entry['url'] for entry in entries}), 'Posts missing from search index')
except (OSError, ValueError, KeyError) as exc:
    errors.append(f'search.json: {exc}')
check((ROOT / 'CNAME').is_file() and (ROOT / 'CNAME').read_text().strip() == 'www.trevorkems.com',
      'Custom domain missing or changed')

if errors:
    print('\n'.join(f'FAIL: {error}' for error in errors))
    sys.exit(1)
print(f'PASS: {len(documents)} HTML documents; all seven original post URLs; internal links and anchors; '
      'pagination; privacy checks; headings, alt text, canonicals, metadata, feed, sitemap, search, and CNAME.')
