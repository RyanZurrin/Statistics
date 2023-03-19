# pthon clas for testing regular expressions to different languages, use BNF format


import re


# define the regular expression
regex = re.compile('(0|1)(0|1)*')
print(f'mathching the regular expression: {regex}')
# test the regular expression
print(f"language 0 : {regex.match('0')}")
print(f"language 1 : {regex.match('1')}")
print(f"language 10 : {regex.match('10')}")
print(f"language 11 : {regex.match('11')}")
print(f"language 100 : {regex.match('100')}")
print(f"language 101 : {regex.match('101')}")
print(f"language 110 : {regex.match('110')}")
print(f"language 111 : {regex.match('111')}")
print(f"language 1000 : {regex.match('1000')}")
print(f"language 1001 : {regex.match('1001')}")
print(f"language 1010 : {regex.match('1010')}")
print(f"language 01011 : {regex.match('01011')}")
print(f"language 0001111 : {regex.match('0001111')}")
print(f"language 011111 : {regex.match('011111')}")
print(f"language 110000011101 : {regex.match('110000011101')}")
print(f"language 000001100000111011 : {regex.match('000001100000111011')}")
