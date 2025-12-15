import random

DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = [start + i * step for i in range(length)]
    hidden_pos = random.randrange(length)
    correct_answer = str(progression[hidden_pos])
    progression[hidden_pos] = ".."

    question = " ".join(str(x) for x in progression)
    return question, correct_answer
