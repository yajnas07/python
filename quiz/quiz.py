import requests
import json
import random

def fetch_questions():
    url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"
    response = requests.get(url)
    response_json = response.json()
    questions = response_json["results"]
    return questions

def run_quiz(question, options, answer):
    # print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    user_answer = int(input("Enter the number of the correct answer: "))

    if user_answer == (answer + 1):
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is", options[answer])
        return 0
        

def main():
    questions = fetch_questions()

    score = 0
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        options = question["incorrect_answers"] + [question["correct_answer"]]
        
        # random.shuffle(options)
        # for j, option in enumerate(options):
        #     print(f"{j + 1}. {option}")

        # user_answer = input("Enter your answer: ")
        score += run_quiz(question, options, options.index(question["correct_answer"]))
        # if user_answer == question["correct_answer"]:
        #     print("Correct!")
        #     score += 1
        # else:
        #     print("Incorrect.")
        #     correct_answer = question["correct_answer"]
        #     print(f"Correct answer is {correct_answer}")

    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()
