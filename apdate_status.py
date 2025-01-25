from datetime import datetime

'''
импортируем библиотеку для использования встроенных функций с помощью. которых определим
формат ввода данных для даты
'''
notes = {}
note = {}
note_copy = []
username = []
status = []
title = []
content = []
created_date = [] # объявляем переменную с пустой строкой для будущей записи
issue_date = []
stop_note = ''
flag_created_date = True
flag_issue_date = True
flag_case_2 = True
count_name = 0
counter_title = 0
counter_content = 0
# пишем функцию для приведения даты к единому формату
def check_date_format(date_string):
    # используем блоки try except для перехвата ошибки формата данных
    try:
        datetime.strptime(date_string, '%d:%m:%Y')
        # переводим введенную дату к определяемому формату и сразу делаем проверку на выход
        # за границы диапазона
        return True
        # в случае корректного ввода даты возвращаем значения для выхода из блока
    except ValueError:
        # в случае не корректного ввода данных перехватываем ошибку и повторяем ввод
        return False

def chek_status(status_box):
    if status_box.lower() == 'active' or status_box.lower() == 'end' or status_box.lower() == 'in process':
        return True
    else:
        print('Вы ввели не правильный статус заметки, попробуйте ещё раз.')

while True:
    print('Выберите вариант для работы с заметкой:\n'
          '1. Создать заметку;\n'
          '2. Редактировать заметку;\n'
          '3. Удалить заметку;\n'
          '4. Просмотр существующих заметок;\n'
          '5. Выход из приложения.')
    move_info = input()
    match move_info:
        case '1':
            print("Вы вошли в меню создания замети, пожалуйста заполните все поля в соответствии с примерами:")
            username.append(input('Введите имя пользователя: '))
            note['Имя пользователя'] = username
            while True:
                prov_status = input('Введите статус выполнения заметки(Active, end, in process): ')
                if chek_status(prov_status):
                    status.append(prov_status)
                    note['Статус заметки'] = status
                    break
            while True:
                enter_title = input('Введите имя заметки, прекратить ввод(stop,нажать ENTER): ')
                if enter_title.lower() == 'stop' or enter_title.lower() == '':
                    break
                else:
                    title.append(enter_title)
                    counter_title+=1

            while True:
                enter_content = input('Введите текст заметки, прекратить ввод(stop,нажать ENTER): ')
                if enter_content.lower() == 'stop' or enter_content.lower() == '':
                    break
                else:
                    content.append(enter_content)
                    counter_content+=1

            while flag_created_date:
                # пока flag будет истинной блок будет запрашивать корректный ввод данных
                temp_created_date = input('Введите дату создания заметки в формате 12:12:2024: ')
                if check_date_format(temp_created_date):
                    # проверяем на корректность ввода даты в случае верности ввода
                    # в блоке try выведется True, которая приведет в эту часть if
                    # и выведет нас из блока if else и следом из цикла while
                    # так как flag установится в False
                    print("Дата введена корректно.")
                    created_date.append(temp_created_date)

                    break
                else:
                    # в случае перехвата ошибки в блоке try except в нем сгенерируется значение
                    # False которое приведет в эту часть блока if else, так как введен
                    # не верный формат данных и цикл повторится заново
                    print(f"Некорректный формат даты.", end=' ')


            while flag_issue_date:
                # пока flag будет истинной блок будет запрашивать корректный ввод данных
                temp_issue_date = input('Введите дату истечения заметки (дедлайн) в формате 12:12:2024: ')
                if check_date_format(temp_issue_date):
                    # проверяем на корректность ввода даты в случае верности ввода
                    # в блоке try выведется True, которая приведет в эту часть if
                    # и выведет нас из блока if else и следом из цикла while
                    # так как flag установится в False
                    print("Дата введена корректно.")
                    issue_date.append(temp_issue_date)
                    break
                else:
                    # в случае перехвата ошибки в блоке try except в нем сгенерируется значение
                    # False которое приведет в эту часть блока if else, так как введен
                    # не верный формат данных и цикл повторится заново
                    print(f"Некорректный формат даты", end=' ')


            note['Заголовки'] = title
            note['Описание заметки'] = content
            note['Дата создания заметки'] = created_date
            note['Дата окончания заметки(дедлайн)'] = issue_date
            notes.setdefault(f'Заметка № {count_name};',note_copy)
            count_name += 1
        case '2':
            while flag_case_2:
                print('Вы вошли в меню редактирования заметки, выберите редактируемую заметку:')
                for key, _ in notes.items():
                    print(f'{key.capitalize()}')
                name_key = int(input())
                print(f'Вы выбрали заметку {name_key} , выберите редактируемый параметр:\n'
                      '1. Изменить имя пользователя;\n'
                      '2. Изменить статус заметки;\n'
                      '3. Изменить заголовок заметки;\n'
                      '4. Изменить текст текст заметки;\n'
                      '5. Изменить дату создания заметки;\n'
                      '6. Изменить сдачу(дедлайн) заметки;\n'
                      '7. Выйти из меню редактирования.')
                parametr = input()
                match parametr:
                    case '1':
                        username = input('Введите новое имя пользователя: ')
                        note['Имя пользователя'][name_key] = username
                    case '2':
                        new_status = input('Введите новое имя пользователя')
                        chek_status(new_status)
                        note['Статус заметки'][name_key] = new_status
                    case '3':
                        print(note['Заголовки'])
                        index_title = int(input('Выберите изменяемый заголовок: '))
                        note['Заголовки'][index_title] = input('Введите новое название заголовка:')
                        pass
                    case '4':
                        print(note['Описание заметки'])
                    case '5':
                        print(note['Дата создания заметки'])
                    case '6':
                        print(note['Дата окончания заметки(дедлайн)'])
                    case '7':
                        break
                break
        case '3':
            print('Вы вошли в меню удаления заметки, выберите заметку:')
            x = notes.keys()
            print(x)
            key_note = input('Ведите название удаляемой заметки:')
            del note[key_note]
            count_name-=1
        case '4':
            for key, _ in notes.items():
                print(f'{key.capitalize()}')
            print('Выберите заметку для просмотра информации о ней: ')
            index_note = int(input())
            for key, value in note.items():
                if key.lower() == 'дата создания заметки' or key.lower() == 'дата окончания заметки(дедлайн)':
                    print(f'{key.capitalize()} : {value[index_note]}')
                elif key.lower() == 'заголовки':
                    print(f'{key.capitalize()} : {value[:]}')
                elif key.lower() == 'описание заметки':
                    print(f'{key.capitalize()} : {value[:]}')
                elif key.lower() == 'имя пользователя':
                    print(f'{key.capitalize()} : {value[index_note]}')
                elif key.lower() == 'статус заметки':
                    print(f'{key.capitalize()} : {value[index_note]}')
                else:
                    print(f'{key.capitalize()} : {value}')
        case '5':
            break

