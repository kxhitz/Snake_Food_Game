# Snake_Food_Game

This project is a classic Snake Game built using Python's Turtle graphics library. The game involves navigating a snake to eat food, growing longer each time it eats, while avoiding collisions with the walls and itself.

## Features

- Classic Snake gameplay with continuous movement.
- Automatic screen updates for smooth gameplay.
- Snake grows longer each time it eats food.
- Border boundary detection and teleportation.
- Score tracking with the highest score retention.
- Simple and intuitive controls.

## Requirements

- Python 3.x
- Turtle graphics library (included with Python's standard library)

## Installation

1. Ensure you have Python 3.x installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).
2. Clone this repository or download the source code files.

git clone https://github.com/your-username/snake-game.git
cd snake-game

## Usage

To start the game, navigate to the directory containing the `snake_game.py` file and run the following command:

python snake_game.py

## Game Controls

- **Up Arrow Key**: Move the snake up.
- **Down Arrow Key**: Move the snake down.
- **Left Arrow Key**: Move the snake left.
- **Right Arrow Key**: Move the snake right.
- **Space Bar**: Stop the snake.

## Game Mechanics

- The snake starts at the center of the screen and can move in four directions.
- The objective is to eat the food that appears at random locations on the screen.
- Each time the snake eats food, it grows longer, and the score increases by 10 points.
- The game ends if the snake collides with its own body.
- If the snake hits the border, it reappears on the opposite side of the screen.
- The game speed increases slightly with each piece of food consumed.

## Customization

- **Screen Setup**: Modify the screen setup parameters to change the background color, screen size, and title.
- **Snake and Food Appearance**: Change the appearance of the snake and food by modifying their shape, color, and size.
- **Game Speed**: Adjust the initial `delay` variable to change the starting speed of the game.
- **Score Display**: Customize the font, size, and position of the score display.

## Acknowledgments

This project was inspired by the classic Snake game, which has been a popular and simple game concept for decades. The implementation utilizes Python's Turtle graphics library for its simplicity and ease of use in creating graphical applications.
