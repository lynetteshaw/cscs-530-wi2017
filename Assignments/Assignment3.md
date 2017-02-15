# CMPLXSYS 530 
## Assignment 3: Python Practice - Langton's Ant
### Due: Friday, 2/24/2017


**Instructions for Submission**

Submit .py files and writeup via EITHER Canvas OR by providing me a link to your own Github repository (see "Getting Started with Github" for guidance on this).
 
 
&nbsp; 

### Langton's Ant
 
 At the end of Chapter 7 in _Think Complexity_ (p. 73), Downey discusses a class of CA variants known as "Turmites." He focuses specifically
 on one famous one known as "Langton's Ant":
 
> The most famous Turmite is Langton’s Ant, discovered by Chris Langton in 1986. See
> http://en.wikipedia.org/wiki/Langton_ant.

> The ant is a read-write head with four states, which you can think of as facing north, south,
> east or west. The cells have two states, black and white.

> The rules are simple. During each time step, the ant checks the color of the cell is it on. If it
> is black, the ant turns to the right, changes the cell to white, and moves forward one space.
> If the cell is white, the ant turns left, changes the cell to black, and moves forward.

> Given a simple world, a simple set of rules, and only one moving part, you might expect
> to see simple behavior—but you should know better by now. Starting with all white cells,
> Langton’s ant moves in a seemingly random pattern for more than 10,000 steps before it
> enters a cycle with a period of 104 steps. After each cycle, the ant is translated diagonally,
> so it leaves a trail called the “highway.”

&nbsp; 

### Assignment

**1)** Write your own implementation of Langton's Ant in Python. Feel free to rely heavily on existing CA code available through either PyCX, the repository associated with the 
_Think Python_ and _Think Complexity_ texts, or other code that has been made available for reuse and modification (please provide the original source if you go this route). 
To state the obvious, you should  _NOT_ just copy an existing implementation. You are only cheating yourself out of some practice by doing so.

&nbsp;

**2)** Once you've developed this basic implementation, take it another step further to implement **_one_** of the following variants:

- Look at different variations on boundary conditions (wrapped, fixed, etc.)
- Multiple ants. Ants can either have the same rules or have simple modifications of the existing one (e.g. turn left vs. turn right on a black cell)
- Allowing for more than two possible "colors" for the cells (i.e. expanding. Note, this will require updating the rules for your ant.

&nbsp;

**3)** The writeup for this will be simple. Basically, just give me a few paragraphs describing your general observations and anything you found particularly interesting. 
Also include some images of your system to illustrate what you are talking about. If you are feeling particularly ambitious, feel free to come up with some quantitative 
metrics to characterize the system and look at how different conditions affect them.

&nbsp;


#### Things to Bear in Mind

- You can actually think about Langton's Ant as _either_ an agent(s) moving across a space _or_ a grid of cells in which only the cell, or cells if there are multiple "ants," 
which have most recently changed are "active" and executing the rules that will change one of their neighbors' states. How you choose to think about this will change how you 
approach your implementation.

- Note that in the case of a single Langton's ant, _10,000_ steps are required before it suddenly transitions from a seemingly chaotic to a highly ordered pattern. Concordantly, 
you may want to watch you simulation run for awhile to see the most interesting behaviors.

- Depending on the path you take to doing so (e.g. using the PyCX simulator, creating series of plots using matplotlib, etc.), rendering animations for a very big grid may prove very slow. 
This doesn't mean you can't look at big spaces, but you might need to have some patience, consider increasing the step interval between frames, or find a creative way to update your frames. 

- Like with other CAs, there should be ways to implement this with arrays, lists, and/or classes. Do what makes the most sense to you! 



