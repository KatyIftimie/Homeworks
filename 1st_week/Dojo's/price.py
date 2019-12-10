import sys

price = ["1500 HUF", "750 HUF", "500 HUF", "300 HUF"]
questions = ["Are you over 14?", "Do you intend to use the sauna?", "Are you a student?", "Are you a woman?"]
answer = ["yes", "no"]
question_number = 1
            


def main(questions, question_number, answer):
    counter = 0
    user_answer = input(questions[counter] + " :")
    user_answer = user_answer.lower()
    for counter in range(len(questions)):
        if user_answer in answer:
            print("Question number " + str(question_number))

            counter += 1
        else:
            print("Don't try to fool me!")
            user_answer = input(questions[counter] + " :")
            # questions[counter] = questions[counter] - 1
            question_number -= 1
            counter = counter - 1

        
        if question_number == 1 and user_answer == "no":
            print("Sorry! You can't get in.")
            sys.exit()
        if question_number == 2 and user_answer == "yes":
            print("The price is going to be " + str(price[0]))
            sys.exit()

        if question_number == 3 and user_answer == "yes":
            print("The price is going to be " + str(price[3]))
            sys.exit()

        if question_number == 4 and user_answer == "yes":
            print("The price is going to be " + str(price[2]))
            sys.exit()

        if question_number == 4 and user_answer == "no":
            print("The price is going to be " + str(price[1]))
            sys.exit()
        question_number += 1
        

        



if __name__ == "__main__":
    main(questions, question_number, answer)
