import random
import operator

DESCRIPTION = "Calculate the result of the expression."


def get_question_and_answer():
    a = random.randint(1, 50)
    b = random.randint(1, 50)

    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    op = random.choice(list(operations))
    question = f"{a} {op} {b}"
    correct_answer = str(operations[op](a, b))
    return question, correct_answer
