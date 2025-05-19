history = {'+': [], '-': [], '*': [], '/': []}

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2
    else:
        return "Неизвестная операция"

def print_history():
    for op, ops in history.items():
        print(f"{op} {ops}")

def repl():
    while True:
        try:
            num1 = input("Введите первое число:")
            if num1.lower() == 'exit':
                break
            num1 = float(num1)
            
            num2 = float(input("Введите второе число:"))
            operation = input("Введите операцию:")
            
            result = calculate(num1, num2, operation)
            
            if isinstance(result, str):
                print(result)
            else:
                expression = f"{num1}{operation}{num2}={result}"
                history[operation].append(expression)
                print(expression)
            
            print_history()
        except ValueError:
            print("Ошибка: введите число")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    repl()
