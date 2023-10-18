# William Eng
# weng2@oakland.edu
# generating random quiz files

# Create 16 different quizzes.
# • Create 20 basic arithmetic problems for each quiz.
# • Provides the correct answer for each problem.
# • Writes the quizzes to 16 text files.
# • Writes the answers to 16 text files.

import random

# Generate 16 quiz files
# quiz_files = []
# answer_files = [] 
for quiz_num in range(16):
    # TODO: Create the quiz and answer key files.
    quiz_file = open("quiz" + str(quiz_num+1) + ".txt", 'w')
    answer_file = open("quiz_answer" + str(quiz_num+1) + ".txt", 'w')
    # TODO: write out the header for the quiz.
    title = "Basic Arithmetic Quiz (Form " + str(quiz_num+1) + ")"
    quiz_file.write("Name:\nDate:\n\n" + title.center(50)+ "\n")
    quiz_file.close()
    answer_file.close()
    # Create 20 basic arithmetic problems.
    for question_num in range(20):
        # TODO: Generate a random basic arithmetic problem
        operator = random.choice(['+', '-', '*', '/'])
        # must be between 0 and 100 included
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)
        if operator == '+':
            question = str(question_num + 1) + '. \t' + str(number1) + ' + ' + str(number2) + ' = ' + '______' + '\n'
            answer = number1 + number2 
            answer = str(question_num + 1) + '. \t' + str(answer) + '\n'
        elif operator == '-':
            question = str(question_num + 1) + '. \t'+ str(number1) + ' - ' + str(number2) + ' = ' + '______' + '\n'
            answer = number1 - number2 
            answer = str(question_num + 1) + '. \t' + str(answer) + '\n'
        elif operator == '*':
            question = str(question_num + 1) + '. \t'+ str(number1) + ' * ' + str(number2) + ' = ' + '______' + '\n'
            answer = number1 * number2
            answer = str(question_num + 1) + '. \t' + str(answer) + '\n'
        else: 
            # do not divide by 0
            number2 = random.randint(1, 100)
            question = str(question_num + 1) + '. \t'+ str(number1) + ' / ' + str(number2) + ' = ' + '______' + '\n'
            answer = number1 / number2
            answer = round(answer, 2)
            answer = str(question_num + 1) + '. \t' + str(answer) + '\n'
            
        # TODO: Write the question to the quiz file
        quiz_file = open("quiz" + str(quiz_num+1) + ".txt", 'a')
        quiz_file.write(question)
        # TODO: Write the answer to a file.
        answer_file = open("quiz_answer" + str(quiz_num+1) + ".txt", 'a')
        answer_file.write(answer)
    quiz_file.close()
    answer_file.close()