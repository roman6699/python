import random
def get_question():
    with open("spyder.txt", "r", encoding = "utf-8") as f:
        question_list = f.read().splitlines()
        number_qestion = random.randrange(0, len(question_list))
        question_answer = str (question_list[number_qestion])
    for i in range(0, len(question_answer)):
        if question_answer[i]==";":
            question = question_answer[0:i]
            answer = question_answer[i+1:len(question_answer)]
            return answer, question


def play_game():
    print("New game")
    answer, question = get_question()
    print(question)
    print(answer)
    curent_view = []
    for i in range(0,len(answer)):
        curent_view.append("*")
                
    print("".join(curent_view))
    
    guesses = 0
    user_answer = ""
    answered = False
    while guesses < 5:
        user = input("Введите букву или назовите слово: ").lower()
        if user == answer:
            print("Вы правильно назвали слово!")
            answered = True
            break
        if (user in answer):
            print("Есть такая буква")
            for i in range(0,len(answer)):
                if answer[i]== user:
                    curent_view[i]=user
                    user_answer="".join(curent_view)
        else:
            guesses += 1
            print("Такой буквы нет!")
        if user_answer == answer:
            print("Вы правильно назвали все буквы!")
            answered = True
            break
        print(user_answer)
    if (answered):
            play_game()
play_game()
            



