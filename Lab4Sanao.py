questions = {

    "What is the largest mammal in the world?": "Blue Whale",
    "Which planet is known as the \"Blue Planet\"?": "Earth",
    "What is the current highest bill currency in the country?": "One Thousand Pesos",
    "Who is the father of the Filipino language?": "Manuel Quezon",
    "What is the highest mountain in the Philippines?": "Mount Apo"
}

attempts = 0
question_num = 0
score = 0

for question, answer in questions.items():
    attempts = 3

    while attempts > 0:
        print("---------------------------------------------")
        user_answer = input(f"{question} (Attempts: {attempts}): ")

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
            break
        else:
            attempts -= 1
            print("Incorrect!")

        if attempts == 0:
            print(f"The correct answer was: {answer}")

print(f"\nFinal Score: {score}/{len(questions)}")
