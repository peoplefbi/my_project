import prompt


def run_game(game_name, get_question_and_answer, description):
    print(f"Welcome to the {game_name}!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    rounds_count = 3

    for _ in range(rounds_count):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

