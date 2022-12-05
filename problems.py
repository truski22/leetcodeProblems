
class solution:
    #problema leetcode 13. Roman to integer (easy)
    def romanToInt(self,s):
        if len(s)==0:
            return
        numeros={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i,j=0,1
        solution=0
        while j<len(s):
            if numeros[s[i]] < numeros[s[j]]:
                solution += (-1)*numeros[s[i]]
            else:
                solution += numeros[s[i]]
            i,j = j,j+1
        solution+=numeros[s[i]]
        return solution

    #problema 14 leetcode Longest Common Prefix
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #["flower","flow","flight"]
        sol=""
       #TO-DO
        for n in strs:
            print(n)

            

            



#input = input()
s = solution()
# print(s.romanToInt(input))
s.longestCommonPrefix(["flower","flow","flight"])