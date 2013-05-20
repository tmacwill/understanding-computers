<div class="page-header">
    <h1>Chapter 19 <small>Tonight's Programming</small></h1>
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

Just like last time, let's start with a simple statement. Where in Scratch we had a "say" block to make a character display some text to the user. In Javascript, we can do the same thing with the `alert` function:

    `alert("Hi there!");

Since we don't have a nice yellow block that contains the text we want to say, we'll put our message inside of parentheses instead. Notice how we're also ending our statement with a semicolon, just like we ended all of our CSS rules with a semicolon. When this Javascript code is run, a pop-up message with the text we've specified will be displayed to the user.

Alright, what about variables? In Scratch, we created and modified variables using the red variable block. To create a variable called `cats` in Javascript, we'd say something like:

    var cats = 2;

Uh oh, looks like math class at first, but don't worry! The `var` keyword means that we're creating a brand new variable that doesn't exist yet. Next, we decided to call our variable `cats`, and it has a value of `2`. Just like last time, we have a semicolon at the end of our line. Variables aren't limited to just numbers, and we can make a variable equal to a string (which is just a sequence of characters) using quotes:

    var name = "Boots";

Okay, now that we have variables, let's use them in some conditions. We saw "if-else" blocks in Scratch, so let's translate those to Javascript.

    if (cats == 2) {
        alert('You have two cats!');
    }
    else {
        alert('You do not have two cats!');
    }

Looks pretty similar to what we did in Scratch! First, check out the Boolean expression `(cats == 2)`. We saw that we can use a single `=` to set the value of a variable, so we'll use a double `==` when we want to compare the value of variables. We could have also said `(cats > 2)` if we wanted to check if the value of the `cats` variable is more than 2. After our expression, we have curly braces, just like we did in CSS. Inside of the curly braces will be the code that we want to be run if our condition is true. In Scratch, we were able to put blocks inside of the "if" block, so in Javascript, we'll put code inside of these curly braces. After we close the curly braces for the `if`, we have another set of curly braces for the `else`.

We can also combine Boolean expressions, just like we did in Scratch:

    if (cats == 2 && name == "Boots")

Here, the `&&` is the same as "and". If we instead wanted to say "or", we would say:

    if (cats == 2 || name == "Boots")

Finally, let's translate loops from Scratch to Javascript. Remember, we used loops to execute the same Scratch blocks more than once. If we used a "Forever" loop, then the blocks inside of the loop would run... forever! That might not always be the best idea in the world, so we'll want to define some kind of stopping condition for some of the loops we write. In Javascript, we'll define some block of code that will be run over and over again until some condition is no longer true. Here's what that looks like:

    var counter = 1;
    while (counter <= 10) {
        alert(counter);
        counter = counter + 1;
    }

Woah, lots of code, let's break this down line by line. In the first line, we're creating a new variable called `counter` and setting its value equal to the number `1`. Next up is our loop: we'd like to run some block of code while the value of the `counter` variable is less than or equal to 10. Since counter starts off as `1`, we know this will be true at least once. Then, we have a pair curly braces again, and just like before, these will demarcate what code we'd like to run repeatedly. Inside of the curly braces, we have our old friend `alert`, which will display the value of the `counter` variable to the user. Finally, the last line of our loop increments the value of the `counter` variable. If `counter` had a value of `1`, it would have a value of `2` after this line. Since we're out of lines to execute within the loop, we'll jump back to the top of the loop to run everything again. After one run, or **iteration**, of this loop, our `counter` variable will be `2`, which is most definitely less than or equal to `10`, so it will run again. Eventually, though, our `counter` will have a value of `11`, which will cause us to break out of the loop and move on.

Rather than using the `while` keyword, we can express the same exact thing with the `for` keyword and fewer lines of code:

    for (var counter = 1; counter <= 10; counter++) {
        alert(counter);
    }

Alright, looks like we've compressed our last code snippet down quite a bit. It looks like we're still creating a `counter` variable that starts off with a value of `1`, and we're still running this loop until the value of `counter` exceeds `10`. That `counter++` bit is just a shorthand for `counter = counter + 1`, and it will be run _after_ the contents of the loop. So, this `for` loop is exactly the same as the `while` loop above!

Phew! That was a lot of Javascript. Now, let's take a look at how we can actually integrate Javascript into our web page. Just like we had a `<style>` tag in which we could write some CSS, HTML also gives us a `<script>` tag in which we can write some Javascript. So, if we wanted to display a pop-up on an HTML page that appeared as soon as the user opened it, we could do something like this:

    <!doctype html>
    <html>
        <head>
            <title>Tommy's Cat Store</title>
            <script>
                alert("We love cats!");
            </script>
        </head>
        <body>
            <h1>Tommy's Cat Store</h1>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="cats.html">Cats</a></li>
            </ul>
            <h2>We love cats.</h2>
        </body>
    </html>

Of course, pop-ups are pretty annoying, so I wouldn't recommend _actually_ doing that. Just like it was nice to move all of our CSS into a separate, CSS-only file, we can do the same thing with Javascript. We can also use the `<script>` tag to specify the location of a Javascript file like this:

    <script src="cats.js"></script>

Annoyingly, we can't just say `<script />` here, but that's okay I guess. We'll get over it.

That's all the Javascript we'll see for now! If you're interested in learning more, there are lots of resources available online. But, the main takeaway here is that the concepts we've covered in Scratch will apply to most any programming language we look at!

Now go forth and make something awesome.
