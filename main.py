print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы:")

questions = [



    "1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
    "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
    "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
    "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
    "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
    "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
    "7. Как называется разница между выручкой и затратами компании?"
]
answers = [
"Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"
]
result = 0
print(questions[0])
user_input = input("ответ")
if answers [0].lower() == user_input.lower():
    result = result + 1

    print("Верно")
else:
    print("Не верно")

print(questions[1])
user_input = input("ответ")
if answers [1].lower() == user_input.lower():
    result = result + 1
    print("Верно")
else:
    print("Не верно")
print(questions[2])
user_input = input("ответ")
if answers [2].lower() == user_input.lower():
    result = result + 1
    print("Верно")
else:
    print("Не верно")
print(questions[3])
user_input = input("ответ")
if answers [3].lower() == user_input.lower():
    result = result + 1
    print("Верно")
else:
    print("Не верно")
print(questions[4])
user_input = input("ответ")
if answers [4].lower() == user_input.lower():
    result = result + 1
    print("Верно")
else:
    print("Не верно")
print(questions[5])
user_input = input("ответ")
if answers [5].lower() == user_input.lower():
    result = result + 1
    print("Верно")
else:
    print("Не верно")
print(questions[6])
user_input = input("ответ")
if answers [6].lower() == user_input.lower():
    result = result + 1
    print("Верно")
else:
    print("Не верно")
if result > 5:
    print("Это отличный результат!Ты много знаешь о стартапах.")
elif result > 3:
    print("Неплохой результат!Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:
    print("Видимо, ты только начинаешь свой путь к стартапам!Ты ещё много узнаешь о мире, где мы живём.")


