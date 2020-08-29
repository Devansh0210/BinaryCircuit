#!/usr/bin/env python
# coding: utf-8

# helper function
def padding(n:int):
    s = ''
    for i in range(n):
        s = s + '0'
    return s

def binaryGen(n:int):
    """
    Generating n digit binary numbers
    
    """    
    binaryNo = [padding(n-len(bin(i)[2:]))+bin(i)[2:] for i in range(2**n)]
    return binaryNo     


def conv_grayCode(inp_s:str):
    """
    Converting binary no to corresponding Gray code (Reflector Code)

    """
    ans = inp_s[0]
    for i in range(1,len(inp_s)):
        ans = ans + str(int((int(inp_s[i]) and not int(inp_s[i-1])) or (int(inp_s[i-1]) and not int(inp_s[i]))))

    # print(ans)
    return ans

def decTobin(n):
    """
    Converting any number from base 10 to binary number i.e. base 2
    ex. decTobin(9) = 1001, decTobin(5) = 0101

    """
    print(bin(n).replace("0b",""))  

def binTodec(s):
    tot = 0
    i = 0
    for k in s[::-1]:
        tot = tot + int(k)*(2**i)
        i = i + 1
        
    print(tot)
    
