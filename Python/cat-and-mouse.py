# https://leetcode.com/problems/cat-and-mouse/description/


class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        mem = {}

        optimal_strategy = self.mouse_move(1, 2, mem, graph)
        if optimal_strategy == -1: return 2
        return optimal_strategy

    def mouse_move(self, mouse, cat, mem, graph):
        state = (mouse, cat, 1)

        if state in mem:
            return mem[state]

        if 0 in graph[mouse]:
            mem[state] = 1
            return 1

        mem[state] = 0

        maximized = -1
        for move in graph[mouse]:
            if move == cat:
                continue

            maximized = max(maximized, self.cat_move(move, cat, mem, graph))

            if maximized == 1:
                mem[state] = 1
                return 1

        mem[state] = maximized
        return maximized

    def cat_move(self, mouse, cat, mem, graph):
        state = (mouse, cat, 0)

        if state in mem:
            return mem[state]

        if mouse in graph[cat]:
            mem[state] = -1
            return -1

        mem[state] = 0

        minimized = 1
        for move in graph[cat]:
            if move == 0:
                continue

            minimized = min(minimized, self.mouse_move(mouse, move, mem, graph))

            if minimized == -1:
                mem[state] = -1
                return -1

        mem[state] = minimized
        return minimized
