# https://leetcode.com/problems/employee-importance/


"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def calc_importance(employee):
            importance = employee.importance
            for sid in employee.subordinates:
                importance += calc_importance(employees[sid])
            return importance

        employees = {e.id: e for e in employees}
        return calc_importance(employees[id])
