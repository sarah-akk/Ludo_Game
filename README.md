# Ludo Game Algorithm and Implementation Details

## Overview

This Python-based Ludo game simulates the classic board game where up to four players compete to move their pawns from the starting position to the goal. The game incorporates various mechanics such as dice rolling, movement rules, capturing opponent pawns, and win conditions. Additionally, we implement the **Expectiminimax** algorithm to enhance AI decision-making in the game.

## Code Structure

### 1. **Initialization**

The `Game` class initializes:

- Players (`TopLeftPlayer`, `TopRightPlayer`, `BottomRightPlayer`, `BottomLeftPlayer`)
- The game grid (`grid`)
- The dice (`Dice`)
- The current turn and active player
- Displays a welcome message and draws the grid

### 2. **Rolling the Dice**

- The `roll_dice()` function simulates a dice roll using the `Dice` class.
- Returns a random number between 1 and 6.

### 3. **Pawn Movement**

- `move_pawn(pawn_id, current_player, roll_result)`: Moves a pawn based on the dice roll.
- If a pawn is at the **starting corner**, it can enter the board on a roll of 6.
- The function ensures that the pawn follows the player's designated **road cells**.
- If a pawn lands on a cell occupied by an opponent, **capture logic** is triggered.
- If a pawn encounters a **wall (two+ pawns in one cell)**, movement is restricted.

### 4. **Getting Possible Moves**

- `get_possible_moves(current_player, roll_result)`: Determines which pawns can move based on the dice roll.
- Checks if the pawn is:
  - In the starting corner and requires a roll of 6.
  - On the board and able to move without obstacles.
  - Near the end and if it can enter the goal.

### 5. **Valid Move Check**

- `is_valid_move(target_cell_x, target_cell_y, pawn)`: Validates whether a move is possible.
- Ensures the move does not:
  - Pass through a **wall**.
  - Move out of the defined **road cells**.
  - Jump directly to an end cell incorrectly.

### 6. **Capturing Opponent Pawns**

- `capture_opponent_pawns(pawns)`: If a pawn lands on a cell occupied by an opponent, it sends the opponent's pawn back to its start position.
- Captured pawns return to the **corner cell** of their respective players.

### 7. **Turn Handling & Game Flow**

- The `play()` function manages the main game loop:
  - Rolls the dice.
  - Displays the player's possible moves.
  - Validates user input.
  - Moves the selected pawn.
  - Checks for captures.
  - Redraws the grid after each move.
  - Checks for a winning condition (all pawns reached the goal).
  - Allows another turn if the player rolls a 6 but restricts three consecutive 6s.

### 8. **AI Implementation: Expectiminimax Algorithm**

We implement the **Expectiminimax Algorithm** to enhance AI decision-making. This algorithm is used when AI-controlled players make their moves. It works as follows:

- **Chance nodes** calculate the expected value of all possible dice rolls.
- **Decision nodes** select the best move based on the highest (or lowest) evaluation score.
- The algorithm evaluates all legal moves and simulates multiple turns ahead to determine the best possible action for the AI.
- The AI chooses moves that maximize its advantage while considering possible randomness from dice rolls.

This makes AI players more strategic and adaptive, improving the single-player experience! 🤖🎲

### 9. **Sound and Visuals**

- `pygame.mixer.Sound("sounds/click.mp3").play()` triggers a sound effect when a player selects a move.
- The `grid.draw()` function visually updates the board state after each turn.

## Running the Game

To start the game, navigate to the `src` directory and run the following command in the terminal:

```bash
cd src
python main.py
```

## Winning Condition

- A player wins when all their pawns reach the final goal.
- The game announces the winner and terminates.


This implementation captures the essence of Ludo while introducing strategic AI elements like capture mechanics, movement validation, and **expectiminimax-based decision-making**. Have fun playing! 🎲😃

