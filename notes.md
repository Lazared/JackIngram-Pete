Several Scenarios -


#Problem statement 

##Solutin design 
- Implementation
    10 teams , single-robin league --> 45 games in total, eacch team single with  every other team.
- Iteration
    We add movement and scoring
- Simple 1
    Simulate the league
- Mid 
    we move the attackers
- Complex
    move attackers by game player and update the league

###Quick and free footbal game people can play

Game Definition: one attack pe team, win or draw
Players need to interact with the game 
- move the player with arrows, A for attack, `Space` to shoot for goal
- simulator needs rethinking - add a path  then shoot.
A - is the start of attack
-    Attackers will advnace on a given path , one has the ball , can pass to other or shoot. 
    -   iteration: goalkeeper starts jigging
    - When you press `Space` the attacker with the ball will try to score.
    -  If colision on the path of ball to goal , then is save` else is win
    - Games is complete upon 2 attacks , one per team
    - Record score and update tables with results

Remove the timer - we use the league settings - single or double robin
Every time a game starts - we need to inject the right teams in the match 
We will use a queue to run all the games for the league


Settings - Enviroment setup

single robin - 45 games to complete the league , each team plays only once
we already have a simulator for each game 
    Games played vs remaining diplay
