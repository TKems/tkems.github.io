---
layout: post
title:  DLink Movienite Part 2 and Hardware Hacking
categories: [Projects,Hardware Hacking,Personal Project]
excerpt: The DLink Movienite streaming device has a serious hardware flaw that is exploited easily for root level access.
---

In my previous post about the DLink Movienite [Part 1 Here!](https://www.trevorkems.com/dlink-movienite), I went over how I found a serial port enabled with root shell access. In this post, I will go over some basics of finding a open serial ports and how to use a serial device to gain network access using that port.


Once you have access to a serial port on a device, sometimes there can be programs that allow for network access even when there wasn't any services at first.

On the Movienite, in the /etc/ directory we find the inetd.conf file that configures the inetd service. However it seems like inetd isn't started on boot. To start it, just run the inetd command without any arguments. In the case of the Movienite, since the inetd config file starts the telnetd service, we can then connect over telnet to the device.

![](/images/telnet-command.png)

After telnet is established, we can use it to poke around the file system a bit more without debug message interrupting our commands.

![](/images/dlink-movienite-2.jpg)


Overall, this allows an attacker with physical access to the device to compromise user information. My next step is to find if this device has any remote vulnerabilities that an attacker could take advantage of.

In progress...
