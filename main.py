
# from src.calc import *

# def main():
    
#     print("Basic Arithmetic Operations")
#     cmd=input('Type y for continue calculation...')  
#     if cmd !='y':
#         print("please type 'y' for proceeding calculation...") 
    

#     else:
#         print("operations are :'add' 'sub' 'mul' 'div'")
#         print("Type exit for close the operations")
#         print("Please provide operations to perform followed with two numbers. Example: add 5 3")
    
#         while cmd=='y':

#             user_input=input("Calc> ").lower().strip().split()
      
#             command=user_input[0]
#             if command not in ["add", "sub", "mul", "div", "exit"]:
#                 print("Enter valuable operators like 'add' 'sub' 'mul' 'div' ")
#                 quit()

#             if command == "exit" :
#                 print("calculator closed... Thanks for using!")
#                 break
#             try:
#                 num1 = user_input[1]
#                 num2 = user_input[2]
#                 calculator(command,num1,num2)
#             except:

#*************************************************************************************************************************
#                 print("Error: Only numbers are allowed.")
#                 return

# if __name__ == "__main__":
#     main()
