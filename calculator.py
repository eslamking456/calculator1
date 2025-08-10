print("welcome to calculator")
print("""operations:
      +
      -
      *
      /
       """)
while True:
    num1 = float(input("enter the first number : "))
    op = input("enter operation type : ")
    num2 = float(input("enter the second number : "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:

        print("error")
    re = input("do you want to perform another operation (y/n): ")
    if re == "n":
        break
print("see you soon")