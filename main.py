# Introductory Comments
# This program generates a quiz for U.S. state capitals.
# The user is presented with a state and four capital options, one of which is correct.
# The user must choose the correct capital or quit the quiz.

import random

# Assign database by setting tuple CapitolsAndState
# Example data structure: a dictionary with states as keys and capitals as values
capitals_and_states = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}
# Initialize counters for correct and wrong answers
correct = 0
wrong = 0

# Start the quiz loop, max 100 questions
for question_num in range(100):  # Adjust the range as needed
    # Randomly select a state and its associated capital
    state, correct_capital = random.choice(list(capitals_and_states.items()))

    # Randomly select 3 more capitals which will be “incorrect answers”
    incorrect_capitals = random.sample([
        capital for capital in capitals_and_states.values()
        if capital != correct_capital
    ], 3)

    # Combine correct and incorrect answers
    options = incorrect_capitals + [correct_capital]
    random.shuffle(options)  # Randomize the order of options

    # Assign to CapitalA, CapitalB, CapitalC, CapitalD
    CapitalA, CapitalB, CapitalC, CapitalD = options

    # Display question and options to the user
    print(
        f"\nQuestion {question_num + 1}: What is the capital of {state}? Or (Q)uit"
    )
    print(f"A) {CapitalA}")
    print(f"B) {CapitalB}")
    print(f"C) {CapitalC}")
    print(f"D) {CapitalD}")

    # Wait for user input
    user_input = input("Your answer (A/B/C/D/Q): ").strip().upper()

    # Check if the user wants to quit
    if user_input == 'Q':
        print("Thanks for playing! Exiting the quiz.")
        break

    # Ignore any invalid input
    if user_input not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, D, or Q.")
        continue

    # Determine the selected answer
    if user_input == 'A':
        answer = CapitalA
    elif user_input == 'B':
        answer = CapitalB
    elif user_input == 'C':
        answer = CapitalC
    elif user_input == 'D':
        answer = CapitalD

    # Check if the answer is correct
    if answer == correct_capital:
        print("Correct!")
        correct += 1
    else:
        print(f"I'm sorry, the correct answer is: {correct_capital}.")
        wrong += 1

    # Provide dashboard to the user
    total_questions = correct + wrong
    print(
        f"Total Questions: {total_questions}, Correct: {correct} ({(correct / total_questions) * 100:.2f}%)"
    )

    # Print space for readability
    print()
    print("--------------------------------------")
    print()

# End of quiz - final summary
print("Quiz Over!")
print(
    f"Final Score: {correct} Correct, {wrong} Incorrect, {correct / (correct + wrong) * 100:.2f}% Correct"
)
