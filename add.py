def add(num1, num2): 
    return num1 + num2 

select = int(input("Select Operations:"))
number_one = int(input("Enter the First Number"))
number_two = int(input("Enter the second Number"))
if (select == 1):
    print(number_one,"+",number_two,"=",add(number_one,number_two))
    
else:
    print("Wrong input..!!");

       


