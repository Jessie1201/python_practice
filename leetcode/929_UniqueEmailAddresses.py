# https://leetcode.com/problems/unique-email-addresses/
# how many different addresses actually receive mails? 

class Solution:
    def numUniqueEmails(self, emails) -> int:
        for i in range(len(emails)):
            emails[i] = emails[i].split('@')
            emails[i][0] = emails[i][0].replace(".", "")
            if '+' in emails[i][0]:
                emails[i][0] = emails[i][0][:emails[i][0].index('+')] 
        uniq = []
        for el in emails:
            if not el in uniq:
                uniq.append(el)
        return len(uniq)
        
        
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"])
    print(param_1)
