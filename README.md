# Trevor Kems — professional portfolio

Jekyll portfolio and technical blog for [trevorkems.com](https://www.trevorkems.com), hosted on GitHub Pages. The original Reverie/Jekyll Now structure and MIT license are retained; the site uses local CSS, system fonts, and the existing search script.

## Local development

Use Ruby 3.3.4 (see `.ruby-version`) and Bundler. The Gemfile selects the GitHub Pages dependency set, including Jekyll 3.10 and the supported feed, sitemap, SEO, and pagination plugins.

The Gemfile requires Ruby 3.3.x: the Pages dependency set used here does not support Ruby 4.0. The Windows build was verified with portable Ruby 3.3.4, without changing the installed Ruby 4.0.6. That local runtime and its build helper are in ignored `tmp/`; dependencies are in ignored `vendor/bundle/`.

```sh
bundle install
bundle exec jekyll serve
```

For production validation:

```sh
JEKYLL_ENV=production bundle exec jekyll build --trace
python3 scripts/verify_site.py
```

In PowerShell, set `$env:JEKYLL_ENV = 'production'`, then run the build and `python scripts/verify_site.py`.

The validation script requires only Python's standard library and checks the **actual Jekyll output**. It protects the original post URLs, internal links and anchors, canonical tags, basic HTML accessibility, feed, sitemap, search index, and CNAME. The GitHub Actions workflow in `.github/workflows/validate.yml` runs these checks on pushes and pull requests. It does not deploy or change the existing GitHub Pages publishing configuration.

## Content maintenance

- `index.html`: portfolio homepage.
- `_data/research.yml`: selected research and source links, shared by the homepage and Research page.
- `_data/projects.yml`: tools and labs; earlier student work is linked separately on Projects.
- `_data/talks.yml`: presentations, event dates, recordings, and slides.
- `_data/experience.yml`: employment history used by the Experience page.
- `_data/navigation.yml`: primary navigation.
- `_data/focus.yml`: homepage focus areas.
- `_pages/`: portfolio pages and compatibility redirects.
- `_posts/`: original long-form articles.
- `_includes/` and `_layouts/`: reusable markup and SEO integration.
- `assets/style.scss`: responsive design; `_sass/_darcula.scss` supplies the existing syntax colors.

Research summaries are grounded in the original articles and these public repositories:

- [Victure camera research and decoder](https://github.com/TKems/Victure-Camera-Vulnerabilities)
- [Damn-Vulnerable-ADCS](https://github.com/TKems/Damn-Vulnerable-ADCS)
- [LockBit decryptor breakdown](https://github.com/TKems/LockBit-Decryptor-Breakdown)
- [Garage-door RF research](https://github.com/TKems/Garage-Door-Hacking)
- [ViewState Decoder](https://github.com/TKems/Viewstate-Decoder-Extension)
- [Competition tooling](https://github.com/TKems/campfire)

The ADCS lab is described as supporting NTLM relay testing; the README does not claim template-vulnerability coverage. The LockBit analysis concerns the recovery tool's decryption-ID checker. No malware-decryption breakthrough or recovered victim data is claimed.

Trevor confirmed the current Waterleaf title as **Senior Penetration Tester** during this update. April 2023 remains the company start date; no promotion date was supplied.

## Privacy and contact

No resume or resume PDF is published. The former `/resume/` URL redirects to the privacy-safe Experience page and is excluded from the sitemap. Public contact email is `contact@tkems.io`, routed separately from Trevor's personal email.

## URLs and deployment

Do not change `permalink: /:title/`, post filenames, or post slugs without explicit redirects. The seven original post URLs remain the reference set in `scripts/verify_site.py`.

The chronological archive now lives at `/blog/`, with six posts per page and `/blog/page:num/` pagination. Keep `blog/index.html` as HTML **without a permalink in front matter**, as required by jekyll-paginate.

The original site had seven posts and therefore only one additional archive page: `/page2/`. Its static redirect points to `/blog/page2/`, is excluded from the sitemap, and canonicalizes to the destination. `/employment/` and `/resume/` similarly redirect to `/experience/`. These are HTML redirects suitable for branch-based GitHub Pages, not HTTP 301 responses.

`CNAME` remains `www.trevorkems.com` and is now included in the generated site. HTTPS is set in `_config.yml`. Feed and sitemap remain at `/feed.xml` and `/sitemap.xml`. SEO tags come from jekyll-seo-tag; avoid adding duplicate titles, canonicals, or OpenGraph tags. The existing portrait supplies the default social image, with a research image override for Operation Big Brother.

## Remaining assets and verification

- Add a verified Splunk .conf recording/slides link when available.
- The old DLink follow-up referenced `/images/telnet-command.png`, which was already absent. Its reference is retained in an HTML comment for restoration, removing the broken image request. The first DLink article also already had a commented-out missing `dlink-movienite-3.jpg` reference.
- A dedicated social card and optimized portrait variants can be added later.

**Production Jekyll build passed on Windows**, using Ruby 3.3.4, Jekyll 3.10.0, and github-pages 232. The Windows compiler needed C17 mode for several native gem extensions; no dependency source patches were required. The build emits a non-fatal Faraday retry-middleware advisory from the dependency stack.

The actual generated output passes `scripts/verify_site.py`, covering all seven original post URLs, internal links and anchors, six-plus-one post pagination, redirects, privacy checks, headings, image alt text, canonicals, metadata, feed, sitemap, search, and CNAME.

Edge checks against the actual Jekyll output covered desktop and mobile layouts, with no horizontal overflow or broken images. Search, keyboard skip navigation, redirects, and reduced-motion media were also checked.
