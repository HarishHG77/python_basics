y=input('enter mobile number')
x=int(y)
if(len(x)>10):
    raise ValueError()
except ValueError:
    print("valid mobile number")