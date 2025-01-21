from datetime import datetime

'''
импортируем библиотеку для использования встроенных функций с помощью. которых определим
формат ввода данных для даты
'''

note = {}
title = []
content = []
created_date = '' # обявляем переменную с пустой строкой для будущей записи
issue_date = ''
stop_note = ''
flag_created_date = True
flag_issue_date = True

# пишем функцию для приведения даты к единому формату
def check_date_format(date_string):
    # испоьзуем блоки try except для перехвата ошибки формата данных
    try:
        datetime.strptime(date_string, '%d:%m:%Y')
        # переводим введеную дату к определяемому формату и сразу делаем проверку на выход
        # за границы диапозона
        return True
        # в случае корректного ввода даты возвращаем значения для выхода из блока
    except ValueError:
        # в случае не корректного ввода данных перехватываем ошибку и повторяем ввод
        return False


username = input('Введите имя пользователя: ')
note['Имя пользователя'] = username
status = input('Введите статус выполнения заметки: ')
note['Статус заметки'] = status
while True:
    enter_title = input('Введите имя заметки, прекратить ввод(stop,нажать ENTER): ')
    if enter_title.lower()=='stop' or enter_title.lower()=='' :
        break
    else:
        title.append(enter_title)

while True:
    enter_content = input('Введите текст заметки, прекратить ввод(stop,нажать ENTER): ')
    if enter_content.lower() == 'stop' or enter_content.lower() == '':
        break
    else:
        content.append(enter_content)

while flag_created_date:
# пока flag будет истинной блок будет запрашивать корректный ввод данных
    temp_created_date = input('Введите дату создания заметки в формате 12:12:2024: ')
    if check_date_format(temp_created_date):
                # проверяем на корректность ввода даты в случае верности ввода
                # в блоке try выведется True, которая приведет в эту часть if
                # и выведет нас из блока if else и следом из цикла while
                # так как flag установится в False
        print("Дата введена корректно.")
        created_date = temp_created_date[:5]
        flag_created_date = False
    else:
                # в случае перехвата ошибки в блоке try except в нем сгенерируется значение
                # False которое приведет в эту часть блока if else, так как введен
                # не верный формат данных и цикл повторится заново
        print(f"Некорректный формат даты.", end = ' ')
        flag_created_date = True

while flag_issue_date:
            # пока flag будет истинной блок будет запрашивать корректный ввод данных
    temp_issue_date = input('Введите дату истечения заметки (дедлайн) в формате 12:12:2024: ')
    if check_date_format(temp_issue_date):
                # проверяем на корректность ввода даты в случае верности ввода
                # в блоке try выведется True, которая приведет в эту часть if
                # и выведет нас из блока if else и следом из цикла while
                # так как flag установится в False
        print("Дата введена корректно.")
        issue_date = temp_issue_date[:5]
        flag_issue_date = False
    else:
                # в случае перехвата ошибки в блоке try except в нем сгенерируется значение
                # False которое приведет в эту часть блока if else, так как введен
                # не верный формат данных и цикл повторится заново
        print(f"Некорректный формат даты", end = ' ')
        flag_issue_date = True
note['Заголовки'] = title
note['Описание заметки'] = content
note['Дата создания заметки'] = created_date
note['Дата окончания заметки(дедлайн)'] =issue_date
for key, value in note.items():
    print(f'{key.capitalize()} : {value}')