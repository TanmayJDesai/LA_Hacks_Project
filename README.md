## Shortest Path Finder for College Campuses
# Introduction
Welcome to the Shortest Path Finder for College Campuses! This project provides a visualizer for finding the shortest path between two points on a grid, particularly designed for college campuses. New students can use this tool to navigate their way through the campus more efficiently.

# Requirements
Before using the visualizer, ensure that you have the required libraries installed. In your IDE's terminal, type the following commands:

```bash 
pip3 install pygame
pip3 install numpy
pip3 install pygcurse
```
# How to Use
* Launch the Program:
  * Run the program and watch as the grid unfolds in a visually appealing pygame interface.

* Select Your Starting Point:
  * Left-click and right-click at the same time to mark your starting point on the grid.

* Choose Your Destination:
  * Repeat the same left-click and right-click combo to set your destination. It can be the same point for a unique experience!

* Create Barriers:
  * Left-click, hold, and drag to draw barriers that represent buildings or obstacles on your campus.

* Initiate Pathfinding:
  * Press the enter key to let the magic happen. The Shortest Path algorithm will weave through the grid and find the most efficient route between your chosen points.

* Rediscover the Path:
  * Want to see the same path again? Just press any key to reset and visualize the path once more.

## Screenshots

<img width="586" alt="Screenshot 2023-04-23 at 12 15 25 PM" src="https://user-images.githubusercontent.com/65262891/233860231-813c8fc8-b608-401a-a8bf-501c89f90c1d.png">
<img width="589" alt="Screenshot 2023-04-23 at 9 53 06 AM" src="https://user-images.githubusercontent.com/65262891/233860249-36d3907a-d8f0-486f-8fb3-1c17f7ce7421.png">

## Code Structure
# BFS.py
This file contains the breadth-first search (BFS) algorithm for finding the shortest path. It uses a grid-based approach and pygame for visualization. The FIND_SHORTEST_PATH function takes care of exploring the grid to find the shortest path between two points.

# DrawBase.py
This file handles the drawing of the grid using pygcurse and provides the user interface for selecting points and creating barriers. The Final_Grid function initializes the grid and sets up the interface, while the Draw_The_Grid function is responsible for drawing the grid.

