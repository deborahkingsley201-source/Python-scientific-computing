def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts[0], parts[1], parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(num1), len(num2)) + 2
        res = str(int(num1) + int(num2)) if operator == '+' else str(int(num1) - int(num2))

        first_line += num1.rjust(length) + "    "
        second_line += operator + num2.rjust(length - 1) + "    "
        dashes += "-" * length + "    "
        answers += res.rjust(length) + "    "

    result = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip()
    if show_answers:
        result += "\n" + answers.rstrip()
    return result

# Example Execution
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
