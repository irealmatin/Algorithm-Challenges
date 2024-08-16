# Qestion : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dict_digit = {
                      '2':['a' , 'b' , 'c'] , 
                      '3':['d','e','f'] ,
                      '4':['g','h','i'] , 
                      '5':['j' , 'k' , 'l'] ,
                      '6':['m','n','o'] , 
                      '7':['p','q' , 'r' , 's'],
                      '8':['t' ,'u', 'v' ],
                      '9':['w' , 'x' , 'y' , 'z']
                      }
        #base case
        if not digits :
            return []
        

        self.res_lst = []
        self.combination(digits,0,[])
        return self.res_lst
    
    def combination(self , digits ,indx , currStr):
        if indx >= len(digits):
            self.res_lst.append("".join(currStr))
            return
        
        else:
            for char in self.dict_digit[digits[indx]] :
                currStr.append(char)
                self.combination(digits , indx+1 , currStr)
                currStr.pop()




"""
note :
1 - using backtracking 
2 - time :  worst case is when we apply 7 & 9 -> 77777... so it costs (4**n)  * (n:for n time join )
"""