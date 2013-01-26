---
layout: default
title: Eminent Domain Names
---

<link rel="stylesheet" type="text/css" href="css/7-domains.css" />

<div class="page-header">
    <h1>Chapter 7 <small>Eminent Domain Names</small></h1>
</div>

All of our discussion thus far has revolved around the idea of using IP address to contact other machines. However, cnn.com isn't exactly an IPv4 or IPv6 address, but it certainly looks like I can somehow use that sequence of characters to contact another Internet-connected device. If you know the IP address of CNN.com, you can open it up using a web browser: if you click [here](http://157.166.226.26/), you should be whisked away to CNN's homepage, despite the fact that your web browser's address bar has no references to cnn.com. Of course, remembering the words "cnn dot com" is much easier than remembering (and typing) "one five seven dot one six six dot two two six dot two six," so it'd be ideal to not have to waste brain cells on many sequences of 12 digits.

The **Domain Name System**, or DNS for short, allows us to give more convenient names to networked devices. DNS is essentially a huge phonebook distributed across many storage locations around the world. Just like the YellowPages that you wish weren't delivered to your front door, each domain _name_ in the DNS database has an associated IP _address_. Whenever you try to access a domain name that isn't just an IP address, your web browser will use DNS to look up what IP address corresponds to the domain being accessed. Once we have an IP address, our request can proceed in the manner we've already seen! So, DNS is really just another networking layer that makes life a bit easier for us. However, unlike a printed phonebook, changing entries in DNS is pretty simple and relatively fast.

In the early days of the Internet, the big phonebook of IP addresses was simply a text file called `HOSTS.TXT`. Developers would routinely copy some authoritative copy of this text file to their own machines, so they could then take advantage of all domains on the Internet. Remnants of this system still remain even on modern operating systems. On my Mac (or Linux), I can open up a file called `/etc/hosts` that lists aliases for IP addresses local to my machine. On Windows, this file is located in `C:\Windows\System32\Drivers\etc\hosts`, but it's contents are the same. On each line, we have an IP address followed by a space and then a domain name. Let's try adding a new entry. 157.166.226.25 is an IP address for cnn.com, so add the following line to the bottom of your hosts file (you may be prompted for your administrator password, since this is a system file):

    66.228.37.113 bing.com

Now, open up a web browser and head to bing.com. Toto, we're not in Redmond anymore. When we added that line to our local hosts file, we effectively created a new entry in the DNS phonebook that says "bing.com corresponds to the IP address 66.228.37.113." If you type that IP into your web browser, you'll see that it's simply one of Google's (many) IP addresses. So, when your web browser saw "bing.com," it was told that that domain resolved to one of Google's IPs, which led you to Google's homepage.

Given the massive size of the Internet, it's probably not the best idea to keep the list of all domain names in a single text file. Not only would that be impractical to keep everyone on the Internet up-to-date with the latest version, but if that file were ever compromised, someone could wreak havoc on the Internet. So, it makes more sense to distribute that information across multiple machines, called DNS servers. Rather than keep track of the entire domain name space, each DNS server typically maintains a smaller subset of all the domains that have been registered on the Internet and their corresponding IP addresses.

Let's say that I make a request to [http://cse1.net](http://cse1.net/). First, my browser will probably check its cache of recently-accessed domain names to see if it already knows the IP of cse1.net. Assuming it doesn't, it will contact a **cache DNS server** in order to ask what IP the domain "cse1.net" points to. This DNS server is could be managed by my ISP, which is a company responsible for connecting me to the Internet. My computer was informed of the DNS servers on its network when it first connected (unless I manually set them myself), and on a Mac, I can view the IP addresses of these DNS servers in my network settings, as shown below. Because various computers on the network are making requests to the same DNS servers, there's a good chance that a given DNS server is going to be asked for the IP address of a popular site like "google.com" pretty frequently. So, cache DNS servers will remember the IP addresses they've been asked for in order to give other computers making a request to the same place an immediate answer. If a given cache DNS server doesn't already know the IP for a domain, then it's going to have to keep looking by asking other DNS servers if they know the answer.

![DNS Client Settings](img/7-dns-servers.png)

If this DNS server knows where "cse1.net" is, perhaps because another computer on the network made a request to cse1.net a few minutes ago, it will respond immediately with the correct IP, and we'll be good to go. But because that makes the story boring, let's assume the first DNS server we contact doesn't know the IP of cse1.net. Now, perhaps after asking a few nearby DNS servers and getting no result, this DNS server will go ahead and contact a **root** DNS server responsible for handling all domains ending in ".net". While the root DNS server doesn't know exactly what the address of cse1.net is, it does know the right person to ask. This server will proceed to query the **authoritative name server** for cse1.net, which is responsible for maintaining a list of IP addresses for all addresses in a DNS zone, which is simply a group of domains. Now, this server can respond with the IP address for cse1.net, which will finally make its way to my web browser. Phew! All of this before my computer even _started_ to request data from cse1.net!

We can see, then, that DNS information is organized hierarchically. First, my computer checks its local cache of IP addresses, which could be maintained in a file like `/etc/hosts` or by the web browser itself. Next, we'll check a cache DNS server to see if we can immediately get an answer, but, just like your CPU cache, the data stored on cache servers could be ephemeral. Then, we have authoritative name servers that maintain IP addresses for groups of domain names, and at the top of the hierarchy are root DNS servers, which manage sets of domains.

    SETTING YOUR OWN DNS SERVERS, GOOGLE EXAMPLE

    NET NEUTRALITY, WHY THAT'S A BIG DEAL

Of course, even this distributed system can still be compromised, which would be pretty bad news for cats everywhere. So, a few years ago, ICANN, the organization responsible for assigning domain names, bestowed upon seven heroes the [keys to the Internet](http://www.popsci.com/technology/article/2010-07/order-seven-cyber-guardians-around-world-now-hold-keys-internet). When all seven individuals, scattered across the globe in the US, UK, Burkina Faso, Trinidad and Tobago, Canada, China, and the Czech Republic, come together as one superpower, the Internet can be rebooted and rid of all evil. You might think I'm joking, but this actually isn't too far from the truth. DNSSEC is an emerging standard that seeks to make DNS more secure in general by ensuring that attackers can't forge the IP addresses of websites. _Someone_ has to have the power to restart it!

While the first `HOSTS.TXT` file simply stored a series of mappings between IP addresses and domain names, modern DNS servers store a bit more information. Today, most domains have the equivalent of a spreadsheet associated with them. Here's some of the information that's currently associated with cse1.net.

![DNS Manager](img/7-dns-manager.png)

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
