#isalpha()--used to check entered string has only alphabets or not
x=input("enter your name :")
if(x.isalpha()):
    print("valid name")
else:
    print("entered string has no alphabets")

#checking whether entered string has digits or not
y=input("enter your phome number :")
if(y.isdigit()):
    print("valid entry")
else:
    print("not valid entry")

#isalnum()
z=input("enter your password :")
if(z.isalnum()):
    print("valid entry")
else:
    print("not valid entry")

#startswith()
g=input("enter your college name")
if(g.startswith("bldea")):
    print("valid entry")
else:
    print("not valid entry")

#eendswith()
k=input("enter your college name")
if(k.endswith("jkd")):
    print("valid entry")
else:
    print("not valid entry")

