---
layout: default
title: Protocol me, maybe
---

<link rel="stylesheet" type="text/css" href="css/8-protocols.css" />

<div class="page-header">
    <h1>Chapter 8 <small>Protocol me, maybe</small></h1>
</div>

The Internet is an extremely heterogenous environment. Not only do a huge variety of devices need to be able to communicate with each other over the Internet, but there's also a good chance that those devices are powered by different operating systems and software. In order for different devices to talk to each other, they need to agree upon some standardized way of communicating. That way, even if networked computers are running different hardware and software, they'll be able to communicate because they're all following a formal, established **protocol**.

We obey plenty of protocols in our everyday lives. For example, when you meet someone new, you might say hello and extend your hand. Your new friend might then then say hello back to you, grab your hand, and shake it. After a few solid shakes, both of you will release the other's hand, and perhaps you'll begin to talk about the weather. After all, Cambridge _is_ really nice this time of year. Even if you've never met this new person at all, you both obeyed the same standards of behavior. Because society has established the handshake protocol, both you and your friend knew exactly what to do without any additional instruction. This is essentially the goal for networked computers: even if two computers have never communicated before, there needs to be some way of exchanging information in a way that is agnostic to the software running on both devices.

We've actually already seen a protocol in action. Remember DHCP? Turns out the "P" in DHCP indeed stands for "protocol," which is what we'll be focusing on now. In case you forget (heck, I sure did), DHCP is the process through which your computer obtains an IP address so it can communicate on a network. Ideally, we'd like any type of computer to connect to the network, whether that computer be a Mac, a PC, or a mobile phone. However, we've seen that these devices may be running different operating systems, all of which could have their own way of doing things. So, all of these different devices need to agree on some sort of procedures that they'll follow regardless of the software they're running. DHCP is simply an agreed-upon, standardized set of steps that all devices that want to connect to a network will follow.

We've already seen how DHCP works at a high level, but let's review the protocol's steps.

1. The client wishing to connect to the network broadcasts a DHCPBROADCAST message to the network in order to locate the network's DHCP servers.

1. A DHCP server receives the broadcast and responds with a DHCPOFFER message, whose purpose is to assign the device an IP address. This message contains an IP for the device to use on the network, the amount of time that IP is valid for, and the IPs of DNS servers on the network that the device should use to resolve domain names, listed in order of preference.

1. After the client receives the DHCPOFFER, it sends the server a DHCPREQUEST message in order to request to use the IP address. This request contains the same IP that was assigned in the DHCPOFFER.

1. Finally, the server responds with a DHCPACK message, which acknowledges that it has received the request and completes the DHCP process.

As you can see, the steps of the DHCP protocol are formal and clearly defined, but they're not designed for any type of hardware or software in particular. Instead, the people writing the software for Macbooks and iPads simply have to follow the steps that DHCP sets out, and their devices will be able to connect to networks.

Alright, now that we have a handle on what protocols are, let's take a look at a protocol you probably use every day. We've talked about accessing data on CNN.com, but we haven't really said anything yet about what a request to CNN or the response from Wolf Blitzer looks like. Just as DHCP defined a set of steps for devices to follow, **HTTP**, or hypertext transfer protocol, defines lays out a process for requesting data from a web page.

Typically, HTTP communication happens between two devices. The first device, called the **client**, is the computer that's requesting information from some other computer. These requests usually come from a **web browser**, which is the program that you use to browse the web. Today, popular web browsers include Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Internet Explorer. On the other end of the request is a **server**, which is simply the name for a computer dedicated to powering a website. The server's job is to send some data back to the client based on what was requested, some of which was included in the web page's URL. For example, a URL that looks like http://www.example.com/important.doc could be pointing at a file called `important.doc` that lives on the web server behind `example.com`. If that's the case, then the server will open up that file and send its contents back to the client. Web servers run specialized software that is designed to handle web requests, and modern web servers may use programs like [Apache](http://www.apache.org/) and [nginx](http://nginx.org/).

Let's first take a look at what goes into an HTTP request created by your web browser. Based on the links you click and what you type into the address bar, the web browser will create these HTTP requests behind the scenes, so let's go ahead and take the hood off that process. HTTP requests are written in plain text, so they're easy for us as humans to read and write. Here's what an HTTP request my browser might generate when I head to my Facebook news feed:

    GET /home.php HTTP/1.1
    Host: www.facebook.com

Okay, this might look a bit cryptic at first, so let's break this down a bit. The first word, "GET" is the HTTP **method**, sometimes called the HTTP **verb**, which describes the request as an action. Here, we want to get some data from Facebook's homepage, so it makes sense that we'd want to use an HTTP GET method. HTTP specifies that these methods have to be written in ALL CAPITAL LETTERS, so don't worry, I'm not yelling at you. Next is a single space, which is specified by HTTP and not something that I just added for readability. After the space is something that looks like a URL. This isn't a complete URL, since it's missing a few necessary parts at the beginning, but it does contain the path to the resource we're requesting. Then, after another space, we have the version of HTTP that we're speaking. HTTP version 1.1 happens to be the latest accepted version of HTTP, so we'll simply use that. Now it looks like we pressed the "Enter" key, which creates a character called a carriage return, so we started up a new line. On this new line, we'll have a series of key-value pairs. Remember, key-value pairs are ways to pass along additional information using any number of parameters we want. Here, we're only passing one key-value pair, in which we tell the server that the value of "Host" is "www.facebook.com." This value is essentially the rest of the URL that we'd like to access. While the path goes in the first line of the HTTP request, the domain that the request should be sent to is passed along as a separate (non-optional) key-value pair. Why did I decide to do that? I didn't! This is something that's been specified by HTTP, so in order for my HTTP request to be valid, I have to follow HTTP's guidelines. I don't make the rules, I just enforce them.

Once the server receives this request, it has to decide how it should handle it. Based on our request, it looks like the server might have to do something with a file called `home.php`. Eventually, the server will be ready to send us some data to respond to our request. Not only does HTTP standardize how requests should be made, but it also describes what responses to requests should look like. This response will be divided into two parts: the **headers** and the **body**. First, let's look at the headers, which could look something like this:

    HTTP/1.1 200 OK
    Date: Wed, 30 Jan 2013 21:43:11 GMT
    Server: Apache/2.2.22 (Fedora)
    Content-Length: 2422
    Content-Type: text/html; charset=UTF-8
    Connection: close

This looks a bit like the request we sent to Facebook, but it isn't quite the same. On the first line, we again have the version of HTTP that we're using to communicate, which is still v1.1 (since there isn't really a reason to use anything else). On the second half of the first line is the HTTP **response code**, also called status codes. The response code tells us whether or not something went wrong with the request. In this this, it looks like everything went well, since we received the code `200` back, which corresponds to a status of `OK`. If we instead had made a request to a page that doesn't exist, like `http://www.facebook.com/asdf`, the first line in our HTTP response would look something like this:

    HTTP/1.1 404 Not Found

Here, we received a different status code: `404`. HTTP dictates that this response code should be sent when a request is made to a URL that doesn't actually point to a valid resource on the server. So, it's up to the web server to decide whether or not a request was successful and send back the appropriate status code. Here are a few other status codes that you'll commonly encounter on the web. You can also browse a more complete list [here](https://developer.mozilla.org/en-US/docs/HTTP/HTTP_response_codes).

<table class="table table-bordered">
    <thead>
        <tr>
            <th>Status Code</th>
            <th>Status Text</th>
            <th>Meaning</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>200</td>
            <td>OK</td>
            <td>The request was completed successfully.</td>
        </tr>
        <tr>
            <td>301</td>
            <td>Moved Permanently</td>
            <td>The resource at this URL has moved, so use a different URL in the future.</td>
        </tr>
        <tr>
            <td>302</td>
            <td>Found</td>
            <td>The resource at this URL has moved temporarily.</td>
        </tr>
        <tr>
            <td>400</td>
            <td>Bad Request</td>
            <td>The request didn't follow the rules of HTTP.</td>
        </tr>
        <tr>
            <td>401</td>
            <td>Unauthorized</td>
            <td>You'll need to log in to access the resource at that URL.</td>
        </tr>
        <tr>
            <td>403</td>
            <td>Forbidden</td>
            <td>You are not allowed to access the resource at that URL.</td>
        </tr>
        <tr>
            <td>404</td>
            <td>Not Found</td>
            <td>The resource pointed to by that URL doesn't exist.</td>
        </tr>
        <tr>
            <td>500</td>
            <td>Internal Server Error</td>
            <td>The server has encountered an error and cannot properly respond.</td>
        </tr>
    </tbody>
</table>

As you can see, the first digit of status codes can be used to categorize what the status code means. More broadly, status codes can be broken down into these categories:

<table class="table table-bordered">
    <thead>
        <tr>
            <th>First Digit of Status Code</th>
            <th>Category</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Informational</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Success</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Redirection</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Client Error</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Server Error</td>
        </tr>
    </tbody>
</table>

Phew, that was a lot on status codes, so let's move on and come back to them a little later. If we look back at our original HTTP response, we can see that after that first line are again a series of key-value pairs, one per line. However, while we only sent one key-value pair in our request, it looks like we got back a whole bunch of key-value pairs in the response. The first pair is pretty simple: this is simply the date and time at which the request was completed. Next, we have some information about the web server that responded to our request. In this case, it looks like the server is running software called Apache (one of the two examples of software that powers web servers that we saw earlier), whose responsibility is to handle these HTTP requests. In parenthesis, we can see that this server is running [Fedora](http://fedoraproject.org/), a form of Linux, as its operating system. As you might expect, if we instead send an HTTP request that looks something like this...

    GET / HTTP/1.1
    Host: www.microsoft.com

...included in the response is a key-value pair that instead looks like this:

    Server: Microsoft-IIS/7.5

Here, this server is running version 7.5 of Microsoft's IIS server software, which is simply an alternative to Apache. Not all servers will include the "Sever" key-value pair, since the client doesn't really care about what kind of server responded to the request. As we'll see a bit later, this can actually be a security risk, so it's probably a good idea to tell your server to never send back that key-value pair in response to any request.

Moving right along, the next two lines of the HTTP response look like they have something to do with the contents of the response. First, we have the `Content-Length`, which tells us how many bytes long the server's response will be. Here, 2422 bytes is around 2 kilobytes, which isn't a whole lot of data. Then, we have the type of content that is being sent back. Back in our discussion of character encodings and ASCII, we said that in order for computers to be able to interpret bits of data, we needed to somehow specify how they were encoded. Here, we're saying that the data that the browser is about to receive will be encoded using UTF-8, which means that our webpage can include snowmen and love hotels. Thank goodness.

The `Content-Type` also tells us that the response will be textual data that represents **HTML**, or hypertext markup language. We'll take a much deeper look at HTML once we get into web development much later, but for now, HTML is simply a language that allows us to express how a web page should be organized. For example, `<h1>Hello<h1>` is one way we could create a heading that says "Hello" using HTML. Here, `h1` is one of many HTML **tags**, which are used to describe content. We'll call `<h1>` the **start tag**, which starts up a block of content, and `</h1>` the end tag, which closes off a block of content (notice that the end tag will always begin with a `/`). The text "Hello," which lies between the start and the end tag, is what will ultimately be displayed by your web browser as a heading (since that's what the `h1` tag denotes). Similarly, if we use the `p` tag instead, we can create paragraphs of text like this: `<p>This is a paragraph</p>`. Web browsers almost always allow you to view the HTML used to create the web page you're currently looking at. On a web page, if you select "View Source" from your browser's menu, you'll be taken to a page of text containing the HTML for the website you're reading.

Alright, almost done. The last of our HTTP headers simply says that once the browser has received the entire response, it can close the connection to the web server, since there won't be any more data sent along until it makes another request. Finally, the HTTP response **body**, which comes after the response headers we just looked at, is the main contents of the response. If we visit Facebook's home page, then the response body will actually contain HTML that can be displayed by your web browser and let you catch up with your high school friends. So, you won't actually see any HTTP headers as you're surfing the web using a web browser, as they're used to provide additional information to the client. Most of the time, what we really care about is the body of the response, since that contains the contents of the web page we're visiting.

In the above example, we sent an HTTP request with the goal of getting some data from a server. Often, though, we want to send along some data to the server. For example, when we search something using Google, we need to include some type of search query, or else Google won't have any idea what we're looking for. As we saw before, one way to send data to a web server is through the URL's **query string**, which also holds key-value pairs. So, our HTTP request searching Google for cats could be:

    GET /search?q=cats HTTP/1.1
    Host: www.google.com

This looks just like the GET request we made to Facebook, except we have different values for the path and host. When performing a search query, our goal is still to _get_ data from Google's servers, which have some information about cats that we'd like to retrieve. So, as we see above, a GET request is still the right way to ask Google for data. However, sometimes we want to send some new information to a server rather than requesting some existing information. For example, when you log into Gmail, you need to send your email and password to Gmail's server, which isn't so much _getting_ information as _posting_ some new information. So, an HTTP POST request would be more appropriate, which could look something like this:

    POST /login HTTP/1.1
    Host: www.example.com
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 35

    username=tommy&password=supersecret

The first line of this request looks just like our request from before, but our HTTP method is now a POST rather than a GET. The next line, in which we specify the domain of the server we're contacting, is also the same. Now, we have two more key-value pairs that we didn't have before, but they should look familiar. Because a POST request is designed to send data, we once again have to specify what kind of and how much data we're sending. Finally, we have the request **body**, which is just like the response body we saw earlier. You'll notice though, that our request data looks just like a URL query string, even though it's not actually stored in the URL. For this to work, we also had to specify a `Content-Type` of `x-www-form-urlencoded` above. While this query string format is only one way of transferring data, it is among the most frequently-used way of including information in the body of a POST request. In fact, if you've ever filled out a form online, there's a good chance that the POST request created by your web browser used this content type to transfer data&mdash;that's where the `www-form` part comes from!

Modern web browsers usually allow you to view the HTTP requests and responses that result from loading a web page. In Google Chrome, clicking the menu at the top-right and selecting Tools > Developer Tools should bring up something like the below:

![Network Tab](img/8-network.png)

Looks like simply going to Google's home page generated a lot of network traffic! Some of this should look familiar to you, though. In the leftmost column, we have the name of the resource that was requested. Our first request downloaded the HTML for Google's homepage, which tells the browser what should be displayed. In the next column, we can see that an HTTP GET request was used to get Google's homepage, which makes sense because we're simply requesting data rather than sending any new data. Next, we can see the status code and corresponding text, and since the homepage was downloaded without any issues, we got back a 200 OK status code. The next column is the content type of the response, which we've already said is HTML. Finally, we can see how large the response was in kilobytes, as well as how long it took the browser to download the content. However, based on the above, it looks like our browser used more than just one HTTP request to load google.com. After downloading the HTML for http://www.google.com/, the web browser realized that it didn't have all of the data necessary to fully display the page. For example, it looks like the HTML the browser downloaded contains links to some images, like the Google logo we've all come to know and love. However, those images weren't transferred with the HTML that came with in the HTTP response body, since remember, the response `Content-Type` said it was only text. So, the web browser actually has to go ahead and make new HTTP requests for each image the web page is trying to display. If we look towards the bottom of the above picture, we can see that the Google logo was transferred via a separate HTTP response, this time with a content type of `image/png`, or a picture. As we'll see later, a web page's HTML can also tell the browser to download other text-based files that change a web site's appearance or functionality.

Though the process of communicating over HTTP looks like it simply involves two parties, a client and a server, large sites like CNN and Google probably have a huge number of powerful servers behind their websites in order to deal with high demand. As you've probably noticed, running a large number of programs at the same time on your home computer tends to slow it down, perhaps to the point where you'd rather watch paint dry than wait for your email to send. If thousands of people are hitting a website at the same time, then we don't want all of those requests going to the same computer, since a single machine can't handle them all. In the event a website's servers become overwhelmed with the number of requests coming in, then the loading times for people browsing the site will start to increase. Even large websites suffer from this problem! Twitter, for example, has an amazing infrastructure capable of handling millions of Bieber fans tweeting at once, but during events like the Presidential Inauguration, their servers reach their capacity due to the gigantic number of requests coming in at once. Here are a few recently-released photos from Google's data centers, showing their incredible infrastructure:

![Google 1](img/8-google1.jpg)

![Google 2](img/8-google2.jpg)

![Google 3](img/8-google3.jpg)

Each of the lit-up rows in those columns is a server powering one of Google's many websites! Crazy, right?

COMPRESSION OF PAGES
