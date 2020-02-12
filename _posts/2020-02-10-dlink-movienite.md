---
layout: post
title:  DLink Movienite
categories: [Projects,Hardware Hacking]
excerpt: The DLink Movienite streaming device has a serious hardware flaw that is exploited easily for root level access.
---

The DLink Movienite streaming device is a small, black device that was released in 2012. It supports Netflix, Vudu, Pandora, and YouTube out of the box and is very easy to setup. It has Wi-fi, Ethernet, and HDMI on the rear of the unit. This may seem like a disappointment, however there is more available inside the device.  

![](/images/dlink-movienite.jpg)

As you can see, there is a lot inside this small box! At first I noticed the Wi-fi card in the mini PCI Express slot. However, after further examination, I noticed a 4 pin header on the left of the board. This proved to be a very interesting discovery. In order to get access I soldered on some jumper wires. At first I did some digging and found that this port most likely was a serial debugging port. However, I had no idea if this would be the case. Since I didn't have a nice USB to serial adapter, I found an [article](https://oscarliang.com/use-arduino-as-usb-serial-adapter-converter/) describing how to use an Arduino's built in serial programmer as a serial adapter. I choose to just tie the Arduino's RESET pin to GND and then connect the RX and TX to the pins on the board.


![](/images/dlink-movienite-2.jpg)

After I connected it to my PC, I opened up PuTTY and choose the serial option. I played around for a while with baud rate for a while, however, I only got a garbled text output. I decided to flip the TX and RX wires and see if that would change anything.

<!-- Missing Image
![](/images/dlink-movienite-3.jpg)
-->

Success! And a surprise! uBoot output and a root shell!

After some more digging around in the file system, I found a vulnerability that would allow a remote attacker control of the box remotely could be started on the device using a single, simple command. I am not listing it here as it may have security implications.

I am still working on this project and still trying to find some possible software based vulnerabilities within the firmware of the device.

Stay tuned...
