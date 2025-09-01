import random
import matplotlib.pyplot as plt

# Questions with options and correct answer
quiz = [
    ("What is the capital of France?", ["A) Berlin", "B) Paris", "C) Rome", "D) Madrid"], "B"),
    ("What is 5 + 7?", ["A) 10", "B) 12", "C) 14", "D) 15"], "B"),
    ("Who wrote 'Romeo and Juliet'?", ["A) Dickens", "B) Shakespeare", "C) Tolstoy", "D) Homer"], "B"),
    ("What is the largest planet in our solar system?", ["A) Earth", "B) Saturn", "C) Jupiter", "D) Neptune"], "C"),
    ("Which element has the chemical symbol O?", ["A) Oxygen", "B) Gold", "C) Osmium", "D) Helium"], "A"),
    ("In which year did World War II end?", ["A) 1945", "B) 1939", "C) 1918", "D) 1965"], "A"),
    ("What is the square root of 64?", ["A) 6", "B) 7", "C) 8", "D) 9"], "C"),
    ("Who painted the Mona Lisa?", ["A) Picasso", "B) Van Gogh", "C) Leonardo da Vinci", "D) Michelangelo"], "C"),
    ("What is the national animal of India?", ["A) Elephant", "B) Lion", "C) Peacock", "D) Tiger"], "D"),
    ("What is the boiling point of water in Celsius?", ["A) 0", "B) 50", "C) 100", "D) 150"], "C")
]

# Select 4 random questions
selected = random.sample(quiz, 4)
score = 0

print("🎯 Welcome to the Quiz Game (MCQ Version)!\n")

for i, (q, options, correct) in enumerate(selected, 1):
    print(f"Q{i}: {q}")
    for option in options:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == correct:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {correct}.\n")

# Show final score
print(f"🎉 You got {score} out of 4 correct!")

# Visualization
labels = ["Correct", "Wrong"]
values = [score, 4 - score]

plt.bar(labels, values, color=["green", "red"])
plt.title("Quiz Results")
plt.ylabel("Number of Questions")
plt.show()