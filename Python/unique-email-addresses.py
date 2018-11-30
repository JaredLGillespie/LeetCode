# https://leetcode.com/problems/unique-email-addresses/


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def create_unique_email(email):
            local, domain = email.split('@')
            built_local = []
            for c in local:
                if c == '.': continue
                if c == '+': break
                built_local.append(c)
            return ''.join(built_local) + domain

        unique_emails = set()
        for email in emails:
            unique_emails.add(create_unique_email(email))

        return len(unique_emails)
