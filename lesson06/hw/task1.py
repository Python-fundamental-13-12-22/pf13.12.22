def arifmetic(a,b,operation):
        if operation=="+":
                return a+b
        elif operation=="-":
                return a-b
        elif operation=="*":
                return a*b
        elif operation=="/":
                return a/b
        else:
                return "Invalid!"
a=int(input("a: "))
b=int(input("b: "))
operation=input("Select a opeation(+;-;*;/): ")
print(f"Result: {arifmetic(a,b,operation)}")