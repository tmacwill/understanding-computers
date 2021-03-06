## Introduction

We're probably all familiar with email. Whether we're logged into Gmail.com or Verizon.net in a web browser or using Microsoft Outlook or Apple Mail on the desktop, the cat videos we send to our friends and co-workers are all delivered using the same email **protocols**. We're still using the same basic idea behind protocols like DHCP and HTTP: even if we have different devices on our network running different software, they call all communicate if everyone follows the same set or rules. While making a request to a web page used only one protocol, since HTTP defines rules for both requests and responses, we'll look at three different protocols that may or may not be used in the process of sending an email. First, we'll take a look at how your email containing a link to a cat video is sent to your co-worker, and then we'll see what happens when you log into your inbox and read email messages.

## Sending Emails with SMTP

Just as a web server was responsible for responding to clients' HTTP requests, a server will also be responsible for sending and receiving emails. **SMTP**, or Simple Mail Transfer Protocol, will be our weapon of choice for email delivery. When Alice sends an email to her good friend Bob, two SMTP servers will be involved: Alice will need an SMTP server to send an email, and Bob will need an SMTP server so the mail can be delivered.

As the "simple" in SMTP suggests, sending and receiving emails actually isn't too complicated a process! First, you'll sit down at an email client (also called a mail user agent, or MUA), whether that be an app on your phone or an interface on the web. On your client of choice, you can compose a message, as well as choose a subject, recipients, CC'd (or carbon copied) recipients, and BCC'd (or blind carbon copied) recipients. For the sake of this example, let's say you're using Gmail, though this same process will apply if you're on another client like Mailbox on your iPhone or Outlook on your desktop. Once you hit send, your message will be sent to an SMTP server (also called an MDA, or mail delivery agent) owned and managed by Gmail. Since services like Gmail are pretty popular, there's a good chance that you're not the only one trying to send an email at any given point in time. So, your message will probably join a queue of other email messages on an SMTP server; to be fair to its customers, Gmail will handle the messages in the order they come in.

Once your message reaches the front of the queue, the sending SMTP server needs to figure out where to send the email. As you've probably noticed, email addresses are always in the form `name@domain.tld`, where the @ character separates a unique username and the domain (which could have a subdomain as well) of a server. Using the email address's domain, the sending SMTP server can figure out which SMTP server will be receiving the message. We know that we'll need an IP address in order to send any kind of message across the Internet, but all we have is a human-readable domain name... Hmm... What can we possibly do? If only we had a process for translating domain names into IP addresses!

DNS to the rescue! Remember, DNS is just a process for translating a human-readable name into some kind of IP address. Back when we looked at DNS records, we saw a type of record called an MX, or mail exchange, record. Here's where those are going to come into play. The MX record tells the sending SMTP server the IP address of the server that will receive mail for the domain. So, Gmail's SMTP server can use DNS to determine the IP address of the recipient's SMTP server, and then send along a request containing the email. Finally, this request will travel through the Internet just like the traceroute and HTTP requests we've already seen! After passing through routers are the Internet's core, the email will eventually reach the receipient SMTP server.

To recap, the process of sending an email involves one SMTP server communicating with another SMTP server, which looks something like this:

![SMTP Diagram](/static/img/content/chapters/email/smtp.png)

## Data Structures: Queues and Stacks

Let's take a quick detour and talk about that email queue for a moment. The concept of a **queue** is actually a pretty common one in computer science. A queue is any collection of items where things will be processed in the order they came in. For example, the line for the [Rock 'n' Roller Coaster](http://en.wikipedia.org/wiki/Rock_'n'_Roller_Coaster_Starring_Aerosmith) at Walt Disney World is a queue (and based on my experience, a pretty long one at that). The people who got in line at 10am will get to rock and roll before the people who got in line at 11am, so we have a queue of people. (I know what you're thinking, experienced Disney World travelers who use the [FastPass](https://disneyworld.disney.go.com/guest-services/fast-pass/) system to jump ahead of the line, but wait your turn this time.) If you're big into acronymns like me, you can use "FIFO," or "first in, first out," to remember how items are processed in a queue.

On the other hand, consider a **stack** of plates. Unless you want the stack to fall over, you'll want to take a plate from the top of the pile rather than the bottom of the pile when it's time for dinner. That means that the first plate you added to the stack will always be at the bottom of the pile, while the last plate you added to the stack will be at the top of the pile. So, you'll end up taking plates off in the reverse of the order you added them to the stack, which is essentially the opposite of a queue! If a queue is FIFO, then a stack is LIFO, or "last in, last out."

## Email Headers

Let's now take a look at exactly what the contents of one of these requests looks like. Just like HTTP requests, emails also have headers that we typically don't see when we open up a message. In the Gmail UI, you can click "Show original" to show the full contents of the email messsage that was sent. Here's a sample of what an email actually looks like:

    Delivered-To: unicodelovehotel@gmail.com
    Received: by 10.223.64.143 with SMTP id e15csp17700fai;
            Sat, 2 Mar 2013 09:46:00 -0800 (PST)
    X-Received: by 10.49.12.143 with SMTP id y15mr25034564qeb.27.1362246358685;
            Sat, 02 Mar 2013 09:45:58 -0800 (PST)
    Return-Path: <unicodelovehotel@live.com>
    Received: from col0-omc1-s9.col0.hotmail.com (col0-omc1-s9.col0.hotmail.com. [65.55.34.19])
            by mx.google.com with ESMTP id hc10si11831922qab.44.2013.03.02.09.45.57;
            Sat, 02 Mar 2013 09:45:58 -0800 (PST)
    Received-SPF: pass (google.com: domain of unicodelovehotel@live.com designates 65.55.34.19 as permitted sender) client-ip=65.55.34.19;
    Authentication-Results: mx.google.com;
           spf=pass (google.com: domain of unicodelovehotel@live.com designates 65.55.34.19 as permitted sender) smtp.mail=unicodelovehotel@live.com
    Received: from COL002-W67 ([65.55.34.7]) by col0-omc1-s9.col0.hotmail.com with Microsoft SMTPSVC(6.0.3790.4675);
         Sat, 2 Mar 2013 09:45:41 -0800
    X-EIP: [P1MGsuJd3RDrA2h/Chca1T2JhXgCEJS1]
    X-Originating-Email: [unicodelovehotel@live.com]
    Message-ID: <COL002-W672344BAD5002880FBD489C3F80@phx.gbl>
    Return-Path: unicodelovehotel@live.com
    Content-Type: multipart/alternative;
        boundary="_a3224380-c68b-4f38-84d4-fd4a8233b8b2_"
    From: Unicode Love Hotel <unicodelovehotel@live.com>
    To: "unicodelovehotel@gmail.com" <unicodelovehotel@gmail.com>
    Subject: I love cats
    Date: Sat, 2 Mar 2013 12:45:41 -0500
    Importance: Normal
    MIME-Version: 1.0
    X-OriginalArrivalTime: 02 Mar 2013 17:45:41.0855 (UTC) FILETIME=[C245C6F0:01CE176D]

    --_a3224380-c68b-4f38-84d4-fd4a8233b8b2_
    Content-Type: text/plain; charset="iso-8859-1"
    Content-Transfer-Encoding: quoted-printable

    I just wanted to let you know how much I love cats! They're the best.            =
              =

    --_a3224380-c68b-4f38-84d4-fd4a8233b8b2_
    Content-Type: text/html; charset="iso-8859-1"
    Content-Transfer-Encoding: quoted-printable

    <html>
    <head>
    <style><!--
    .hmmessage P
    {
    margin:0px=3B
    padding:0px
    }
    body.hmmessage
    {
    font-size: 12pt=3B
    font-family:Calibri
    }
    --></style></head>
    <body class=3D'hmmessage'><div dir=3D'ltr'>I just wanted to let you know ho=
    w much I love cats! They're the best.</div></body></html>=

    --_a3224380-c68b-4f38-84d4-fd4a8233b8b2_--

Yikes! Let's break this down a bit. Our email, like an HTTP request, is divided into two parts, headers on the top and body on the bottom, and just like last time, our headers consist of key-value pairs. We're actually going to read these from bottom to top (since we have newer timestamps on the top and older timestamps on the bottom). Looks like the headers tell us the date the message was sent, the subject of the email, the recipient of the email, and the sender of the email. Then, we have a `Content-Type` header, which should look familiar! We'll come back to that one in a bit. Next, we have some keys that start with `Received`. The first `Received` header says that an SMTP server owned by Microsoft (and once Hotmail, it looks like) received the message from some other IP address. Because I sent the message using Outlook.com's web UI, that's probably the IP address of the web server I was on at the time. The next `Received` header says that an SMTP server owned by Google received the message sent by Microsoft's SMTP server, which represents the delivery of the email from one server to the other.

After the headers, we have the body of the email, where our message can be found. Looking closely, it looks like the text of our email has actually been sent twice? What gives? If we look back at that `Content-Type` header at the top of the email, it looks like we have a value of "multipart," which seems to suggest our content will consist of multiple parts. From the same header value, we can see that we have a boundary of "\_a3224380-c68b-4f38-84d4-fd4a8233b8b2\_" that separates the two parts of the email message. The first part of the email is our message using only plain text (e.g., ASCII), while the second part of our message is using HTML to create some formatting (like fonts and colors). Modern web apps like Gmail.com and Outlook.com will use the HTML version of a message (so you can send emails with some additional formatting), while other email clients may prefer only the text-only version.

## Interacting with SMTP

In order to send an email, an email client will issue a series of commands to an SMTP server. The server will reply to each of these commands with a response code (just like those HTTP response codes) that lets the client know whether or not the command was successful. We can use a program called `openssl`, which is just like `telnet`, to establish a connection to an SMTP server and then manually send it the commands necessary to send an email via SMTP! If you're using a Mac, this should already be installed for you, and if you're using Windows, you can download it [here](http://openssl.org/related/binaries.html). Now, if we open up a terminal, we can run:

    openssl s_client -ssl3 -connect smtp.gmail.com:587 -starttls smtp -crlf

This command will open up a session with the server at `smtp.gmail.com` on port 587. Here, the **port** refers to the destination port we'll be using to send messages to the server. Remember, different services may send and receive messages over different ports, which allows a single computer to run a variety of services at once! In response to this command, we'll see something like this:

    SSL-Session:
        Protocol  : SSLv3
        Cipher    : RC4-SHA
        Session-ID: xxx
        Session-ID-ctx:
        Master-Key: xxx
        Key-Arg   : None
        Start Time: 1362263768
        Timeout   : 7200 (sec)
        Verify return code: 0 (ok)
    ---
    250 PIPELINING

This means we have a connection to the server, and we're ready to start sending commands. SMTP doesn't define very many commands, since it's the _simple_ mail transfer protocol, after all. Let's say hello to the SMTP server. If we type `helo` at the prompt and then press enter, we'll see something like:

    helo
    250 mx.google.com at your service

Aww, so cute. Just like you need to log in to your account when you visit Gmail.com, you'll also need to log into your account here. To start the login process, type `auth login` at the prompt. You'll get something like this:

    auth login
    334 VXNlcm5hbWU6

Uh... what? That 334 is a response code, though the meanings of numbers are different than the response codes we saw with HTTP. That string of seemingly random characters `VXNlcm5hbWU6` is actually the word "User" encoded using [Base64](http://en.wikipedia.org/wiki/Base64), which is simply _another_ character encoding that translates characters (including non-ASCII symbols) to ASCII characters. Don't worry too much about how or why it's used, but there are many utilities online that will convert words to Base64 for you, like [base64encode.org](http://www.base64encode.org/). Since the server sent a response using Base64, we'll need to reply using Base64 as well. For this demo, we'll use `unicodelovehotel@gmail.com`, which is `dXNlcm5hbWVAZ21haWwuY29t` in Base64. So, let's just paste that string into the terminal and hit enter to send it to the SMTP server. Here's the response:

    dXNlcm5hbWVAZ21haWwuY29t
    334 UGFzc3dvcmQ6

Sigh, Gmail must enjoy being difficult. As you might guess, though, we're now being asked for our password, also in Base64. Let's assume my password is just `password` (which it really shouldn't be...), which is `cGFzc3dvcmQ=` in Base64. Again, let's just paste that and hit enter to send it to the SMTP server.

    cGFzc3dvcmQ=
    235 2.7.0 Accepted

Woohoo! English again! Now, that we've successfully authenticated with Gmail's SMTP server, and we're ready to send a message. We'll first use the `MAIL FROM` command to specify the email address we're sending from:

    mail from:<unicodelovehotel@gmail.com>
    250 2.1.0 OK o5sm28186399qao.12 - gsmtp

Looks good, now we'll use the `RCPT TO` command to specify the email address we're sending to:

    rcpt to:<unicodelovehotel@live.com>
    250 2.1.5 OK o5sm28186399qao.12 - gsmtp

Finally, we can specify the body of our email. To do so, we'll need to send the `DATA` command like this:

    data
    354  Go ahead o5sm28186399qao.12 - gsmtp

Don't mind if I do, Gmail. Just like before, we'll specify a few email headers, followed by our email's body:

    From: <unicodelovehotel@gmail.com>
    To: <unicodelovehotel@live.com>
    Subject: I love cats
    Figured I would send you another reminder that I like cats.
    .

Here, we're not bothering with any kind of multipart encoding; we're just gonna send text. Putting a single `.` on a line and then pressing enter tells the SMTP server that we're all done, and we should see something like this:

    250 2.0.0 OK o5sm28186399qao.12 - gsmtp

And we're done! We just sent an email using Gmail's SMTP server. So, behind the scenes, Gmail.com is following exactly this process to communicate with a Google SMTP server when you press the "Send" button on an email. To recap, our entire session looked like this:

    helo
    250 mx.google.com at your service
    auth login
    334 VXNlcm5hbWU6
    dXNlcm5hbWVAZ21haWwuY29t
    334 UGFzc3dvcmQ6
    cGFzc3dvcmQ=
    235 2.7.0 Accepted
    mail from:<unicodelovehotel@gmail.com>
    250 2.1.0 OK o5sm28186399qao.12 - gsmtp
    rcpt to:<unicodelovehotel@live.com>
    250 2.1.5 OK o5sm28186399qao.12 - gsmtp
    data
    354  Go ahead o5sm28186399qao.12 - gsmtp
    From: <unicodelovehotel@gmail.com>
    To: <unicodelovehotel@live.com>
    Subject: I love cats
    Figured I would send you another reminder that I like cats.
    .
    250 2.0.0 OK o5sm28186399qao.12 - gsmtp

## Reading Emails with POP3

Great, now we know how SMTP handles the sending of emails! Viewing and downloading emails, though, is a whole different process. At this point in the story, we've sent an email from SMTP server A to SMTP server B, and we'd now like to move that message from an SMTP server to somewhere we can read it. Today, there are actually two different protocols for doing just that. First, we'll take a look at **POP3**, the third version of the Post Office Protocol (clever, right?), which defines a process for retrieving emails so they can be read. Though we'll be using different commands this time, this process will be just like the process of sending an email via SMTP, since we'll be sending and receiving messages from a server.

This time, let's make a connection to Gmail's POP3 server with:

    openssl s_client -connect pop.gmail.com:995

Notice that now we're using port 995, since that's what the POP3 standard told us to do. We should see something like:

    SSL-Session:
        Protocol  : TLSv1
        Cipher    : RC4-SHA
        Session-ID: xxx
        Session-ID-ctx:
        Master-Key: xxx
        Key-Arg   : None
        Start Time: 1362265663
        Timeout   : 300 (sec)
        Verify return code: 0 (ok)
    ---
    +OK Gpop ready for requests from w.x.y.z i9pf25304130qag.0

Great, we're connected! Like last time, we'll need to log in. However, since POP3 and SMTP are different protocols, we'll use a different command this time. Assuming we're using the same username and password, we'll log in like this:

    user unicodelovehotel@gmail.com
    +OK send PASS
    pass password
    +OK Welcome.

Phew, no Base64 this time! Instead, we can just use the command `user` followed by our username, followed by `pass` followed by our password. Now, let's say we want to recreate Gmail's homepage and see our inbox. We can use the `list` command like so:

    list
    +OK 334 messages (3177429 bytes)
    1 12622
    2 4726
    ...

Looks like I have 334 emails in my inbox, so I have a busy night ahead of me. Each number in the list represents a different email, and the number in the second column tells us how large the email is (in bytes). To retrieve one of those emails to read it, we can use the `retr` command:

    retr 1

And now, I should see the full contents of an email in my inbox, headers and all. Finally, if we want to delete one of those emails, we can use the `dele` command like this:

    dele 1

So much for my cat email. So, if your email client is using POP3 to read emails from a server, this is exactly what it's doing underneath the hood.

## Reading Emails with IMAP

We said earlier that there are two major protocols for reading email from a server, so let's now take a look at **IMAP**, the Internet message access protocol, which is a bit newer and fancier than POP3. As we saw, POP3 is a bit of a one-way street. We're simply asking the server for information like the messages in our inbox or the contents of a single message, but we're never actually changing anything on the server's end of things. So, if I use POP3 to read an email on my iPhone and then later log in to my account Gmail.com, the server will report that I haven't read that message yet. Pretty annoying, right? IMAP, on the other hand, defines commands that allow us to interact with the server in other ways, so that we can avoid exactly this problem. Other advantages of IMAP include more advanced commands for searching through emails on the server as well as allowing clients to stay connected to the server for longer periods of time. So, when setting up email on your home computer or iPhone, there's a good chance that you want to use IMAP instead of POP3. In fact, many email clients now pre-configure popular email services like Gmail, using IMAP as the default way for fetching mail.

Let's check out how IMAP works by creating a connection to a Gmail IMAP server:

    openssl s_client -crlf -connect imap.gmail.com:993

We should see something like:

    SSL-Session:
        Protocol  : TLSv1
        Cipher    : RC4-SHA
        Session-ID: xxx
        Session-ID-ctx:
        Master-Key: xxx
        Key-Arg   : None
        Start Time: 1362266505
        Timeout   : 300 (sec)
        Verify return code: 0 (ok)
    ---
    * OK Gimap ready for requests from w.x.y.z g4if3992710vcq.28

And we're connected! New protocol, new set of commands. Each IMAP command needs to be prefixed with a different tag; by convention, we'll just use the letter "A" followed by a different number each time. To login, we can send a single command `login`, followed by a username and password.

    a1 login unicodelovehotel@gmail.com password
    * CAPABILITY IMAP4rev1 UNSELECT IDLE NAMESPACE QUOTA ID XLIST CHILDREN X-GM-EXT-1 UIDPLUS COMPRESS=DEFLATE ENABLE MOVE
    a1 OK unicodelovehotel@gmail.com Unicode Love Hotel authenticated (Success)

Good to go! Let's again figure out how many messages are in our inbox, this time with IMAP's `select` command:

    a2 select inbox
    * FLAGS (\Answered \Flagged \Draft \Deleted \Seen $Forwarded $NotJunk)
    * OK [PERMANENTFLAGS (\Answered \Flagged \Draft \Deleted \Seen $Forwarded $NotJunk \*)] Flags permitted.
    * OK [UIDVALIDITY 609988978] UIDs valid.
    * 334 EXISTS
    * 0 RECENT
    * OK [UIDNEXT 75666] Predicted next UID.
    a2 OK [READ-WRITE] inbox selected. (Success)

Sigh, I'm reminded of my long to-do list again. To get my mind off that, let's explore a few ways that IMAP is a bit more powerful than POP3. In Gmail, there's a tab over to the left that allows you to browse the emails you've already sent. Using IMAP, we can access all of the emails that have the "Sent Mail" label, and we can do the same for any other labels we create inside of the Gmail UI:

    a3 select "[Gmail]/Sent Mail"
    * FLAGS (\Answered \Flagged \Draft \Deleted \Seen $Forwarded $NotJunk)
    * OK [PERMANENTFLAGS (\Answered \Flagged \Draft \Deleted \Seen $Forwarded $NotJunk \*)] Flags permitted.
    * OK [UIDVALIDITY 609988982] UIDs valid.
    * 8833 EXISTS
    * 0 RECENT
    * OK [UIDNEXT 11974] Predicted next UID.
    a3 OK [READ-WRITE] [Gmail]/Sent Mail selected. (Success)

We can use the `fetch` command to read emails. If we just want the headers for the first email in our inbox, we can use:

    a4 fetch 1 body[header]

Or, if we want the actual contents of the email, we can use:

    a5 fetch 1 body[text]

Phew, that's enough IMAP for me. As you can see, IMAP gives us a bit more flexibility than POP3 in terms of querying the inbox for information. Still, both protocols are perfectly valid ways of retrieving email from a server.

## Email Clients

If you've ever set up your email on a desktop client like Outlook or your mobile phone, you probably found some instructions online from your email provider and followed them step-by-step without thinking too much about them. However, now that we know all about SMTP, POP, and IMAP, hopefully this process makes a bit more sense. If you open up a mail client on your desktop or mobile device and go into your account settings, you'll probably see a section devoted to incoming mail and one for outgoing mail. Under incoming mail, there's a good chance you'll see some mention of the address of a POP3 or IMAP server, since that's how your mail client can download the emails that were sent to you. Remember, this process is very similar to a web browser retrieving data from a web server; instead of retrieving web page data, IMAP and POP3 will be used to transfer the contents of emails. Associated with the POP3 or IMAP server listed in your email app is probably a port, username, and password, which will be used to log into the server, as we saw before. Similarly, under the settings for outgoing mail, you should see some mention of an SMTP server that your app will connect to and issue a series of commands just like the ones we sent earlier. For example, the settings page for my iPod's outgoing mail looks something like this:

![iPod Email](/static/img/content/chapters/email/ipod-email.png)

Similarly, the instructions for setting up an email client to work with Gmail can be found [here](http://support.google.com/mail/bin/static.py?hl=en&page=ts.cs&ts=1668960&from=75726&rd=1). Do those IMAP and SMTP settings make sense?

## Phishing

Before we finish up, a quick note on email security. We saw that the process of sending an email really just involves logging into a server and sending a series of textual commands. Earlier, I sent email from `unicodelovehotel@gmail.com`, an address that I proudly own. However, there's nothing stopping anyone from typing in any old email address with the `mail from` command or the `From` header. While Gmail's SMTP server has some security measures in place to prevent us from doing that, there's nothing stopping me from running my own SMTP server and sending emails as anyone in the world. So, an attacker might be able to convince unsuspecting email users into sending along their Facebook password, for example, by sending an official-looking email from `zuck@fb.com`. Or, I might send an email from `barack@whitehouse.gov` complete with a picture of the White House instructing recipients to click a link leading to a virus. Of course, even if I send email as `barack@whitehouse.gov`, I have no way of actually receiving mail to that address unless I can log into the POP3 or IMAP server that receives emails. Still, this kind of attack, called **phishing**, can lead to some pretty convincing spam!

That's enough email for now! I think it's time for me to take a break and go tend to my growing inbox. In the next section, we'll dive a bit deeper into how exactly data is transmitted over the Internet at a more fundamental level!
