# AI801-surviving-in-tetris

Tetris is not a solved game. With the individual pieces being randomly generated and only the next 3 in the queue visible, it is next to impossible to anticipate all of the possible future game states from the current state. Depending on the performance of the agent, the game has the possibility to continue endlessly. While true, the original Atari version was, in a way, beatable. Due to hardware limitations, the game would fail to continue after some point, resembling a “win” as the game ended [2]. Because of this, our group will attempt to build an artificial intelligence with an objective of beating the original Atari version of Tetris. The program will be graded on its ability to go the distance (reach level 127). The expected outcome from this AI will be one that is able to interact with an environment that resembles Tetris, and will be able to place moves until either failure or success.

This project has the opportunity to take advantage of Problem Solving and Uninformed/Informed Search for picking the best move, Game Playing for playing the game, Knowledge Based Agents for tackling the problem at hand, Uncertainty handling and probability for the unknown pieces you could receive next in line. Reinforcement learning can be used to have the model play the game, and iteratively improve its decision making process.

## Requirements
- Python 3.5 (a virtual environment is probably a good idea)

## Setup
```bash
cd ~
brew install pyenv
pyenv install 3.5

pyenv init
## Follow the instructions pyenv gives to set up your bash config.
pyenv shell 3.5
python3 --version ## Python 3.5.10
python3 -m venv .venv
source .venv/bin/activate
