import argparse

def fibn(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help = "The fibonacci number you want to find.", type = int)
    
    args = parser.parse_args()
    result = fibn(args.num)
    
    print("The " + str(args.num) + "th number is " + str(result))
    
if __name__ == '__main__':
    Main()
    
    