
# not done
ideabank = ["Your ideabank: "]
i = 1



new_idea = []
questions = ["ID: ", "Your idea: "]

file = open('ideabank.txt', 'w')


def appending_ideas(new_idea, questions):
    for i in range(len(questions)):
        get_ideas = input(questions[i])
        new_idea.append(get_ideas)
    return new_idea


print(appending_ideas(new_idea, questions))

