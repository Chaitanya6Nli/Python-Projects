# START 
# This function runs the quiz game
def run_quiz(questions):
    score = 0 # Initialize the player's score
    for question in questions:
        print(question["prompt"]) # Print the question
        for option in question["options"]:
            print(option) # Print each answer option

            # Get the player's answer and convert it to uppercase
            answer = input("Enter your answer (A, B, C, D): ").upper()

            # Check if the answer is correct
            if answer == question["answer"]:
                print("Horray!, You're are correct\n")
                score += 1 # Increase score fore correct answer
            else:
                print("Opps!, The correct answer was", question["answer"], "\n")

    # Print the inal score
    print(f"You got {score} out of {len(questions)} questions corect.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the Capital of India?",
        "options": ["A. Mumbai", "B. Bangalore", "C. New Delhi", "D. Lucknow"],
        "answer": "C"
    },
    {
        "prompt": "Which Language is primarily spoken in Maharashtra?",
        "options": ["A. Marathi", "B. Gujarati", "C. Telegu", "D. Bihari"],
        "answer": "A"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Which Planet is known as Red Planet?",
        "options": ["A. Moon", "B. Pluto", "C. Jupiter", "D. Mars"],
        "answer": "D"
    }
]

# Run the quiz
run_quiz(questions)
        



    
