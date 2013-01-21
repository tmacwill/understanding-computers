---
layout: default
title: Binary, ASCII, and Everything in Bit-ween
---

<link rel="stylesheet" type="text/css" href="css/2-binary.css" />

<div class="page-header">
    <h1>Chapter 2 <small>Binary, ASCII, and Everything in Bit-ween</small></h1>
</div>

You've probably heard that computers are all about zeroes and ones. But... what does that mean? And... why? After all, two and three are pretty great numbers, too! (But don't get me started on seven.)

Let's say I ask you a question like "Do you like cats?" There are two possible answers to this question: yes and no. We can represent your answer to this question using one **bit**, which is the most basic unit of information in computing. A bit can only have two possible values, which we can think of as "on" or "off," "true" or "false," or finally, if you're a computer, "0" or "1". We can also use a bit to represent, for example, whether a light is on or off, the result of a coin flip, or the sign of a magnet.

Answering the question "How much do you like cats?" is a _bit_ different (pun fully intended). This question has more than one answer; you could say you kinda like cats, you really love cats, you couldn't live without cats, and so on. You could also think about answering this question on a scale from one to five, a scale from one to ten, etc. Either way, we'll need more than just one bit to represent your love of all things feline, since a 0 or a 1 doesn't cover all of the possible answers to this question.

However, before we talk any more about how computers represent numbers, let's quickly review how we as humans are probably used to representing numbers. According to my laptop's keyboard, we have ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. (We call this the **decimal** system.) That means that we can represent ten different numbers using only one digit. Of course, we're going to start running into issues when we want to represent the number that is one more than 9. Luckily, we've already solved this problem: one more than 9 is 10. To create the number 10, we created a new space for a second digit, which you may remember as the "tens place" from grade school (that is, if you weren't too busy playing with yo-yos like I was). Similarly, we have a hundreds place, thousands place, and so on for larger numbers.

The fact that we use ones, tens, hundreds, and thousands is no accident. We have 10 different digits to choose from, and 10<sup>0</sup> = 1, 10<sup>1</sup> = 10, 10<sup>2</sup> = 100, and so on. (Remember, when we say something like 10<sup>3</sup>, that's just short for 10 &times; 10 &times; 10, or 1000.) So, these places can be represented with a table like this:

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>10<sup>4</sup></td>
        <td>10<sup>3</sup></td>
        <td>10<sup>2</sup></td>
        <td>10<sup>1</sup></td>
        <td>10<sup>0</sup></td>
    </tr>
</table>
<br />

Let's fill in these blanks with some digits:

<br />
<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>2</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>3</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>4</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>5</strong>&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>10<sup>4</sup></td>
        <td>10<sup>3</sup></td>
        <td>10<sup>2</sup></td>
        <td>10<sup>1</sup></td>
        <td>10<sup>0</sup></td>
    </tr>
</table>
<br />

Now, to figure out what number is represented by those digits, we multiply the digit in the ones place by 1, the digit in the tens place by 10 (and so on), and then add them together. That means that the above number is:

<br />
(1 &times; 10<sup>4</sup>) + (2 &times; 10<sup>3</sup>) + (3 &times; 10<sup>2</sup>) + (4 &times; 10<sup>1</sup>) + (5 &times; 10<sup>0</sup>) =
10000 + 2000 + 300 + 40 + 5 = 12345
<br />
<br />

Make sense? Alright, back to those zeros and ones. Remembering _ten_ different digits can be hard work. Heck, I can barely remember birthdays. Let's make one tiny change to the above table. Rather than having places for 10<sup>0</sup>, 10<sup>1</sup>, 10<sup>2</sup>, and so on, let's instead create places for 2<sup>0</sup>, 2<sup>1</sup>, 2<sup>2</sup>, and so on:

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

This representation is called **binary** (as opposed to decimal). In this world, we'll represent numbers using a ones place, a twos place, a fours place, an eights place, a sixteens place, and so on. Now, rather than using ten digits to represent numbers, we'll only use two: 0 and 1. That means that we can represent each digit in a binary number with one bit. Any number then, can be represented as a collection of bits! 

Let's see how we can use bits and binary to represent numbers by translating the binary number 10110 into decimal. First, we'll fill in our new table, this time using only zeroes and ones:

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>.
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

To figure out what number these bits represent, let's do the same thing we did before, but rather than using powers of 10, we'll use powers of 2:

<br />
(1 &times; 2<sup>4</sup>) + (0 &times; 2<sup>3</sup>) + (1 &times; 2<sup>2</sup>) + (1 &times; 2<sup>1</sup>) + (0 &times; 2<sup>0</sup>) =
16 + 0 + 4 + 2 + 0 = 22
<br />
<br />

And that's it! The binary number 10110 is the same as the decimal number 22.

For reference, here's a handy dandy chart listing the first few powers of 2, which will be helpful when working with binary numbers.

<br />
<table>
    <tr>
        <td>2<sup>0</sup></td>
        <td> = </td>
        <td>1</td>
    </tr>
    <tr>
        <td>2<sup>1</sup></td>
        <td> = </td>
        <td>2</td>
    </tr>
    <tr>
        <td>2<sup>2</sup></td>
        <td> = </td>
        <td>4</td>
    </tr>
    <tr>
        <td>2<sup>3</sup></td>
        <td> = </td>
        <td>8</td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td> = </td>
        <td>16</td>
    </tr>
    <tr>
        <td>2<sup>5</sup></td>
        <td> = </td>
        <td>32</td>
    </tr>
    <tr>
        <td>2<sup>6</sup></td>
        <td> = </td>
        <td>64</td>
    </tr>
    <tr>
        <td>2<sup>7</sup></td>
        <td> = </td>
        <td>128</td>
    </tr>
    <tr>
        <td>2<sup>8</sup></td>
        <td> = </td>
        <td>256</td>
    </tr>
    <tr>
        <td>2<sup>9</sup></td>
        <td> = </td>
        <td>512</td>
    </tr>
    <tr>
        <td>2<sup>10</sup></td>
        <td> = </td>
        <td>1024</td>
    </tr>
</table>
<br />

Let's try another one. What's decimal representation of the binary number 01101? First, let's fill in the table:

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>.
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

Now, let's add everything up:

<br />
(0 &times; 2<sup>4</sup>) + (1 &times; 2<sup>3</sup>) + (1 &times; 2<sup>2</sup>) + (0 &times; 2<sup>1</sup>) + (1 &times; 2<sup>0</sup>) =
0 + 8 + 4 + 0 + 1 = 13
<br />
<br />

So, 01101 is the lucky number 13!

What if we want to go the other way? Let's say we have the decimal number 12, and we want figure out its binary representation. Using the same table, we can work backwards by filling in each space. The process of convering a decimal number to binary is just like making change at a cash register. So that you don't annoy your customers, you always want to make change using as few coins as possible.

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

Let's start all the way at the left. 2<sup>4</sup> = 16, which is bigger than 14. That means there can't possibly be a 1 there, so we can put a 0 in the first space. If we were making change at a cash register, putting a 1 in the first space case would be like giving someone who was owed 23 cents a quarter.

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

Now we'll move to the next space. 2<sup>3</sup> = 8, which is smaller than 14, so we want to put a 1 in the second space. Remember, we want to make change using as few coins as possible, so if at any point we can put a 1 in a space without creating too large a number, we should. If we don't, then we could end up giving our customer five pennies when we could have simply used one nickel. Now our table looks like this:

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

Okay, now we've "made change" for 8 out of 14, so we have 6 to go. The next space is a 4, which is less than 6. So, we again want to put a 1 in that space to get:

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

Alrighty, 2 to go. That means the next space, the 2s place, must be a 1, since that would give us the grand total of 14 that we were looking for! We can mark the last remaining space with a 0. Our final table looks like this:

<table style="text-align: center">
    <tr>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>1</strong>&nbsp;&nbsp;</u></td>
        <td><u>&nbsp;&nbsp;<strong>0</strong>&nbsp;&nbsp;</u></td>
    </tr>
    <tr>
        <td>2<sup>4</sup></td>
        <td>2<sup>3</sup></td>
        <td>2<sup>2</sup></td>
        <td>2<sup>1</sup></td>
        <td>2<sup>0</sup></td>
    </tr>
</table>
<br />

Phew! The binary representation of 14 is 01110.

I dunno about you, but I'm getting tired of numbers. In fact, we probably use letters (and maybe other symbols) more than we use numbers while using a computer on a daily basis. But, computers are still all about zeroes and ones, so how can we represent non-numeric values?

To solve this problem, we can create a "character encoding," which maps something to letters or symbols. For example, ships utilize a character encoding in which each letter is represented by a different flag. When a ship needs to broadcast a message consisting of English letters, the crew can instead fly a sequence of flags. Others can then understand this message because there exists a standardized, agreed-upon translation from flag to English letter. In case you're as curious as I was, here's the International Maritime Signal Flag character encoding:

![International Maritime Signal Flags](img/2-maritime.gif)

You may also have heard of Morse Code, which is another character encoding. Here, each letter is represented by a series of sounds. Again, this standardized mapping allows us to transmit English messages without actually using any English letters.

<img src="img/2-morse.jpg" style="width: 600px" alt="Morse Code" />

Since flags and sounds are a bit impractical for your computer, a character encoding called **US-ASCII** is more common. ASCII defines numerical representations for 128 different "characters," where a character can be a letter, number, symbol, or Mickey Mouse. For example, the character "A" is represented by the number 65 in ASCII, and the character "a" is represented by the number 97. So, whenever we need to represent the character "A" using ASCII, we can simply use the number 65 instead, just like a ship would fly a blue and white flag. Since we've already seen that binary can be used to represent numbers using only zeroes and ones, we can use ASCII to represent letters using zeroes and ones as well. Here's the complete ASCII table:



ASCII Table Diagram



The first 32 characters in the table are reserved for "control sequences," which back in the day could be used to control physical devices like printers. Not only are those not so relevant any more, but what if we go to jolly old England and inquire as to the price of a spot of tea? The standard ASCII table doesn't have the character &pound;, but luckily, ASCII isn't the only character encoding around. While we also have an extended version of ASCII that is double in size, an encoding called **UTF-8**, which contains definitions for 1,112,064 different characters, is commonly used today. In fact, there's a good chance that any website you're browsing is using UTF-8 (and there's a 100% chance this one is). Among the millions of UTF-8 characters are the "snowman" (&#9731;), "heavy black heart" (&#10084;), and even the "neither less than nor greater than" (&#8824;), not to be confused with the more common "equal to" (=). Still, at the end of the day, that snowman is really just represented as a series of bits that can be translated into a winter wonderland using an agreed-upon standard.

As we start using these character encodings to create long messages, we're going to create larger and larger sequences of bits. It makes sense, then, to create units of information larger than a single bit. A sequence of 8 bits is commonly referred to as a **byte**. As an aside, the official technical term for a sequence of 4 bits is a **nibble**, ha, ha, ha. Since a byte is still a pretty small piece of information, describing data in terms of **kilobytes** (where 1 kilobyte is about 1000 bytes), **megabytes** (where 1 megabyte is about 1000 kilobytes), and **gigabytes** (where, you guessed it, 1 gigabyte is about 1000 megabytes) has become commonplace. More on that later!

That's it for binary and ASCII! In the next chapters, we'll start to see how your computer uses and stores data.

<div class="page-header page-break">
    <h1>Practice Problems</h1>
</div>

1. Convert the following numbers from decimal to binary, showing each step.

    a. 50

    b. 164

    c. 12345

1. Convert the following numbers from binary to decimal, showing each step.

    a. 0101010

    b. 010101111

    c. 01111011010010

1. What do all binary numbers ending in 1 have in common?

1. We've seen that decimal uses ten different digits and binary uses two different digits. The octal system instead uses seven different digits, but works in exactly the same way. What is the decimal value of the octal number 0644? How about 0755?

1. What's the binary representation of the ASCII character "T"?

1. How many bits are used to represent a standard US-ASCII character?

1. Why isn't 1 the ASCII code for the character "1"?
