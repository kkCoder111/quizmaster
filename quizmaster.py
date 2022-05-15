# Imports
import time
import os

print("QuizMaster by kkCoder111")

print("For more info, visit: https://github.com/kkCoder111/quizmaster")

# Global Variables

quiz_name = "Untitled Quiz"
author = str(os.getlogin())
questions = []
answers = []
correct_answers = []
custom_point_values = {}
point_values = 500

# Functions

def set_quiz_name(name, creator):
    '''Sets the quiz name. (Expected: str, str)'''
    global quiz_name
    global author
    
    quiz_name = name
    author = creator


def default_point_values(point_value):
    '''Sets the default point values for questions.
    This can be overridden. (Expected: int)'''
    global point_values
    if point_value < 0:
        point_values = point_values
    else:
        point_values = point_value
def add_question(question_title, answer_list, correct_answer, point_value):
    '''Adds a question. (Expected: str, list, int, int)'''
    global questions, answers, correct_answers, point_values, custom_point_values
    questions.append(question_title)
    answers.append(answer_list)
    correct_answers.append(correct_answer)

    if point_value > 0:
        custom_point_values[question_title] = point_value

#Main code
def startQuiz():
    global quiz_name
    global author
    global questions
    global answers
    global correct_answers
    global custom_point_values
    global point_values
    correct = 0
    points = 0
    print("Quiz:", quiz_name, "by", author)
    time.sleep(2)
    print("Now for the questions.\n \n \n")
    time.sleep(2)

    for question in range(len(questions)):
        current_points = 0
        print(questions[question])
        answer_print = []
        for answer in range(len(answers[question])):
            answer_print.append(answers[question][answer])
        print("Answers: \n")
        for answer in range(len(answer_print)):
            print("[" + str(answer) + "] " + answer_print[answer])
        allowed = []
        for allow in range(len(answer_print)):
            allowed.append(str(allow))
        print("\n")
        response = input("Enter your answer:")
        while response not in allowed:
            print("Not a valid choice \n")
            response = input("Enter your answer:")
        print("\n")
        response = int(response)

        try:
            current_points = custom_point_values[questions[question]]
        except KeyError:
            current_points = point_values

        if answer_print[response] == correct_answers[question]:
            print("Good job!")
            print(str(current_points) + " more points for you!")
            correct += 1

            points += current_points

        else:
            print("Nope.")
            print("The correct answer was:", correct_answers[question])

        time.sleep(4)
        print("\n \n \n \n")

            

    print("Score:", str(points))
    print("Correct:", str(correct) + "/" + str(len(questions)))
    time.sleep(2)

    print("Thanks for playing!")
    print("Learn how to make your own quiz at:")
    print("https://github.com/kkCoder111/quizmaster/wiki")

    print(questions, answers, correct_answers)
    print(quiz_name, author)

    time.sleep(4)

