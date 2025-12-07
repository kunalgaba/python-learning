expression = input("Expression: ")
x, y, z = expression.split(" ")
match y:
    case "+":
        result = int(x) + int(z)
    case "-":
        result = int(x) - int(z)
    case "*":
        result = int(x) * int(z)
    case "/":
        result = int(x) / int(z)
print(round(float(result), 1))
