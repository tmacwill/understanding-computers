---
layout: default
title: "Project Interweb: Make it Network"
---

<link rel="stylesheet" type="text/css" href="css/6-internet.css" />

<div class="page-header">
    <h1>Chapter 6 <small>Project Interweb: Make it Network</small></h1>
</div>

Now that we've seen how the innards of your computer work, let's shift gears a bit and discuss everyone's favorite way to procrastinate: the Internet. So... what _is_ the Internet? It's been described as [a series of tubes](http://www.gametrailers.com/videos/8nj7ho/internet-is-a-series-of-tubes), but the Internet is really a huge network of connected computers. Using the Internet, your machine can contact another machine, like the one powering cnn.com, in order to share information. However, there's a pretty good chance that your computer doesn't have a wire running to the computer cnn.com runs on. Instead, your request to cnn.com will likely be routed through several other machines in order to reach its destination.

Let's take a look at how my request to cnn.com actually gets there. To do that, I'm going to open up a Terminal and use a program called `traceroute`, which makes a request to song destination on the Internet and displays each machine it visits on the way there. Here's what happened when I ran it from a computer living in Newark, New Jersey (where Snooki is my dedicated system administrator). Before you ask, yes, I do indeed name my computers after characters from <a href="http://en.wikipedia.org/wiki/Star_Fox_(series)">Star Fox</a>.

![Traceroute to CNN.com](img/6-trace-cnn.png)

Each one of these rows represents a machine that my request to CNN.com went through. The first of these rows is my computer, where the request originated from. Each of these devices is called a **router**, whose purpose in life is to route a request for information to the correct destination. While all of these routers may not know how to contact cnn.com, each does seem to have _some_ idea of how to get there. Each device has its own **routing table**, which maps ranges of destination addresses to other connected routers; when my request for cnn.com reaches a router, that router will use its routing table to determine where my request should be sent next so it reaches its destination as quickly as possible.

In the first column, we can see how many "hops" it took our request to reach each router. Next, we can see something that looks like an identifier for each device. From this output, it looks like our request started in Newark and then passed through Washington and Atlanta before reaching its final destination. The stars on row 14 simply indicate that that particular machine is choosing not to disclose any information about itself, for one reason or another. In the next column, we see each device's **IP address**, or a unqiue and identifying series of numbers, that can be used to contact the router. Finally, we can see how long it took from our request to get from the Jersey Shore to that machine. Based on this output, it took less than 20 milliseconds for my request to travel all the way to Atlanta, Georgia!

You may also have heard the term "router" while setting up your home Internet. In general, a router is used to create a **network**, which is simply a set of connected computers. Several computers can be physically wired to a router, and many modern routers also allow devices to connect to the network wirelessly. In your home, your router is likely attached to a DSL or cable modem, which establishes a connection via a coaxial cable and data jack. An **Internet Service Provider**, or ISP, is then responsible for connecting you to the Internet. Large ISPs in the United States include Comcast and Verizon, whose service (or the service of one of their subsidiary companies) you may use in your own home!

Let's try another one. Here's the output of `traceroute` on a different destination, reddit.com. If unfamiliar with reddit, click [here ](http://reddit.com) to waste the next ten hours of your day.

![Traceroute to reddit.com](img/6-trace-reddit.png)

This one looks a bit different. Unlike the previous output, it doesn't look like we can immediately figure out where my request went. However, let's take a closer look at that second column again. Turns out that routers' are commonly identified using nearby airport abbreviations. A quick Google shows that "mmu" is New Jersey's Morristown Municipal Airport, "ewr" is the Newark Liberty International Airport, and "nyc" is New York City. Now, take a look at the times between hops 7 and 8; looks like our time jumped from 1 millisecond to 68 milliseconds! What happened there, are all those Yankees fans slowing down the Internet in New York? While that _could_ be the case, it looks like the next router is located in the United Kingdom, the London Heathrow Airport to be precise! Unsurprisingly, it takes a while for my request to make like Columbus and traverse the Atlantic Ocean.

Let's take a closer look at that third column, the four numbers separated by dots. A device's IP address, much like your street address, describes a location to which other devices connected to the Internet can send messages. Each number in an IP address, called an **octet**, ranges from 0 to 255. So, how many bits is that? (Hint: why is it called an octet?) We know that with one bit we can represent all numbers &le; 1, with two bits numbers &le; 3, with three bits numbers &le; 7, and so on. Eventually, we'll find out that we can represent all numbers &le; 255 with exactly 8 bits. So, each octect in an IP address is 8 bits long, which means we have a total of 32 bits to work with. Hopefully that number rings a bell, as 32 bits is equal to one byte!

Because all IP addresses are simply four numbers between 0&ndash;255, that must mean that we only have a fixed number of them. To figure out how many, let's think about an IP address as a sequence of 32 bits. We know that each of those bits can be either a 0 or a 1, which gives us only two possibilities. Since there are 32 of them, that means that the total number of unique sequences of 0s and 1s is 2<sup>32</sup>, or 4,294,967,296. At first glance, four billion addresses seems like plenty. (If not, then your intuition is better than mine!) However, the current world population is currently pushing seven billion people. On top of that, I have three different Internet-connected devices into my pocket, which isn't uncommon in today's world. Finally, companies like Google have literally millions of servers, each needing some kind of IP address. Suddenly, those four billion addresses don't seem like that many.

As an aside, this isn't the first (or last) time technology has outgrown existing infrastructure. Rumor has it that in 1981 Bill Gates was quoted as saying "640K of memory ought to be enough for anybody" to address concerns with memory limitations of an IBM computer. In the Internet's earliest days, thoughts of supporting over 4 billion interconnected devices probably weren't at the front of engineers' minds!

So if we're running out of IP addresses, what can we do? After all, without an IP address, a device cannot be contacted by other devices connected to the Internet. One solution is to simply increase the size of IP addresses, which would increase the total number of available addresses. The 32-bit IP address is known as **IPv4**, which was released in the early 1980s. Now, a standard known as **IPv6** is starting to gain momentum. While an IPv4 address looks something like 60.254.153.16, an IPv6 address is instead a series of hexadecimal digits like 2001:0db8:85a3:0042:1000:8a2e:0370:7334. Hexadecimal, like binary, simply represents numbers using a different base; while binary uses base 2, hexadecimal uses base 16. Since we only have 10 different digits to work with, hexadecimal uses "a" to represent the number 11, "b" to represent 12, and so on until "f" represents 15. Each hexadecimal digit is 4 bits, so IPv6 addresses are 128 bits in length, which creates a total of 2<sup>128</sup> (or 3.4 &times; 10<sup>38</sup>) different addresses. To be precise, IPv6 allows 340,282,366,920,938,463,463,374,607,431,768,211,456 different IP addresses. Assuming the world's population is about 7 billion people, that means we can have have 4.8 &times; 10<sup>28</sup> different IPv6 addresses _per person_. That's a whole lot of iPhones! Of course, the people behind IPv4 probably said something similar 30+ years ago...

The adoption of IPv6 has been slow but steady. June 6, 2012 was dubbed World IPv6 Launch, and major Internet companies were encouraged to finally enable IPv6 support once and for all. The event was even advertised with the tagline "this time, it's for real." About a quarter of the world's top 500 sites have IPv6 enabled, and about [1% of Google users connect using IPv6](http://www.google.com/ipv6/statistics.html#tab=ipv6-adoption). However, Google does note that the number of IPv6 users has increased by a factor of 2 since last year, which is promising for IPv6 adoption.

Making addresses bigger isn't the only way we can conserve the IP address space. In fact, you probably don't need the laptop sitting on your kitchen table to be accessible by any other computer on the Internet (and or security reasons, you might not want this either, but more on that later). Because you don't need other machines on the Internet contacting your computer, there's no need to give it a unique, publically-accessible IP address. Your computer will indeed need some kind of IP address in order to connect to the Internet, but that's where a technology called **NAT**, or Network Address Translation comes in. Using NAT, the router connecting your home computer to the Internet can assign it a **private** IP address, or one that cannot be used by any ole' device on the Internet to reach your computer. Typically, private IP addresses take the form `10.x.y.z`, `172.16.y.z`, and `192.168.y.z`, which may look familiar if you've ever set up a home wireless network. Now, only your router has a single public IP address, while all of the devices on your home network have private IP addresses that don't take away from the pool of 2<sup>32</sup> IPv4 addresses!

But, this begs the question of how a computer with a private IP can interact with the Internet at all. After all, if I request information from cnn.com, then I'm probably expecting to receive some kind of response from my favorite news network, but CNN can't use my laptop's IP because it's private. Here's where the "T" in NAT kicks in. When my computer with a private IP address makes a request to a public IP address, it has to go through my router first, since that's what's connecting my computer to the Internet via my home network. Though my laptop doesn't have a public IP address, my router sure does. Once my request gets to the router, NAT will modify it so the request looks like it's coming from the router's public IP rather than my computer's private IP. After this slight modification, the router will happily forward it along to the next stop on its journey to CNN. In some cases, routers will actually have a pool of different IPs to choose from, but the same process applies to routers with just one IP address.

Eventually, Wolf Blitzer is going to receive my request and will want to send a response to my computer. Remember, my request looks like it's coming from my router's IP, which can be accessed by cnn.com because my router's IP is public. So, cnn.com will go ahead and send its response along to my router's IP. After another series of hops, my router will eventually receive today's news from CNN. Now, the router has to forward that response along to the computer that originally made the request, keeping in mind that I could have multiple devices on the same network. The router must therefore maintain an internal table of the IP addresses of all the devices that are using the router to connect to the Internet. Associated with each IP in this table is a **source port**, which is simply a unique number assigned to each device connected to the router. When the router modifies an outgoing request to change the source IP, it also tacks on that device's source port, which then gets sent to CNN. The response from cnn.com will thus also contain the source port attached by NAT, which the router can then use to figure out what device to forward the response to.

Let's make this process a bit more concrete with an example. I'm running a wireless network at home, and my router has an IP of 74.125.226.228. Currently, there are three devices connected to the network, and each has its own private IP. I'm relaxing after a long day, so I make a request from my laptop to 64.208.126.154, which will lead me to reddit.com. My network is using NAT, so here's the state of the world from my router's perspective.

<table class="table table-bordered">
    <thead>
        <tr>
            <th>Device</th>
            <th>Private IP</th>
            <th>Public IP</th>
            <th>Source Port</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Macbook Air</td>
            <td>10.0.0.1</td>
            <td>74.125.26.228</td>
            <td>1000</td>
        </tr>
        <tr>
            <td>iPhone</td>
            <td>10.0.0.2</td>
            <td>74.125.26.228</td>
            <td>1001</td>
        </tr>
        <tr>
            <td>iPad</td>
            <td>10.0.0.3</td>
            <td>74.125.26.228</td>
            <td>1002</td>
        </tr>
    </tbody>
</table>

Okay, looks like my laptop has a private IP of 10.0.0.1. Remember, anything in the form `10.x.y.z` is a private IP address that isn't world-accessible. Once my request reaches the router, its source address will change to that of the router, 74.125.26.228 in this case, and the source port, 1000, will be added to the request. Reddit will eventually receive my request and send back a picture of a cat to the IP address included in the request, which is still 74.125.26.228 with a source port of 1000. Because Reddit sent my impending feline friend to my router's IP address, it will eventually end up at my router. Then, my router can look at the source port attached to the response to look up the private IP the request originated from. Finally, the Reddit data will reach my laptop, and I can enjoy a hearty chuckle. This process certainly sounds pretty involved, but recall how few milliseconds it took to reach Reddit in the United Kingdom!

So far, we've taken it for granted that my computer connected to the Internet will have an IP address, so let's now take a look at how that number actually gets assigned. As you move among different networks and even as you connect to the same network, your computer's IP address will change. This is a bit different than the computers that power websites like cnn.com, which typically have some mechanism for maintaining the same IP address or set of IP addresses. More on that later, though!

**DHCP**, or dynamic host configuration protocol, is commonly used to obtain an IP address on a network. First, a computer that wishes to connect to the network, referred to here as the DHCP client, broadcasts a request to the network with a message that says "Here I am. I'd like to join." Then, a device called the DHCP server (which will eventually be responsible for assigning an IP address to the client) will respond to the client's request, informing the client what its IP is. Now, the client knows exactly where it should send future messages during the process of obtaining an IP address, so it won't needlessly send messages to machines that aren't involved in the process. Next, the client will send another message to the DHCP server, this time formally requesting an IP address on the network. Upon receiving this request, the DHCP server will respond and offer the client an IP address on the network. In the meantime, the server will hold that IP address inside, so no other devices can have it until the client responds. Finally, the client will send one last message to the DHCP server, acknowledging that it has received the IP address and has begun using at. At this point, the client is connected and ready to go!

This process assumes, though, that the DHCP server somehow knows which IP addresses it can assign. For example, a DHCP server in North America needs to ensure that it doesn't assign an IP address that is already in use by a device in Europe. To mitigate this issue, different ranges of IP addresses are allocated to different physical regions of the globe. Here's a map created by the author of [XKCD](http://xkcd.com/), one of my favorite webcomics.

![Map of the Internet](img/6-map.png)

Let's take a closer look. Towards the top of the map, we can see that some organizations have been allocated huge IP ranges. Apple, for example, has all IP addresses in the form `17.x.y.z`, and MIT has all IP addresses in the form `18.x.y.z`. The number of IP addresses in those ranges in comparable to the number of IP addresses allocated to entire countries, like Japan's `126.x.y.z`. From our earlier traceroute output, we can see that my trusty machine in New Jersey has an IP in one of the many ranges allocated to North America. Finally, if you take a look at the right of the map at the `192.x.y.z` range, you'll see a small dot that says "private." Sure enough, that's referring to the `192.168.y.z` range that we saw earlier was reserved for private IP addresses!

<br />
<iframe width="480" height="360" src="http://www.youtube.com/embed/Ve7_4ot-Dzs" frameborder="0"></iframe>
<br />
<br />

    HOST COMMAND

All of our discussion thus far has revolved around the idea of using IP address to contact other machines. However, cnn.com isn't exactly an IPv4 or IPv6 address, but it certainly looks like I can somehow use that sequence of characters to contact another Internet-connected device. If you know the IP address of CNN.com, you can open it up using a web browser: if you click [here](http://157.166.226.26/), you should be whisked away to CNN's homepage, despite the fact that your web browser's address bar has no references to cnn.com. Of course, remembering the words "cnn dot com" is much easier than remembering (and typing) "one five seven dot one six six dot two two six dot two six," so it'd be ideal to not have to waste brain cells on many sequences of 12 digits.

The **Domain Name System**, or DNS for short, allows us to give more convenient names to networked devices. DNS is essentially a huge phonebook distributed across many storage locations around the world. Just like the YellowPages that you wish weren't delivered to your front door, each domain _name_ in the DNS database has an associated IP _address_. Whenever you try to access a domain name that isn't just an IP address, your web browser will use DNS to look up what IP address corresponds to the domain being accessed. Once we have an IP address, our request can proceed in the manner we've already seen! So, DNS is really just another networking layer that makes life a bit easier for us. However, unlike a printed phonebook, changing entries in DNS is pretty simple and relatively fast.

In the early days of the Internet, the big phonebook of IP addresses was simply a text file called `HOSTS.TXT`. Developers would routinely copy some authoritative copy of this text file to their own machines, so they could then take advantage of all domains on the Internet. Remnants of this system still remain even on modern operating systems. On my Mac (or Linux), I can open up a file called `/etc/hosts` that lists aliases for IP addresses local to my machine. On Windows, this file is located in `C:\Windows\System32\Drivers\etc\hosts`, but it's contents are the same. On each line, we have an IP address followed by a space and then a domain name. Let's try adding a new entry. 157.166.226.25 is an IP address for cnn.com, so add the following line to the bottom of your hosts file (you may be prompted for your administrator password, since this is a system file):

    66.228.37.113 bing.com

Now, open up a web browser and head to bing.com. Toto, we're not in Redmond anymore. When we added that line to our local hosts file, we effectively created a new entry in the DNS phonebook that says "bing.com corresponds to the IP address 66.228.37.113." If you type that IP into your web browser, you'll see that it's simply one of Google's (many) IP addresses. So, when your web browser saw "bing.com," it was told that that domain resolved to one of Google's IPs, which led you to Google's homepage.

Given the massive size of the Internet, it's probably not the best idea to keep the list of all domain names in a single text file. Not only would that be impractical to keep everyone on the Internet up-to-date with the latest version, but if that file were ever compromised, someone could wreak havoc on the Internet. So, it makes more sense to distribute that information across multiple machines, called DNS servers. Rather than keep track of the entire domain name space, each DNS server typically maintains a smaller subset of all the domains that have been registered on the Internet and their corresponding IP addresses.

Let's say that I make a request to [http://cse1.net](http://cse1.net/). First, my browser will probably check its cache of recently-accessed domain names to see if it already knows the IP of cse1.net. Assuming it doesn't, it will contact a **cache DNS server** in order to ask what IP the domain "cse1.net" points to. This DNS server is could be managed by my ISP (which, remember, is responsible for connecting me to the Internet), and my computer was informed of the DNS servers on its network when it first connected (unless I manually set them myself). On a Mac, I can view the IP addresses of these DNS servers in my network settings, as shown below. If this DNS server knows where "cse1.net" is, perhaps because another computer on the network made a request to cse1.net a few minutes ago, it will respond immediately with the correct IP, and we'll be good to go. But because that makes the story boring, let's assume the first DNS server we contact doesn't know the IP of cse1.net. Now, my ISP's DNS server will go ahead and contact a **root** DNS server responsible for handling all domains ending in ".net". While the root DNS server doesn't know exactly what the address of cse1.net is, it does know the right person to ask. This server will proceed to query the **authoritative name server** for cse1.net, which is responsible for maintaining a list of IP addresses for all addresses in a DNS zone, which is simply a group of domains. Now, this server can respond with the IP address for cse1.net, which will finally make its way to my web browser. Phew! All of this before my computer even _started_ to request data from cse1.net!

![DNS Client Settings](img/6-dns-servers.png)

We can see, then, that DNS information is organized hierarchically. First, my computer checks its local cache of IP addresses, which could be maintained in a file like `/etc/hosts` or by the web browser itself. Next, we'll check a cache DNS server to see if we can immediately get an answer, but, just like your CPU cache, the data stored on cache servers could be ephemeral. Then, we have authoritative name servers that maintain IP addresses for groups of domain names, and at the top of the hierarchy are root DNS servers, which manage sets of domains.

Of course, even this distributed system can still be compromised, which would be pretty bad news for cats everywhere. So, a few years ago, ICANN, the organization responsible for assigning domain names, bestowed upon seven heroes the [keys to the Internet](http://www.popsci.com/technology/article/2010-07/order-seven-cyber-guardians-around-world-now-hold-keys-internet). When all seven individuals, scattered across the globe in the US, UK, Burkina Faso, Trinidad and Tobago, Canada, China, and the Czech Republic, come together as one superpower, the Internet can be rebooted and rid of all evil. You might think I'm joking, but this actually isn't too far from the truth. DNSSEC is an emerging standard that seeks to make DNS more secure in general by ensuring that attackers can't forge the IP addresses of websites. _Someone_ has to have the power to restart it!

While the first `HOSTS.TXT` file simply stored a series of mappings between IP addresses and domain names, modern DNS servers store a bit more information. Today, most domains have the equivalent of a spreadsheet associated with them. Here's some of the information that's currently associated with cse1.net.

![DNS Manager](img/6-dns-manager.png)

Each row in the table is called a DNS **record**. The table headings describe some of the different types of records that DNS uses. First, we have an **SOA record**, which specifies the authoritative information about the zone, including the primary name server. Next, we have **NS records** that specify additional name servers for the zone. **MX records** (Mail eXchange) specify how email sent to the domain should be handled&mdash;more on this one in particular a bit later! Next up we have **A records**, which define the IP addresses of the domain. This is essentially what we created when we edited our hosts file a little while ago. Here, we can see that both cse1.net and www.cse1.net point to the same IP address, which effectively makes typing the "www" part of the website's address optional. As an aside, the **AAAA records** referenced above are used for IPv6, while A records are used for IPv4 (remember the difference?). Finally, we have **CNAME records**, which allow us to alias domains to other domains. In this example, mail.cse1.net has been aliased to ghs.google.com. Each of these rows also has a **TTL**, or time-to-live, which defines the amount of time that should pass before the record should be refreshed by a DNS server. While my hosting service provides a nice web interface for editing DNS information, all of this information actually exists in a text file called a **zone file** located somewhere on my hosting company's infrastructure.

    NSLOOKUP COMMAND

While surfing the web, you may have noticed that most domains are in the form `domain.tld`, where "tld" is a small set of suffixes including com, net, and org. The **TLD** part of a URL is known as the top-level domain, which comes from a list of about 250 suffixes approved by the Internet Assigned Numbers Authority (IANA). Addresses like `foo.domain.tld` called **subdomains**, and allow a domain to be divided into separate components. In terms of DNS, I can assign different IP addresses to different subdomains for the same domain name by creating A records with different values. Based on the last row of our example above, I can also create a subdomain using a CNAME record. Here's a list of some common TLDs and their intended usages. However, today people often purchase TLDs based on what's available or aesthetically pleasing, as some TLDs have no restrictions on who can purchase them and how they can be used. cse1.com, for example, was already taken by someone else, so I instead purchased cse1.net and cse1.org. However, I wouldn't consider CSCI E-1 a "network," which was the intended usage of the ".net" TLD! Some TLDs, on the other hand, cannot simply be purchased by anyone on the Internet.

<table class="table table-bordered">
    <thead>
        <tr>
            <th>TLD</th>
            <th>Intended Usage</th>
            <th>Open to anyone?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>.com</td>
            <td>Companies</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>.edu</td>
            <td>Educational institutions</td>
            <td>No</td>
        </tr>
        <tr>
            <td>.gov</td>
            <td>US government entities</td>
            <td>No</td>
        </tr>
        <tr>
            <td>.info</td>
            <td>Information</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>.mil</td>
            <td>US military organizations</td>
            <td>No</td>
        </tr>
        <tr>
            <td>.net</td>
            <td>Networks</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>.org</td>
            <td>Organizations</td>
            <td>Yes</td>
        </tr>
    </tbody>
</table>

The IANA also defines a list of TLDs based on country codes, called **ccTLDs**. While this is meant to give countries their own little piece of the domain namespace, many people take advantage of country codes to create cute domain names. For example, the ccTLD for Libya is ".ly," which is used by URL-shortening services like [bit.ly](http://bit.ly) and [owl.ly](http://owl.ly). There's also ".me," the ccTLD assigned to Montenegro, which is cleverly used by sites like [about.me](http://about.me), which allows you to create your own home page. Even the United States' own ccTLD, ".us," has been put to good use by sites like [del.icio.us](http://del.icio.us). I'm also proud to say that my initials are a valid TLD, thanks to [Turkmenistan](http://en.wikipedia.org/wiki/Turkmenistan).

Purchasing a domain is actually pretty easy (and inexpensive!). To do so, all I need to do is head to a domain name **registrar** like [GoDaddy](http://www.godaddy.com/), [Namecheap](http://www.namecheap.com/), or [Network Solutions](http://www.networksolutions.com/). These companies handle interfacing with **ICANN**, the non-profit organization responsible for managing the huge number of registered domain names, among other things. Domains typically cost between $10&ndash;$15 per year to maintain, which I think is a pretty reasonable price for carving out your own little place in the Internet. While some registrars may include some number of email addresses on the domain your purchased, simply buying a domain name is separate from creating a website. After all, we now know that a domain name is simply an alias for some IP address, which by nature has to be attached to some Internet-connected and publically-accessible device! Unfortunately then, hosting a website usually occurs a monthly cost in addition to the annual fee associated with a domain name, but such is life on the Interwebs. More on hosting your own website later, though!

Often though, what we type into our web browser's address bar is much more than simply a domain name. Usually, we locate pages on the Internet using **URLs**, or uniform resource locators. In general, URLs are in the form `scheme://domain:port/path?query_string#fragment_id`, and the goal of a URL is to identify a specific resource on the Internet. cse1.net is one website, but it contains many different resources, including the problem sets page and the announcements page. As an example, a URL containing all of these pieces is `http://username:password@foo.example.com:8042/over/there/index.html?type=animal&name=narwhal#nose`. The **scheme** describes how information will be transferred between my computer and the machine responding to me, and the username and password can be used for some sites containing authentication. Next is the **host**, which is the domain we're contacting, followed by the **port** we're connecting to (much more on ports soon!). The **path**, in which hierarchical components are separated by slashes, comes next. As you can see, the path in a URL looks just like the paths to files on your located on your computer; in some cases, a URL path indeed represents at least part of the path to a file located on a remote machine. Finally, additional information can be sent along using the **query** and **fragment**. Typically, the query consists of **key/value pairs** that are passed with the request, while the fragment usually contains additional information used by the web browser.

You may also have heard the term **URI** used to describe what you type into your web browser's address bar. URIs and URLs are actually different things, though the two terms are commonly conflated. URIs, or uniform resource identifiers, are actually more general than URLs, as they serve simply to _identify_ something, not necessarily _locate_ something. The "L" in URL does indeed stand for "locator," and that's because the purpose of a URL is to describe how to find some resource on a network. In doing so, a URL serves as a URI for that resource, as we can say that a resource's location identifies it. For example, saying that my name is "Tommy MacWilliam" identifies me, but it doesn't give any information about how to locate me. On the other hand, the address "33 Oxford St., Cambridge, MA USA, Planet Earth" both describes the location of a building and identifies it. So, a URL is also a URI, but a URI isn't necessarily a URL. If you head to your local library or bookstore, you can also find an example of something that is a URI but not a URL: ISBN numbers. If unfamiliar (because who reads books anymore anyway?) an ISBN is a unique number assigned to published books; an ISBN for one of my favorite books, _Alice's Adventures in Wonderland_, is 9780811822749. Formally, this is called a **URN**, or uniform resource name, and is officially expressed as `urn:isbn:9780811822749`. Again, this ISBN number certainly identifies this great book, but it doesn't tell you where you can go buy it.

<div class="page-header page-break">
    <h1>Practice Problems</h1>
</div>

1. I'm lucky enough to say that my initials are a recognized TLD! I'll have to fly to Turkmenistan to check out the scenery someday. Can you say the same for your initials?
