def subtraction(num1,num2):
    return num1-num2



select = int(input("Select Operations:"))
num1 = int(input("Enter the First Number"))
num2 = int(input("Enter the second Number"))
if (select == '1'):
    print(add(num1,num2))
    
else:
    print("Wrong input..!!");
