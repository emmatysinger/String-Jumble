"""
stringjumble.py
Author: Emma Tysinger
Credit: https://dbader.org/blog/python-reverse-list, https://docs.python.org/3/library/stdtypes.html, https://www.quora.com/In-Python-how-do-you-convert-a-list-to-a-string

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
s=input("Please enter a string of text (the bigger the better): ")
print('You entered "{0}". Now jumble it:'.format(s))

mylist=list(s)
reversed=mylist[::-1]
for i in reversed: #all letters reversed
    print(i,end="")
print("")

words=s.split(" ") #list of words
reversedwords=words[::-1]

for i in reversedwords: #words reversed
    print(i+" ",end="")
print("")

w=[]
for i in words: #reversed letters only
    words1=list(i)
    words1=words1[::-1]
    words2="".join(words1)
    w.append(words2)
w=" ".join(w)
print(w)
