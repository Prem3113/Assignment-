class Solution:
    def countAndSay (self, n:int)->str:
        if n == 1:
            return "1" 
        if n== 2:
            return "11" 
        Str = "11" 
        for i in range (2, n):
            newString = ""
            count = 1 
            for j in range (len (Str)):
                if j== len (Str) - 1:
                   newString = newString + str (count) + Str[j] 
                   break
	            if Str[j] == Str[j+1]:
	                count += 1
	            else:
	                newString = newString + str (count) + Str[j]
	                count = 1 
	        Str = newString 
	   return newString
