#@
# Волков В.Ю.
#
import sqlite3

conn = sqlite3.connect('quiz_results.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS results
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                score INTEGER)''')
conn.commit()

def start_quiz():
    questions = [
    {"question": "Какая столица Франции?", "answers": ["Париж", "Лондон", "Берлин", "Рим"], "correct_answer": "Париж"},
    {"question": "Сколько планет в Солнечной системе?", "answers": ["7", "8", "9", "10"], "correct_answer": "8"},
    {"question": "Какой язык является самым распространенным в мире?", "answers": ["Китайский", "Английский", "Испанский", "Русский"], "correct_answer": "Китайский"},
    {"question": "Какой самый большой материк на планете?", "answers": ["Африка", "Евразия", "Северная Америка", "Южная Америка"], "correct_answer": "Евразия"},
    {"question": "Какая самая длинная река в мире?", "answers": ["Нил", "Амазонка", "Янцзы", "Миссисипи"], "correct_answer": "Нил"},
    {"question": "Сколько дней в феврале в обычном году?", "answers": ["30", "31", "28", "29"], "correct_answer": "28"},
    {"question": "Как называется национальный цвет Италии?", "answers": ["синий", "красный", "зеленый", "желтый"], "correct_answer": "зеленый"},
    {"question": "Сколько дней в году?", "answers": ["366", "250", "365", "301"], "correct_answer": "365"},
    {"question": "Какой цвет у облаков?", "answers": ["синий", "зеленый", "красный", "белый"], "correct_answer": "белый"},
    {"question": "Как называется самая большая планета в Солнечной системе?", "answers": ["Сатурн", "Юпитер", "Земля", "Нептун"], "correct_answer": "Юпитер"},
    ]

    name = input("Введите ваше имя: ")
    score = 0
    
    print("Ответьте на вопросы (введите номер ответа):")
    for i, q in enumerate(questions, 1):
        corr_answ = 0
        print(f"Вопрос {i}: {q['question']}")
        for j, ans in enumerate(q['answers'], 1):
            print(f"{j}. {ans}")
            if ans == q['correct_answer']:
                corr_answ = j
        user_answer = input("Выберите ответ: ")
        if int(user_answer) == corr_answ:
            print("Правильно!\n")
            score += 1
        else:
            print(f"Неправильно. Правильный ответ: {q['correct_answer']}\n")
    
    print(f"Игра завершена. Ваш результат: {score}/{len(questions)}")
    
    cursor.execute("INSERT INTO results (name, score) VALUES (?, ?)", (name, score))
    conn.commit()

def show_results():
    print("Таблица лидеров:")
    cursor.execute("SELECT name, score FROM results ORDER BY score DESC")
    for row in cursor.fetchall():
        print(f'{row[0]} - {row[1]}')


while True:
    print("Выберите действие:")
    print("1. Начать игру")
    print("2. Показать результаты")
    print("3. Выйти")

    choice = int(input())
    if choice == 1:
        start_quiz()
    elif choice == 2:
        show_results()
    elif choice == 3:
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

conn.close()
