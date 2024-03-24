def start():
    n1=float(input("ENTER FIRST NUMBER: "))
    n2=float(input("ENTER SECOND NUMBER: "))
    l=["A","M","D","S","R"]
    print("A --> ADDITION")
    print("S --> SUBTRACTION")
    print("M --> MULTIPLICATION")
    print("D --> DIVISSION")
    print("R --> REMENDER")
    def opr():
        op=input("ENTER OPERATION SYMBOL FROM ABOVE LIST:")
        op=op.upper()
        if op in l:
            if op=="A":
                k=n1+n2
                print("RESULT IS:",k)
                loop()
            elif op=="S":
                k=n1-n2
                print("RESULT IS:",k)
                loop()
            elif op=="M":
                k=n1*n2
                print("RESULT IS:",k)
                loop()
            elif op=="D":
                k=n1/n2
                print("RESULT IS:",k)
                loop()
            else:
                k=n1%n2
                print("RESULT IS:",k)
                loop()
        else:
            print("INVALID OPERATION SYMBOL..")
            opr()
                
    opr()
def loop():
    print("Welcome To My Calc")
    print("Y --->start")
    print("E---->Exit")
    s=input("DO YOU WANT TO START CALCULATION.. Y/N")
    s=s.lower()
    if s=="y":
        start()
loop()
