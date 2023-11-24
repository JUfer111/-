print("Добро пожаловать в квиз про нефть!")
print("Ответь на следующие вопросы:")
questions=["Какая страна на топ 1 стран по добычи нефти?:","Чем нефть полезна для людей?:","Когда впервые нашли нефть?:", "Кто первый нашел нефть?:", "Когда впервые появилась нефть?:"]
answers= ["Саудовская Аравия","Для медицины","1846", "Саламанов Фарман", "50-350 млн лет назад"]
Points=0
print(questions[0])
answer_1=input()
if answer_1==answers[0]:
    print("вы ответили правильно, вы получили 1 балл")
    Points=Points + 1
else:
    print(f"Вы ответили неправилно, а правильный ответ был {answers[0]}")
print(questions[1])
answer_2= input()
if answer_2==answers[1]:
    print("вы ответили правильно, вы получили 1 балл")
    Points=Points + 1
else:
    print(f"Вы ответили неправилно, а правильный ответ был {answers[1]}")
print(questions[2])
answer_3= str(input())
if answer_3==answers[2]:
    print("вы ответили правильно, вы получили 1 балл")
    Points=Points + 1
else:
    print(f"Вы ответили неправилно, а правильный ответ был {answers[2]}")
print(questions[3])
answer_4=input()
if answer_4==answers[3]:
    print("вы ответили правильно, вы получили 1 балл")
    Points=Points + 1
else:
    print(f"Вы ответили неправилно, а правильный ответ был {answers[4]}")
print(questions[4])
answer_5=input()
if answer_5==answers[4]:
    print("вы ответили правильно, вы получили 1 балл")
    Points=Points + 1
else:
    print(f"Вы ответили неправилно, а правильный ответ был {answers[4]}")
print(f"У вас {Points} баллов!")