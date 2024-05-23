# Question : https://leetcode.com/problems/longest-substring-without-repeating-characters



# the first way i was trying to solve it was really awful :)) but its kind of solving for first try ..

#first way 
# class Solution:
#   def generate_substring(self, s):

#         substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
#         return substrings

#   def check_duplicate(self, s):
#         seen = set()  # Use a set to efficiently track unique characters seen so far
#         for char in s:
#             if char in seen:
#                 return True
#             seen.add(char)
#         return False

#   def lengthOfLongestSubstring(self, s):
#         lst_s = []
#         for i in self.generate_substring(s):
#             if not self.check_duplicate(i):
#                 lst_s.append(i)
#         return len(max(lst_s, key=len)) if lst_s else 0


# this way not accepted because of Memory Limit Exceeded ...............
#----------------------------------------------------------------------------------------------------

# the scond way is using set 
"""
In this method, we have a string in hand and I am going to display the maximum size of the sequence in the output. 
Well, we assume that the first letter is a left and right point and enter the same letter into the set. 
The size of the largest string is obtained by { (right index - left index) + 1}.
 Now the next word is correct, if it is new, the previous steps will be followed. 
 If we reach a repeated letter in the movement of the right option, the previous letter will be deleted and the left one will come forward.
Now the new word enters the set.

example : 
abcabcbb  max -> 0-0 + 1 = 1  \ set {a}
L
R
abcabcbb   max - > 1-0 + 1 = 2 \ set {a,b}
LR
abcabcbb   max -> 2-0 +1 = 3
L R
abcabcbb  # previous a was deleted  max -> 3 - 1 +1 = 3  \ set {b,c,a}
 L R
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            L = 0
            max_char = 0
            char = set()

            for R in range(len(s)) :
                while s[R] in char :
                    char.remove(s[L])
                    L +=1

                char.add(s[R])
                max_char = max(max_char , R - L + 1 )
            return max_char
    
# we can do it with Hash map as well 
