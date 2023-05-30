num1 = input("Enter the 1st number: ")
calcu = input("+, -, * or /")
num2 = input("Enter the 2nd number: ")

if calcu == "+":
    result = (float(num1) + float(num2))
elif calcu == "-":
    result =  (float(num1) - float(num2))
elif calcu == "*":
    result =  (float(num1) * float(num2))
elif calcu == "/":
    result =  (float(num1) / float(num2))
else:
    print ("INVALID INPUT - Please enter proper number")
    result = None # none means no value whereas false means its wrong
if result != None: # used != instead of is not
    print (result)
