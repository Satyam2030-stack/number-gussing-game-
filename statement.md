# Problem Statement: Number Guessing Game

## Problem Statement
Users often seek simple, interactive desktop applications to practice logic and engagement. The goal of this project is to build a command-line based interactive Python application where the computer selects a random secret number, and the user must guess it within a limited number of attempts.

## Scope of the Project
- Generate a pseudo-random integer between a defined range (1 to 50).
- Provide continuous feedback to the user on whether their guess is "Too High" or "Too Low".
- Track total attempts and display remaining chances dynamically.
- Handle invalid non-integer inputs gracefully using exception handling without crashing the game.
- Terminate safely upon winning or after completing all attempts till end.

## Target Users (like who can use this game easily)
- Students and beginners learning Python command-line interfaces.
- Anyone looking for a lightweight, quick interactive game.

## High level features used in th game 
1. **Random Secret Number Generation:** Uses Python's built-in `random` module.
2. **Attempt Counter:** Restricts the user to 6 attempts.
3. **Input Validation:** Prevents program termination on invalid text inputs using `try-except`.
4. **Dynamic Feedback & Timers:** Uses formatted strings (`f-strings`) and `time.sleep()` delays for realistic output pacing.
5. **System Exit Handling:** Uses `sys.exit()` for a clean shutdown upon winning.