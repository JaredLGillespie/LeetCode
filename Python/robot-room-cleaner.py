# https://leetcode.com/problems/robot-room-cleaner/


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#     def move(self):
#         """
#         Returns true if the cell in front is open and robot moves into the cell.
#         Returns false if the cell in front is blocked and robot stays in the current cell.
#         :rtype bool
#         """
#
#     def turnLeft(self):
#         """
#         Robot will stay in the same cell after calling turnLeft/turnRight.
#         Each turn will be 90 degrees.
#         :rtype void
#         """
#
#     def turnRight(self):
#         """
#         Robot will stay in the same cell after calling turnLeft/turnRight.
#         Each turn will be 90 degrees.
#         :rtype void
#         """
#
#     def clean(self):
#         """
#         Clean the current cell.
#         :rtype void
#         """


class Solution(object):
    def face_direction(self, robot, current_dir, desired_dir):
        if current_dir == desired_dir: return current_dir
        if (current_dir - 1) % 4 == desired_dir:
            robot.turnLeft()
            return desired_dir

        while current_dir != desired_dir:
            robot.turnRight()
            current_dir = (current_dir + 1) % 4
        return current_dir

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # dir: 0 -> up, 1 -> right, 2 -> down, 3 -> left
        row, col, dir = 0, 0, 0
        visited = {(0, 0): None}
        robot.clean()

        while True:
            if (row - 1, col) not in visited:
                dir = self.face_direction(robot, dir, 0)
                visited[(row - 1, col)] = (row, col)
                if robot.move():
                    robot.clean()
                    row -= 1
            elif (row, col + 1) not in visited:
                dir = self.face_direction(robot, dir, 1)
                visited[(row, col + 1)] = (row, col)
                if robot.move():
                    robot.clean()
                    col += 1
            elif (row + 1, col) not in visited:
                dir = self.face_direction(robot, dir, 2)
                visited[(row + 1, col)] = (row, col)
                if robot.move():
                    robot.clean()
                    row += 1
            elif (row, col - 1) not in visited:
                dir = self.face_direction(robot, dir, 3)
                visited[(row, col - 1)] = (row, col)
                if robot.move():
                    robot.clean()
                    col -= 1
            elif (row, col) == (0, 0): break
            else:
                prow, pcol = row, col
                row, col = visited[(row, col)]
                if (row, col) == (prow - 1, pcol):
                    dir = self.face_direction(robot, dir, 0)
                    robot.move()
                elif (row, col) == (prow, pcol + 1):
                    dir = self.face_direction(robot, dir, 1)
                    robot.move()
                elif (row, col) == (prow + 1, pcol):
                    dir = self.face_direction(robot, dir, 2)
                    robot.move()
                else:
                    dir = self.face_direction(robot, dir, 3)
                    robot.move()
