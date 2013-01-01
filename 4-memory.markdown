---
layout: default
title: Thanks for the Memory
---

<link rel="stylesheet" type="text/css" href="css/4-memory.css" />

<div class="page-header">
    <h1>Chapter 4 <small>Thanks for the Memory</small></h1>
</div>

As promised, we'll now take a look at what your CPU does with those millions of computations per second. Just like you have the ability to recall memories, your computer has the ability to store information for both the short and long term. As you might expect, the space reserved for short-term memory is generally smaller and easier to access, while the hardware dedicated to long-term memory is usually larger and more time-consuming to use. We'll begin our exploration of the various types of memory with the smallest and fastest available to the computer and work our way up to the biggest and baddest!

First, though, let's review some terms that describe the size of data. The smallest piece of data we can represent in memory is a single **bit**, where a bit is simply zero or one. It's not usually that useful to store pieces of information that small, so we usually talk about data in terms of **bytes**, where one byte is simply 8 bits. As we saw, one byte is roughly the size of a few ASCII characters. Still pretty small, so we can go all metric system and add some prefixes. One **kilobyte** is equal to 1000 bytes, and kilobyte is frequently abbreviated as **KB**. A Word document with a couple pages of text (i.e., no images) is between 5-15 kilobytes, that picture of the Harvard Mark I from the previous section is about 130 KB in size, and the text of books like _The Adventures of Tom Sawyer_ and _Frankenstein's Monster_ are just under 500 KB. Next up is a **megabyte**, which is the same as 1000 kilobytes and abbreviated as **MB**. A high resolution image will probably come in at a few megabytes, as will MP3s of popular songs. Ke$ha's masterpiece "We R Who We R", which is 3 minutes and 25 seconds of pure artistry, measures about 3 megabytes, while everyone's favorite party song, the "Cha Cha Slide" by DJ Casper, is about 6 MB at 6 minutes and 19 seconds long. CDs can hold about 700 megabytes of data. After a megabyte comes a **gigabyte**, which is equal to 1000 megabytes and abbreviated **GB**. A standard-definition movie downloaded from iTunes is probably around a gigabyte in size, while high-definition Blu-Ray disks can hold about 25 GB. Shopping for a new computer, you'll often see the total storage capacity given in terms of gigabytes as well. A **terabyte** (**TB**) is equivalent to 1000 megabytes, and the printed collection of the Library of Congress is roughly 10 TB. After a terabyte is a **petabyte** (**PB**) followed by an **exabyte**; as a point of reference, the text of all words ever spoken by human beings is esimated to come in at a few exabytes.

In summary:

<table id="storage">
    <tr>
        <td>Byte</td>
        <td>B</td>
        <td>8 bits</td>
        <td>Characters of text</td>
    </tr>
    <tr>
        <td>Kilobyte</td>
        <td>KB</td>
        <td>10<sup>3</sup> bytes</td>
        <td>Word document, small image</td>
    </tr>
    <tr>
        <td>Megabyte</td>
        <td>MB</td>
        <td>10<sup>6</sup> bytes</td>
        <td>MP3 song, large image</td>
    </tr>
    <tr>
        <td>Gigabyte</td>
        <td>GB</td>
        <td>10<sup>9</sup> bytes</td>
        <td>Movie, ~350 photos, ~250 songs</td>
    </tr>
    <tr>
        <td>Terabyte</td>
        <td>TB</td>
        <td>10<sup>12</sup> bytes</td>
        <td>~350,000 photos, ~250,000 songs</td>
    </tr>
</table>
<br />

Just when you thought we were done with the [CPU](3-cpu.html), we're heading right back there. Turns out that a few different types of memory are actually found directly on the CPU. The smallest and fastest memory on the CPU is found in **registers**. Registers hold extremely small amounts of data: on the order of several bytes. Earlier, when we said that a CPU could add two numbers together, we took for granted where those numbers would be coming from and where the answer would go. This is where registers come in! While the CPU is in the process of adding two numbers together, both numbers are stored in registers, and once the CPU has computed the answer, the result is also stored in a register. Registers are also used to keep track of things like the instruction that is currently being decoded or executed as well as what instruction should be put into the pipeline next. Since registers are so small, there's not much more that could even fit in a CPU register. But, in order for the CPU to quickly perform its addition, accessing register data must be extremely fast, so we have a bit of a trade-off between the size of the memory and the speed of the memory. In fact, we'll see this trade-off become a trend throughout this section! The number of registers on a CPU can vary, with some CPUs having just 16 registers and others having as many as 256 registers.

<div class="page-header page-break">
    <h1>Practice Problems</h1>
</div>

1. I just purchased a shiny new 32 GB iPod Touch. About how many songs can I put on it?

1. My good friend is a budding photographer wondering what size memory card he should buy. How many photos will fit on the 8GB card he's looking at?
