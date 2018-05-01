# Detailed Project Description
#### [Return to the project overview](index.md)
## Story (Project Evolution/Narrative)

Our initial project goal was to learn about simple game-playing AI through designing and implementing a 'CPU' type player in a preexisting build of Tron Light Bikes created by one of our team's members in a previous project:

![Screenshot of existing two-player Tron Lightbikes Game ](imgs/Existing_game.png)

Initially, we intended to create a game with both AI and machine learning as well as varied playing fields that could include game modes, obstacles of various, and different levels. Our proposed game modes included the preexisting Player vs. Player mode as well as adding a Player vs. a combination of Players and CPUs, which could be selected from a splash screen. In addition, taking inspiration from another team member's previous project, a dynamic background mode in which multiple CPUs play each other to create random geometric art was proposed.

Initial System Architecture Diagram
![Initial System Architecture Diagram](imgs/Initial_Arch_Diagram.png)


We all shared the common goals of gaining familiarity and comfort with working on a software project collaboratively, which was accomplished through compartmentalizing each class, allowing multiple team members to work on the project simultaneously without interfering with each other. Additionally, since none of us had any experience with game-playing AI, we all began the project with the goal of building a conceptual understanding of how it works, as well as gaining experience with building a rudimentary AI.


Based on the feedback form and in-class discussion from the first architectural review, we elected to emphasize the multiplayer with CPUs aspect of our game. Our reviewers seemed to see little merit in the dynamic background mode, with most of our feedback surrounding user experience and the game’s features. In terms of graphics and visuals, our reviewers suggested adding more ‘tron-like’, less ‘pygame-like’ overall graphics feel, with sound effects, obstacles, and themes. More complex features such as adding physics (deceleration/acceleration/turning radius to the ‘bikes’) or multiple CPUs running on different AI architects were also suggested. Nearly all of our reviewers were strong proponents of the mixed Player vs. Player vs. CPU(s) mode. Unfortunately, all the insight we were able to gain, though valuable, was fairly superficial, and we were unable to gain significant insight into where to start with AI design and implementation, which remained a 'black hole' of knowledge and comprehension for the team. We were, however, encouraged to implement several types AI, to rank them based on difficulty and win rate.

As we began to delve into creating an AI (machine learning had been abandoned due to its complexity), we explored several strategies including A*, Breadth First Search, Dijkstra's Algorithm, and, after meeting with a knowledgeable upperclassman, Flood-Fill MiniMax, which we elected to implement:

![Updated System Architecture Diagram for AR2](imgs/Updated_Arch_Diag.png)

Our feedback from the second architectural review supported a narrowing of our previous goals to implement only an AI, as progress was slow and our deadline approached quickly. Since our reviewers had little experience with developing AI algorithms, we instead discussed the potential behaviors of our AI. The general consensus was that a defensive bot would probably be easier to begin with, as an aggressive bot would also need to predict the players’ next moves. However, many did think that once the minimax was refined it would be interesting to also attempt a more aggressive bot.


* Add final architectural diagram
* Finish when game is done

* Description of our motivations, goals, and game background
* Show evolution of goals through AR architectural diagrams
* Describe how feedback from the ARs was incorporated



## Implementation
(to be added)
* Updated architectural diagrams (inheritance and dependencies from each class to class)
* Description of AI MiniMax Flood fill
  * Add bits of critical code
* Simple diagram or gif of flood fill
* Flow chart of diagram function
* Use progressive mid-game screen caps to show how AI works


## Detailed Game Description (results)
(to be added)
* Screen caps of game play and various features
* Show AI effectiveness through end-game screen caps
