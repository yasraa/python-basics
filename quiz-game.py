quiz_set = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What is the tallest mountain in the world?", "Mount Everest"),
]
score = 0
missed = 0
for index, (question, answer) in enumerate(quiz_set, start=1):
    user_answer = input(question + " ")
    if user_answer == answer:
        print(f"{index} question Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}")
        missed += 1
print(f"Your final score is: {score}/{len(quiz_set)} you got {missed} questions wrong")
