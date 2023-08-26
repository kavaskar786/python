
#zero division error
try:
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    c=a/b
    print(c)
except ZeroDivisionError as error:
    print(error)


#used the finally and raise keyword in this
try:
    arr1=["kavaskar","mca",1,2]
    print(arr1[4])
    print(arr1[3])
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    if(b==0):
        raise ZeroDivisionError("ZeroDivisionError")
    else:
        print(a/b)
except IndexError as e:
        print(e)
finally:
    print("The code ran successfully")


#
import re
def func1(text):
    pattern1=r'[(?][0-9]{3}[)?]\-[0-9]{3}\-[0-9]{4}'
    pattern2=r'[0-9]{3}\-[0-9]{3}\-[0-9]{4}'
    match1=re.search(pattern1,text)
    match2=re.search(pattern2,text)
    if match1 or match2:
        print("Valid phn number")
    else:
        print("Invalid phn number")
text=str(input("Enter the string"))
func1(text)


import re
def func1(text):
    pattern2=r'[A-Z]+'
    pattern3=r'[a-z]+'
    pattern4=r'[0-9]+'
    pattern5=r'[@ - / , .]+'
    match2=re.search(pattern2,text)
    match3=re.search(pattern3,text)
    match4=re.search(pattern4,text)
    match5=re.search(pattern5,text)
    if match2 and match3 and match4 and match5:
        print("Password Set Successfully")
    else:
        print("Set a Valid Password")
text=str(input("Enter the string"))
func1(text)