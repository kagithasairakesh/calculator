def multiply(num1, num2): 
    return num1 * num2 
 
 
select = input("Select operations form 1, 2, 3, 4 :") 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 

if select == '1': 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
else: 
    print("Invalid input") 