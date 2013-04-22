---
layout: default
title: Web Development
---

<div class="page-header">
    <h1>Chapter 19 <small>Programming</small></h1>
</div>

Last time, we saw how we could make static web pages using HTML and CSS. Now, let's see how we can actually make those pages _do_ something!

## Programming

**Programming** is how we get computers to do our bidding. Just kidding, but not really. A computer **program** is simply a set of specific instructions that a computer will dutifully execute. We'll need to be very specific in our instructions, which can be a challenge! Our computer will always do exactly what we tell it to do, but it isn't always obvious what exactly we should tell our computer.

We'll first take a look at a programming language called [Scratch](http://scratch.mit.edu). Using Scratch, we can drag and drop different constructs to create a program.

Once we open up Scratch, we can see a single cat **sprite**, which is simply a character or object that we can manipulate. The sprite is placed on a **scene**, which represents our two-dimensional world. We can attach **scripts**, or sets of instructions, to both sprites and the scene. Let's take a look at the differnet components that we can use in a script.

* **Statements** are things that we can _do_. For example, statements might include "Say hello," "turn to the right," and "pause for 3 seconds."

* **Boolean expressions** are questions that are either true or false. In Scratch, some conditions include "Is this sprite touching the mouse?" and "Is the mouse clicked?"

* We can also combine Boolean expressions to form expressions like "Is the mouse clicked or is the space bar pressed?" and "Is the mouse down and is this sprite touching something?"

* We can use Boolean expressions in **conditions**, which allow us to do different things based on the current state of the world. Much like a choose-your-own-adventure novel (remember those?), our script can branch off depending on whether or not a Boolean expression is true or false. Typically, we'll say "if something is true, do this, else, do that".

* **Loops** allow us to do something more than once. If we wanted our cat to meow three times, we could drag the same statement over three times in a row, but that would be kinda annoying. Instead, we can enclose some sequence of statements that will be run over and over again until some condition is met.

* **Variables** allow us to store information that we can access later. For example, our cat might ask the user what his or her name is. Impressive that Scratch comes with talking cats, right? After the we answer, the cat can remember our answer in a variable that can be used later in the script.

* **Arrays** are lists of variables. If we were making a program to keep track of our shopping list, we could store all the items that we want to buy in an array of **strings**, where a string is simply a sequence of characters (like a word).

And that's it! Using this small set of constructs, we can create some amazingly complex programs. In Scratch, we can attach scripts to any number of sprites. When we start our program, multiple scripts can be executed at the same time, and we can call each individual script a **thread**. By the way, in Scratch, we'll need to use a special block that says "On green flag clicked" as the starting point for our scripts if we want it to start executing when the user starts our program.

Of course, we might not want all of our scripts to start when the user starts the program. Instead, we might want our scripts to start when a certain **event** occurs. In Scratch, we can define our own events that other sprites can respond to. For example, when we click on a sprite, it might say "Marco" and **broadcast** an event to every other sprite. Sprites that are **listening** for this event can then respond by saying "Polo" (or anything else).

## Javascript

We can apply the same concepts we just saw in Scratch to other programming languages. Let's take a look at Javascript, which just so happens to be my favorite programming language (surprise!). Since Javascript doesn't feature nice drag-and-drop blocks, we'll have to type out our computer programs. Let's translate a few of the concepts we saw in Scratch to Javascript.
