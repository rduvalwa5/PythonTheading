'''
Created on Apr 12, 2014

@author: rduvalwa2
'''
import string 
import random

    
def alphaGen(num):
    alphas = ''.join(string.ascii_lowercase)
    ret = []
    for i in range(num):
        ret.append(random.choice(alphas))
    return ret
        
if __name__ == "__main__":
    result = alphaGen(26)
    print(len(result))
    print(result)
#    for item in result:
#        print(item)