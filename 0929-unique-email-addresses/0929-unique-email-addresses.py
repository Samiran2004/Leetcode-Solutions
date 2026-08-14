class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniEmails = set()
        for email in emails:
            local, domain = email.split('@')

            local = local.split('+')[0]

            local = local.replace('.', '')

            uniEmails.add(local + '@' + domain)
        
        return len(uniEmails)