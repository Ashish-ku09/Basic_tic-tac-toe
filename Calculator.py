#Basic Calculator (with Loop and Error Handling)

print("===== Welcome to Basic Calculator =====")
print("Type 'exit' anytime to stop the calculator.\n")

while True:
    #Take user inputs
    num1 = input("Enter first number: ")
    if num1.lower() == "exit":
        print("👋 Exiting Calculator... Goodbye!")
        break

    num2 = input("Enter second number: ")
    if num2.lower() == "exit":
        print("👋 Exiting Calculator... Goodbye!")
        break

    operator = input("Enter operator (+, -, *, /, %): ")
    if operator.lower() == "exit":
        print("👋 Exiting Calculator... Goodbye!")
        break

    #Validate numeric inputs
    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        print("❌ Invalid input! Please enter numeric values only.\n")
        continue

    #Convert to float
    num1 = float(num1)
    num2 = float(num2)

    #Perform operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("❌ Division by zero is not allowed.\n")
            continue
        result = num1 / num2
    elif operator == '%':
        if num2 == 0:
            print("❌ Modulo by zero is not allowed.\n")
            continue
        result = num1 % num2
    else:
        print("❌ Invalid operator! Please choose +, -, *, /, or %.\n")
        continue

    #Display result
    print(f"✅ Result: {num1} {operator} {num2} = {result}\n")
