
"""Делаю функцию проверки ответов чтоб не писать сто раз if-else"""

def check_answer(questions, correct_answers, name):
  """Счетчик баллов, процентов, общее кол-во вопросов"""
  global score, correct_count, total_questions
  print(questions)
  answer = input().lower()

  if answer == correct_answers:
    print(f'Молодец, {name}!Ты получашь 10 балов')
    score += 10
    correct_count += 1
  else:
    print(f'Неверно, {name}, правильный ответ: {correct_answers}.')
  total_questions += 1


print("Привет! Предлагаю проверить свои знания английского! Напиши, как тебя зовут.")
name = input()
score = 0
correct_count = 0
total_questions = 0

print(f'Привет, {name}, начинаем тренировку')

check_answer(f'My name ____ {name}', "is", name)
check_answer(f'I ____ a coder', "am", name)
check_answer(f'I live ___ Moscow', "in", name)

if total_questions > 0:
  """Расчет процентов"""
  accuracy = (correct_count / total_questions) * 100
else:
    accuracy = 0

print(f'''Вот и все, {name}!
Ты ответил на {correct_count} из {total_questions} верно.
Ты заработал {score} баллов.
Это {accuracy:.2f}% правильных ответов.''')  # Вывод процентов