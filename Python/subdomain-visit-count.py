# https://leetcode.com/problems/subdomain-visit-count/


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = {}
        for x in cpdomains:
            count, cpdomain = x.split()
            if cpdomain not in counts: counts[cpdomain] = 0
            counts[cpdomain] += int(count)

            for i in range(len(cpdomain)):
                if cpdomain[i] == '.':
                    subdomain = cpdomain[i + 1:]
                    if subdomain not in counts: counts[subdomain] = 0
                    counts[subdomain] += int(count)

        return ['%s %s' % (v, k) for k, v in counts.items()]
