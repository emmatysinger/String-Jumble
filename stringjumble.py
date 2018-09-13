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
s=input("Please enter a string of text (the bigger the better):")
print("You entered '{0}'. Now jumble it:".format(s))
mylist=list(s)
characters=int(len(mylist))
newlist=mylist[::-1]
for i in newlist:
    print(i,end="")
print("")
list2=s.split()
newlist2=list2[::-1]
wordcount=len(list2)
wordcount=range(0,wordcount)
for i in newlist2:
    print(i+" ",end="")
print("")
for i in wordcount:
    str="".join(list2[i])
    newlist3=list(str)
    newlist3=newlist3[::-1]
    str2="".join(newlist3)
    print(str2+" ",end="")
print("")
