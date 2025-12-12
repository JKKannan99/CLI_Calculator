def yes(cmd):
    import math
    while cmd=='y':

            user_input=input("Calc> ").lower().strip().split() 
      
            command=user_input[0]
            if command not in ["add", "sub", "mul", "div","square","sqrt","log", "sin","cos","tan","exit"]:
                print("Enter valuable operators like 'add' 'sub' 'mul' 'div' 'squre' 'log' ")
                quit()

            if command == "exit" :
                print("calculator closed... Thanks for using!")
                break
            
            num1 = user_input[1]
           
            if command=='square':
                num1=float(user_input[1])                
                print('Square Result:',num1*num1)
            
            elif command=='log':
                num1=float(user_input[1])                
                print('log Result:',math.log(num1))
            
            elif command=='sqrt':
                num1=float(user_input[1])                
                print('sqrt Result:',math.sqrt(num1))
            
            elif command=='sin':
                num1=float(user_input[1])                
                print('sin Result:',math.sin(num1))
                
            elif command=='cos':
                num1=float(user_input[1])                
                print('cos Result:',math.cos(num1))

            elif command=='tan':
                num1=float(user_input[1])                
                print('tan Result:',math.tan(num1))

            else:
                num2 = user_input[2]
                calculator(command,num1,num2)
            


def calculator(command,num1,num2):
 
    x=float(num1)
    y=float(num2)

    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y
    def div(x,y):
        return x/y

    if command=='add':
        print("Addition Result:",add(x,y))
    elif command=='sub':
        return("Subtraction Result:",sub(x,y))
    elif command=='mul':
        print("Multiplication Result:",mul(x,y))
    elif command=='div':
        if y==0:
            print('cannot divided by zero')
        else:
            print("Division Result:",div(x,y))
  
    else:
        print("unknown command")
=======
# def calculator(command,num1,num2):
 
#     x=float(num1)
#     y=float(num2)

#     if command=='add':
#         print("Addition Result:",x + y)
#     elif command=='sub':
#         print("Subtraction Result:",x - y)
#     elif command=='mul':
#         print("Multiplication Result:",x * y)
#     elif command=='div':
#         if y==0:
#             print('cannot divided by zero')
#         else:
#             print("Division Result:",x / y)
    
#     else:
#         print("unknown command")

#*************************************************************************************************************


