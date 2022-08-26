while True:
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    try:
        result= a/b
        print(result)
    except:
        print("number is not divisible by zero,please enter another number")


