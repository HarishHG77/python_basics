h="harish goudar"
#finding length of string
print(str(len(h)))
l=len(h)
print("length of the given strig="+str(l))
#concatination
g="BCA"
res=h+g
print("concatenated string is="+res)
#string repeatation
x=h*4
print(x)
#slicing
a="bldea college jkd"
print(a[5:])
print(a[:5])
#converting string to uppercase
y=a.upper()
print("string converted to uppercase is "+y)
#converting string to lowercase
z=y.lower()
print("string converted to lowercase:"+z)
#strip
g="              harish"
k=g.strip()
print("after removing unwanted space:"+k)

#index()
pos=a.index('jkd')
print("position of given element is="+str(pos))

#split()
b=("m123","harish","bca","5000")
lst=b.split(',')
fees=int(lst[-1])
print(str(fees))

