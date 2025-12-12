
from src.calc import *

def main():
    
    print("Basic Arithmetic Operations")
    cmd=input('Type y for continue calculation...')  
    if cmd !='y':
        print("please type 'y' for proceeding calculation...") 
    

    else:
        print("operations are :'add' 'sub' 'mul' 'div' 'square'")
        print("Type exit for close the operations")
        print("Please provide operations to perform followed with two numbers. Example: add 5 3")
    
    if cmd=="y":
        yes(cmd)

if __name__ == "__main__":
    main()