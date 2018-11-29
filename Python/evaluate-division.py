# https://leetcode.com/problems/evaluate-division/


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def search(a, b, v, visited):
            if a not in edges or b not in edges: return -1.0
            if a == b: return v

            for neighbor in edges[a]:
                if neighbor in visited: continue
                visited.add(neighbor)
                r = search(neighbor, b, v * dist[(a, neighbor)], visited)
                if r != float('inf'): return r
            return float('inf')

        edges, dist = {}, {}
        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            if a not in edges:
                edges[a] = set()
            if b not in edges:
                edges[b] = set()
            edges[a].add(b)
            edges[b].add(a)
            dist[(a, b)] = v
            dist[(b, a)] = 1.0 / v

        out = []
        for a, b in queries:
            r = search(a, b, 1, set())
            if r == float('inf'): r = -1
            out.append(r)
        return out
