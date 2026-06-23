import rclpy
from rclpy.node import Node

def main():
    rclpy.init()

    node = Node("panda_move")

    print("Robot starting move...")

    # fake Point A → B demo (MoveIt add later)
    print("Reached Point A")
    print("Moving to Point B")
    print("Reached Point B")

    rclpy.shutdown()

if __name__ == "__main__":
    main()
