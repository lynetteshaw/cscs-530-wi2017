# Game Theory Examples

Examples and Python implementations are taken from our _Think Complexity_ textbook. I have also included a prior in-class notebook we used to look at parameter sweeps. 


### Prisoner's Dilemma

To explore an earlier implementation of the Prisoner's Dilemma game we discussed in class, see **2_3_pd-sweep.ipynb**.

If you are interested in getting going on your own player tournament, use the following exercise instructions from _Think Complexity_ (p. 96 - 97):

> Download thinkcomplex. com/ Referee. py , which runs the tournament, and thinkcomplex. com/ PlayerFlipper. py , which implements a simple player strategy.
>
> Any file that matches the pattern Player &ast;.py is recognized as a player. The file should contain a definition for move, which takes the history of the match so far and returns a string: 'D' for defect and 'C' for cooperate.
>
> **_history_** is a pair of lists: the first list contains the player’s previous responses in order; the second contains the opponent’s responses. 
>
> **_PlayerFlipper_** checks whether the number of previous rounds is even or odd and returns 'C' or 'D' respectively. 
>
> Write a **_move_** function in a file like PlayerFlipper.py, but replace “Flipper” with a name that summarizes your strategy. 
>
> Run Referee.py and see how your strategy does.


### Volunteer's Dilemma

See this week's reading of Chapter 14 of _Think Complexity_ for a description of the Voluneteer's Dilemma and the implementation provided here.

### Norms Game

See this week's reading of Chapter 14 of _Think Complexity_ for a description of the Norms Game and the implementation provided here. Note this game is based off of the genetic algorithms uses in Axelrod's "Promoting Norms: An Evolutionary Approach to Norms" and incorporates evolution via basic mutation of strategies!
