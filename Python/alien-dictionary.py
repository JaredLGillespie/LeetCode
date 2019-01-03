# https://leetcode.com/problems/alien-dictionary/


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        order = []
        incoming_edges, outgoing_edges = {}, {}
        no_incoming_edges, remaining = set(), set()

        for i in range(len(words)):
            for c in words[i]:
                if c not in incoming_edges:
                    incoming_edges[c] = set()
                    outgoing_edges[c] = set()
                    no_incoming_edges.add(c)
                    remaining.add(c)

            if i == 0: continue
            l = min(len(words[i]), len(words[i - 1]))

            for j in range(l):
                a, b = words[i - 1][j], words[i][j]
                if a == b: continue
                outgoing_edges[a].add(b)
                incoming_edges[b].add(a)
                if b in no_incoming_edges: no_incoming_edges.remove(b)
                break

        while no_incoming_edges:
            c = no_incoming_edges.pop()
            order.append(c)
            remaining.remove(c)

            for o in outgoing_edges[c]:
                if o not in remaining: continue
                incoming_edges[o].remove(c)
                if not incoming_edges[o]: no_incoming_edges.add(o)

        if remaining: return ''
        return ''.join(order)
