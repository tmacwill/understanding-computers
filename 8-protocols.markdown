---
layout: default
title: Protocol me, maybe
---

<link rel="stylesheet" type="text/css" href="css/8-protocols.css" />

<div class="page-header">
    <h1>Chapter 8 <small>Protocol me, maybe</small></h1>
</div>

The Internet is an extremely heterogenous environment. Not only do a huge variety of devices need to be able to communicate with each other over the Internet, but there's also a good chance that those devices are powered by different operating systems and software. In order to do so, devices need to agree upon some standardized way of communicating. That way, even if networked computers are running different hardware and software, they'll be able to communicate because they're all following a formal, established **protocol**.

We obey plenty of protocols in our everyday lives. For example, when you meet someone new, you might say hello and extend your hand. Your new friend might then then say hello back to you, grab your hand, and shake it. After a few solid shakes, both of you will release the other's hand, and perhaps you'll begin to talk about the weather. After all, Cambridge _is_ really nice this time of year. Even if you've never met this new person at all, you both obeyed the same standards of behavior. Because society has established the handshake protocol, both you and your friend knew exactly what to do without any additional instruction. This is essentially the goal for networked computers: even if two computers have never communicated before, there needs to be some way of exchanging information in a way that is agnostic to the software running on both devices.

We've actually already seen a protocol in action. Remember DHCP? Turns out the "P" in DHCP indeed stands for "protocol," which is what we'll be focusing on now. In case you forget (heck, I sure did), DHCP is the process through which your computer obtains an IP address so it can communicate 
