# ROS2 Panda MoveIt2 - 6DOF Robotic Arm Motion Planning

 Project Overview

This project demonstrates a 6-axis robotic arm simulation using ROS2 Humble and MoveIt2. The main goal is to move a robotic arm from Point A to Point B while ensuring a collision-free path in a simulated environment.

The system uses inverse kinematics for calculating joint configurations and MoveIt2 for motion planning and execution in RViz2.

 #Objectives

- Simulate a 6-DOF Panda robotic arm  
- Implement motion planning using MoveIt2  
- Generate collision-free trajectories  
- Execute Point A → Point B movement  
- Apply inverse kinematics for joint calculation  
- Visualize robot motion in RViz2
- 
 #Technologies Used

- ROS2 Humble  
- MoveIt2  
- RViz2  
- Python (rclpy)  
- Panda Robot Model 

 #Features

- 6-axis robotic arm simulation  
- Inverse Kinematics via MoveIt2 planning pipeline  
- Motion planning and execution  
- Collision-free trajectory generation  
- Real-time visualization in RViz2  
- Joint state monitoring and control  

# Workflow

1. Launch Panda robot in MoveIt2 RViz environment  
2. Set start position (Point A)  
3. Set goal position (Point B)  
4. Generate motion plan using MoveIt2  
5. Execute trajectory using ROS2 controller  
6. Robot moves smoothly along a collision-free path  

# Project Structure
panda_move/
├── panda_move/
│ ├── move_panda.py
│ └── init.py
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
└── test/

# Key Learning Outcomes

- Robotics kinematics (Forward & Inverse)  
- Motion planning and trajectory generation  
- ROS2 package structure and workflow  
- MoveIt2 planning and execution pipeline  
- Real-time robotic simulation in RViz2  

Author

**Ezza Javed**  
GitHub: https://github.com/ezzen167  

