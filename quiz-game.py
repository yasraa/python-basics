quiz_set = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What is the tallest mountain in the world?", "Mount Everest"),
]
score = 0
for question, answer in quiz_set:
    user_answer = input(question + " ")
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}")
print(f"Your final score is: {score}/{len(quiz_set)}")
