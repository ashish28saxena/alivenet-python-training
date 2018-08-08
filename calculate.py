def add(x, y):
   return x + y
   
def subtract(first, secand):  
	return first - secand
	
def multiply(first,secand):
   return first * secand
 
def  divide(first,secand):
    return first / secand
   
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

first=input("Please Enter First Number: ")
secand=input("Please Enter Secand Number: ")
operater=input("Please Enter Operater: ")

if operater==1 :
    print(first,"+",secand,"=", first + secand)
   
elif operater==2 :   
   print(first,"-",secand,"=", subtract(first,secand))
elif operater==3 :
   print(first,"*",secand,"=", multiply(first,secand))
elif operater==4 :
    print(first,"/",secand,"=", divide(first,secand))
else :
   print "Invalid Argument"   

