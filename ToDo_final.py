import random
todos = {}
HELP = '''
Список доступных команд:
* show - напечать все задачи на заданную дату
* add - добавить задачу
* help - Напечатать help
* random - добавить случайную задачу на сегодня
'''
RANDOM_TASKS = [
  'Написать Гвидо письмо',
  'Выучить Python',
  'Записаться на курс в Нетологию',
  'Посмотреть 4 сезон Рик и Морти'
]
def add_todo(date, task):
    if date in todos:
        todos[date].append(task)
    else:
        todos[date]=[]
        todos[date].append(task)
    print(f'Задача {task} добавлена на {date}')

while True:
    command=input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        add_todo(date,task)
    elif command == 'show':
        date = input('Введите дату: ')
        if date in todos:
            for task in todos[date]:
                print(f'[]{task}')
        else:
            print('На эту дату задач нет')
    elif command == 'random':
        date = 'Сегодня'
        add_todo(date, random.choice(RANDOM_TASKS))
    else:
        print ('Неизвестная команда!')
        break
