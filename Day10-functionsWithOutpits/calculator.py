def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("enter the first one "))

    for operator in operation:
        print(operator)
    flag = True
    while flag:
        symbolPicked = input("enter the symbol")
        num2 = float(input("enter the another number"))
        function = operation[symbolPicked]
        answer = function(num1, num2)
        print(f"{num1} {symbolPicked} {num2} ={answer}")
        choice = input(
            f"type 'y' to continue with {answer},or type 'n' to exit ,or 'fresh' to start fresh calculation ").lower()

        if choice == "y":
            num1 = answer
        elif choice == "fresh":
            calculator()
        else:
            flag = False


calculator()
