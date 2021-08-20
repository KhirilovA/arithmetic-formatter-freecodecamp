import string


def arithmetic_arranger(problems, display_results=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    allowed_operators = ['+', '-']
    space = ' '
    dash = '-'
    first_line = ''
    second_line = '\n'
    dashes_line = '\n'
    results_line = '\n'
    
    for problem in problems:
        problem_operator = problem.split()[1]
        if problem_operator not in allowed_operators:
            return "Error: Operator must be '+' or '-'."
        
        first_operand, second_operand = problem.split()[0], problem.split()[2]
        if any(e not in string.digits for e in first_operand) or any(
               e not in string.digits for e in second_operand):
            return "Error: Numbers must only contain digits."
        
        first_operand_len = len(first_operand)
        second_operand_len = len(second_operand)
        if first_operand_len > 4 or second_operand_len > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if problem_operator == "+":
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))
        
        # arranging lines
        result_lenght = len(result)
        if result_lenght > 4 or int(result) < 0:
            results_line += space
        else:
            results_line += space*2
        second_line += problem_operator + space
        first_line += space * 2
        dashes_line += dash * 2

        # We get the longest operand and fit everything under it
        if (first_operand_len >= second_operand_len) and (
                first_operand_len >= result_lenght):
            first_line += first_operand
            second_line += space * (first_operand_len - second_operand_len) + second_operand
            dashes_line += dash * first_operand_len
            results_line += space * (first_operand_len - result_lenght) + result
        else:
            first_line += space * (second_operand_len - first_operand_len) + first_operand
            second_line += second_operand
            dashes_line += dash * second_operand_len
            results_line += space * (second_operand_len - result_lenght) + result
        first_line += 4 * space
        second_line += 4 * space
        dashes_line += 4 * space
        results_line += 4 * space

    arranged_problems = first_line[:-4] + second_line[:-4] + dashes_line[:-4]
    if display_results == True:
        arranged_problems += results_line[:-4]

    return arranged_problems