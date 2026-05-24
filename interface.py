def get_numbers():
    print("\n--- КАЛЬКУЛЯТОР ---")
    a = float(input("Первое число: "))
    op = input("Операция (+, -, *, /): ")
    b = float(input("Второе число: "))
    return a, b, op

def show_result(a, b, op, result):
    print(f"\nРезультат: {a} {op} {b} = {result}\n")
    
def show_history(history):
    print("\n--- ИСТОРИЯ ---")
    if not history:
        print("История пуста")
    else:
        for line in history:
            print(line)
    print("----------------\n")