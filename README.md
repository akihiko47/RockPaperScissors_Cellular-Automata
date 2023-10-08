# 🧬 Rock Paper Scissors 🧬

![alt text](https://github.com/akihiko47/RockPaperScissors_Cellular-Automata/blob/main/banner.jpg?raw=true)

In this simulation, every pixel is a cell. In the likes of John Conway's Game of Life, at each simulation step, every cell decides its next color based on its neighbors' colors. Unlike Conway's game, though, there are three states (or colors) instead of just "dead" or "alive". Here's where the rock paper scissors analogy comes into play. Whenever a cell of a certain category is confronted with another of a different category, it will either "eat" or be "eaten" by the other. The rules are:
- C eats B
- B eats A
- A eats C

## Settings ⚙️
1. `matrix_size = 100` - size of cells field (n x n)
2. `cube_size = 10` - size of one cell (in pixels)
3. `rand = True` - add some randomization (makes game more organic)
4. `rand_cof = 1` - how random is mode above
5. `near_win_count = 2` - how many cells need to eat another cell

## Controls 🎮
1. draw - mouse
2. change pen color - 1 / 2 / 3
3. start - space
4. color scheme - left arrow / right arrow
5. intensity - up arrow / down arrow
6. max FPS - minus / plus
7. restart - escape

You can also find controls in `controls.txt`

## Contributions
Contributions are welcomed! 👋
