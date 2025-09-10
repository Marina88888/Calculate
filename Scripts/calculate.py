from Scripts import romanSymbols


def find_operands(user_input, operator):
    operands = ""
    for char in user_input:
        if char == operator:
            operands += " "
        else:
            operands += char
    return operands.split()


def find_operator(user_input):
    operator = ""
    for op in user_input:
        if op in "+-*/":
            if operator == "":
                operator = op
            else:
                if len(find_operands(user_input, operator)) > 2:
                    raise ValueError( "формат математической операции не удовлетворяет заданию - два операнда и один оператор")
                else:
                    raise ValueError("формат математической операции не удовлетворяет заданию - должен быть только один оператор")

    if operator == "":
        raise ValueError("строка не является математической операцией")

    return operator


def init_operands(user_input, operator):
    operand_a , operand_b =  find_operands(user_input, operator)[0].replace(" ", ""), find_operands(user_input, operator)[1].replace(" ", "")
    converted_a, converted_b = romanSymbols.translate(operand_a, operand_b)

    try:
        operand_a, operand_b = int(converted_a), int(converted_b)
    except:
        raise ValueError("Калькулятор умеет работать только с целыми числами")
    else:
        if operand_a < 1 or operand_b < 1 or operand_a > 10 or operand_b > 10:
            raise ValueError("Калькулятор может принимать на вход числа от 1 до 10 включительно, не более.")
        else:
            return operand_a, operand_b


def calculate(operator, operand_a, operand_b):
    match operator:
        case '+':
            return operand_a + operand_b
        case '-':
            return operand_a - operand_b
        case '*':
            return operand_a * operand_b
        case '/':
            return operand_a // operand_b
        case _:
            raise ValueError("Неизвестный оператор")

