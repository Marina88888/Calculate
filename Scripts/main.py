from Scripts import calculate


def main():
    while(True):
        user_input = input("Введите строку: ")
        try:
            process_input(user_input)
        except Exception as e:
            print(f"{e}")


def process_input(user_input):
        operator = calculate.find_operator(user_input)
        operand_a, operand_b = calculate.init_operands(user_input, operator)
        print(calculate.calculate(operator, operand_a, operand_b))


main()


