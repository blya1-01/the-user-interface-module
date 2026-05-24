def get_numbers():
    print("\n--- КАЛЬКУЛЯТОР ---")
    a = float(input("Первое число: "))
    op = input("Операция (+, -, *, /): ")
    b = float(input("Второе число: "))
    return a, b, op

def show_result(a, b, op, result):
    print(f"\nРезультат: {a} {op} {b} = {result}")

def show_history(history):
    print("\nИстория")
    if not history:
        print("История пуста")
    else:
        for line in history:
            print(line)
    print("----------------")