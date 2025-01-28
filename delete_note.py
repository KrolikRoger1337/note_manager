from datetime import datetime, date

'''
импортируем библиотеку для использования встроенных функций с помощью. которых определим
формат ввода данных для даты
'''
notes = {} # Создаем словарь в котором будем хранить название заметок по ключу
note = {} # создаем словарь в котором у нас будут храниться данные о заметке по ключу
username = [] # создаем список имен пользователей
status = [] # создаем список в котором будем хранить данные о статусе заметки
titles = [] # создаем список в котором будем хранить все заголовки всех заметок
title = [] # создаем список в котором будем хранить данные о заголовках одной заметки после чего очищаться
copy_title = [] # создаем список в котором будут храниться данные заметки title
# предназначенные для записи в titles, чтобы не потерять заголовки создаваемой заметки
contents = [] # создаем список в котором будем хранить все описания заметок
content = [] # создаем временный список в котором будут храниться данные об одной заметке
copy_content = [] # создаем список предназначенный для записи в contents после очищения content,
# чтобы не потерять данные о текущей заметке
created_date = [] # создаем список для хранения данных о дате создания заметки
issue_date = [] # создаем список для хранения данных о завершении созданной заметки
count_name = 0 # создаем счётчик заметок
# создаем функцию для удаления заметки

# создаем функцию для проверки уникальности имен
def check_username(enter_user, username_list):
    for item_name in username_list:
        if enter_user == item_name:
            return True
    return False
# создаем функцию для проверки уникальности заголовков
def check_title(title_check, list_title):
    for item_title in list_title:
        if title_check == item_title:
            return True
    return False
# создаем функцию для проверки дед лайна
def check_deadline(deadline_date):
    # осуществляем перевод str в date, так как передаваемый аргумент преобразован в str
    deadline_date = datetime.strptime(deadline_date, '%d:%m:%Y').date()
    # создаем переменную в которой хранится текущая дата
    today = date.today()
    # узнаем разницу между сегодняшней датой и датой сдачи
    # в случае deadline_date > today(дедлайн не наступил) days_to_deadline > 0
    # в случае deadline_date < today(дедлайн наступил столько то дней назад) days_to_deadline < 0
    # в случае deadline_date == today(дедлайн наступил сегодня) days_to_deadline > 0
    days_to_deadline =  (deadline_date - today).days
    # создаем блок в котором описываем порядок вывода оповещения при различных значениях
    if days_to_deadline == 0:
        print('Дедлайн сегодня')
        # если дедлайн наступил - разность days_to_deadline и today < 0
    elif days_to_deadline < 0:
        # проверяем на то, что количество дней превышает значение в 100
        if 11 <= -days_to_deadline % 100 <= 14:
            print(f'Дедлайн прошел: {-days_to_deadline} дней назад')
        # проверяем на то, что разница days_to_deadline и today равна 1
        elif -days_to_deadline % 10 == 1:
            print(f'Дедлайн прошел: {-days_to_deadline} день назад')
        # проверяем на то, что количество дней в диапазоне от 2 до 4
        elif 2 <= -days_to_deadline % 10 <= 4:
            print(f'Дедлайн прошел: {-days_to_deadline} дня назад')
        # в остальных случаях
        else:
            print(f'Дедлайн прошел: {-days_to_deadline} дней назад')
        # если до дед лайна далеко заходим в этот блок
    else:
        # проверяем на то, что количество дней не превышает значение в 100
        if days_to_deadline % 10 == 1 and days_to_deadline % 100 != 11:
            print(f'До дедлайна: {days_to_deadline} день')
        # исключаем возможность попадания чисел 112-114
        elif 2 <= days_to_deadline % 10 <= 4 and not (12 <= days_to_deadline % 100 <= 14):
            print(f'До дедлайна: {days_to_deadline} дня')
        # все остальные случаи
        else:
            print(f'До дедлайна: {days_to_deadline} дней')

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
# пишем функцию для проверки статуса
def check_status(status_box):
    if status_box.lower() == 'active' or status_box.lower() == 'end' or status_box.lower() == 'in process':
        return True
    else:
        print('Вы ввели не правильный статус заметки, попробуйте ещё раз.')
# Создаем цикл, который не дает закрыться программе при возникновении ошибки
while True:
    # создаем блок перехвата ошибок
    try:
        # Создаем цикл, который не дает закрыться программе по окончанию строк кода
        while True:
            # Создаём меню для работы с заметкой
            print('МЕНЮ:\n'
                  '1. Создать заметку;\n'
                  '2. Редактировать заметку;\n'
                  '3. Удалить заметку;\n'
                  '4. Просмотр существующих заметок;\n'
                  '5. Выход из приложения.\n'
                  'Выберите вариант для работы с заметкой: ', end = ' ')
            # Создаем конструкцию проверки вводимого параметра move_info
            # для выбора режима работы с заметкой
            move_info = input()
            match move_info:
                # Создаем конструкцию для создания заметки и заполнения информации о ней
                case '1':
                    # Подсказка для пользователя о вхождении в раздел создания заметки
                    print("Вы вошли в меню создания замети, пожалуйста заполните все поля в соответствии с примерами:")
                    # Заполняем поля согласно подсказок, при заполнении всех полей согласно примеров
                    # создание заметки закончится автоматически

                    while True:
                        enter_name = input('Введите имя пользователя(User1): ')
                        if check_username(enter_name,username):
                            print('Такой пользователь уже существует, выберите себе другое имя.')
                        else:
                            username.append(enter_name)
                            break

                    note['Имя пользователя'] = username


                    # Создаем цикл для ввода статуса заметки и функцией проверки ее на корректность ввода
                    while True:
                        prov_status = input('Введите статус выполнения заметки(Active, end, in process): ')
                        if check_status(prov_status):
                            status.append(prov_status)
                            note['Статус заметки'] = status
                            break

                    # Создаем цикл для ввода имя заметок и создаем точку выхода из цикла
                    # подсказываем пользователю как выйти из опции добавления имен заметок
                    while True:
                        enter_title = input('Введите имя заметки, прекратить ввод(stop,нажать ENTER): ')
                        if enter_title.lower() == 'stop' or enter_title.lower() == '':
                            break
                        # Проверяем на уникальность заголовков
                        if check_title(enter_title, title):
                            print('Такой заголовок уже существует, придумайте другое название.')
                        else:
                            title.append(enter_title)
                    # Создаем цикл для заполнения списка content, подсказываем пользователю как
                    # выйти из опции добавления текста заметок
                    while True:
                        enter_content = input('Введите текст заметки, прекратить ввод(stop,нажать ENTER): ')
                        # Создаем условие для остановки цикла
                        if enter_content.lower() == 'stop' or enter_content.lower() == '':
                            break
                        else:
                            # добавляем корректный текст заметки
                            content.append(enter_content)

                    while True:
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


                    while True:
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

                    # Создаем заметку в словаре и добавляем каждое значение в соответствии своему ключу
                    copy_title = title.copy() # создаем копию заголовков
                    titles.append(copy_title) # добавляем копию списка для хранения заголовков в общем списке
                    title.clear() # очищаем текущий список для записи следующих данных
                    # данная конструкция нужна для формата записи
                    # note{'dict_key'} : список value(titles)[списки title0[],title1[]...title n-1[]]
                    # без такой записи в список value(titles) значения будут выводиться одним списком
                    # в не правильный формат данных:
                    # note{'dict_key'} : список value[список title[title, title...title]

                    # аналогичная конструкция для описания заметок, такая конструкция позволяет
                    # обеспечить правильный вывод данных и корректное обращение к данным по индексам
                    # ограничивая вывод других данных
                    copy_content = content.copy()
                    contents.append(copy_content)
                    content.clear()

                    note['Заголовки'] = titles
                    note['Описание заметки'] = contents
                    note['Дата создания заметки'] = created_date
                    note['Дата окончания заметки(дедлайн)'] = issue_date

                    # создаем словарь с ключом по индексу и присваиваем ему значение словаря в котором
                    # хранятся данные о заметках для возможности выбора отображения заметок
                    notes.setdefault(count_name,note)
                    count_name += 1 # счетчик срабатывает при добавлении заметки

                # создаем точку входа в режим редактирования заметки
                case '2':
                    while True:
                        # Выбираем заметку для редактирования
                        print('Вы вошли в меню редактирования заметки, выберите редактируемую заметку(Номер): ')
                        # Выводим созданные заметки для выбора редактируемой
                        for key, _ in notes.items():
                            print(f'Заметка № {key};')
                            # выбираем нужную заметку
                        name_key = int(input())
                        while True:
                            # выводим меню для редактирования выбранной заметки
                            print(f'Редактируемая заметка {name_key}:\n'
                                  '1. Изменить имя пользователя;\n'
                                  '2. Изменить статус заметки;\n'
                                  '3. Изменить заголовок заметки;\n'
                                  '4. Изменить текст заметки;\n'
                                  '5. Изменить дату создания заметки;\n'
                                  '6. Изменить сдачу(дедлайн) заметки;\n'
                                  '7. Удалить заголовок;\n'
                                  '8. Выйти из меню редактирования.\n'
                                  'Выберите редактируемый параметр: ', end = ' ')

                            parametr = input()
                            # создаем конструкцию для работы с каждым полем заметки
                            match parametr:
                                # присваиваем новое имя выбранной заметки
                                case '1':
                                    # проверяем на уникальность имени
                                    while True:
                                        new_name = input('Введите новое имя пользователя(User1), если хотите выйти из редактирование имени введите "stop": ')
                                        if new_name.lower() == 'stop':
                                            break
                                        else:
                                            if check_username(new_name, note['Имя пользователя'][name_key]):
                                                print('Такой пользователь уже существует, придумайте себе другое имя.')
                                            else:
                                                note['Имя пользователя'][name_key] = new_name
                                                print('Имя пользователя заметки изменено.')
                                                break

                                # присваиваем новый статус выбранной заметки с проверкой на правильность
                                # ввода данных

                                case '2':
                                    new_status = input('Введите новый статус заметки(active, end or in process), если хотите выйти из редактирования статуса, введите "stop": ')
                                    if new_status.lower() == 'stop':
                                        break
                                    else:
                                        check_status(new_status)
                                        note['Статус заметки'][name_key] = new_status
                                        print('Статус заметки изменен.')

                                # присваиваем новое имя заголовка
                                case '3':
                                    print(note['Заголовки'][name_key])
                                    n_title = input('Выберите изменяемый заголовок, если хотите выйти из редактирования заголовка введите "stop": ')
                                    if n_title.lower() == 'stop':
                                        break
                                    else:
                                        index = note['Заголовки'][name_key].index(n_title)
                                        while True:
                                            new_title = input('Введите новое имя заголовка: ')
                                            if check_title(new_title,note['Заголовки'][name_key]):
                                                print('Такой заголовок для данной заметки уже существует, придумайте новый заголовок')
                                            else:
                                                note['Заголовки'][name_key][index] = new_title
                                                break
                                        print('Заголовок заметки изменен.')
                                # присваиваем новое описание заметки в соответствии с заголовком
                                case '4':
                                    print(note['Заголовки'][name_key])
                                    n_content = input('Выберите заголовок изменяемого текста или введите "stop" для выхода из редактирования описания: ')
                                    if n_content.lower() == 'stop':
                                        break
                                    else:
                                        index = note['Заголовки'][name_key].index(n_content)
                                        note['Описание заметки'][name_key][index] = input('Введите новое описание заметки: ')
                                        print('Описание заметки изменено.')
                                # присваиваем новую дату создания заметки с проверкой на корректность ввода
                                case '5':
                                    print(note['Дата создания заметки'][name_key])
                                    while True:
                                        new_created_date = input('Введите новую дату создания заметки или "stop" для выхода из редактирования даты: ')
                                        if new_created_date.lower() == 'stop':
                                            break
                                        else:
                                            if check_date_format(new_created_date):
                                                note['Дата создания заметки'][name_key] = new_created_date
                                                print('Дата создания заметки успешно изменена.')
                                                break
                                            else:
                                                print('Не корректный ввод дынных.')
                                # присваиваем новую дату окончания заметки с проверкой на корректность ввода
                                case '6':
                                    print(note['Дата окончания заметки(дедлайн)'][name_key])
                                    while True:
                                        new_issue_date = input('Введите новую дату окончания заметки: ')
                                        if new_issue_date.lower() == 'stop':
                                            break
                                        else:
                                            if check_date_format(new_issue_date):
                                                note['Дата окончания заметки(дедлайн)'][name_key] = new_issue_date
                                                print('Дата окончания заметки успешно изменена.')
                                                break
                                            else:
                                                print('Не корректный ввод дынных.')
                                # для удаления заголовка и соответствующего ему описания
                                case '7':
                                    if len(note['Заголовки'][name_key]) == 0:
                                        print('У вас отсутствуют заголовки, создайте их.')
                                        break
                                    else:
                                        print(note['Заголовки'][name_key])
                                        delete_title = input('Помните! Удаляя заголовок вы удаляете '
                                                                                        'соответствующее ему описание.\n'
                                                                                        'Выберите удаляемый заголовок(Имя заголовка) '
                                                                                        'или введите "stop" для выхода из удаления заголовка: ')
                                        if delete_title.lower() == 'stop':
                                            break
                                        else:
                                            index = note['Заголовки'][name_key].index(delete_title)
                                            del note['Заголовки'][name_key][index]
                                            del note['Описание заметки'][name_key][index]
                                            print('Заголовок заметки успешно удалён.')
                                # для выхода из меню редактирования заметки
                                case '8':
                                    print('Вы вышли из редактора заметок')
                                    break
                        break
                # создаем точку входа для удаления заметки
                case '3':

                    print('Вы вошли в меню удаления заметки. ')
                    if len(notes) == 0:
                        print('У вас нет заметок')
                    else:
                        print('Выберите способ удаление заметки(Номер):\n'
                              '1. Удаление по номеру заметки;\n'
                              '2. Удаления по имени пользователя.')
                        choose_delete = input('Выберите способ удаления(Номер) или введите "stop", чтобы остановить удаление заметок: ')
                        if choose_delete.lower() == 'stop':
                            break
                        else:
                            match choose_delete:
                                case '1':
                                    # выводим список существующих заметок
                                    print('Список существующих заметок:')
                                    for key, _ in notes.items():
                                        print(f'Заметка № {key}', end = ' ')
                                    # выбираем удаляемую заметку
                                    key_note = int(input('Введите название удаляемой заметки(Номер): '))
                                    # удаляем выбранную заметку
                                    del notes[key_note]
                                    del note['Имя пользователя'][key_note]
                                    del note['Статус заметки'][key_note]
                                    del note['Заголовки'][key_note]
                                    del note['Описание заметки'][key_note]
                                    del note['Дата создания заметки'][key_note]
                                    del note['Дата окончания заметки(дедлайн)'][key_note]
                                    # уменьшаем счётчик заметок, для корректного присваивания в словаре и обращения по ключу
                                    count_name -= 1
                                    print('Заметка успешно удалена.')

                                case '2':
                                    print('Список существующих заметок:')
                                    for item in username:
                                        print(item, end = ' ')
                                    index = note['Имя пользователя'].index(input('\nВведите название удаляемой заметки(Имя пользователя): '))
                                    del notes[index]
                                    del note['Имя пользователя'][index]
                                    del note['Статус заметки'][index]
                                    del note['Заголовки'][index]
                                    del note['Описание заметки'][index]
                                    del note['Дата создания заметки'][index]
                                    del note['Дата окончания заметки(дедлайн)'][index]
                                    # уменьшаем счётчик заметок, для корректного присваивания в словаре и обращения по ключу
                                    count_name -= 1
                                    print('Заметка успешно удалена.')

                            # обновляем нумерацию заметок после удаления
                            notes = {new_key: value for new_key, value in enumerate(notes.values())}

                # создаем точку входа для отображения существующих заметок
                case '4':
                    # выводим существующие заметки для выбора конкретной из них
                    if len(notes)!=0:
                        for key, _ in notes.items():
                            print(f'Заметка № {key}:')
                        # выбираем нужную заметку
                        index_note = input('Выберите заметку для просмотра информации о ней(Номер) или введите "stop" '
                                               'для выхода из меню просмотра заметок: ')
                        if index_note.lower() == 'stop':
                            break
                        else:
                            # Выводим содержимое выбранной заметки key отображает описание каждого раздела
                            # value отображает содержание раздела для конкретной заметки
                            # index_note нужен для вывода из общего списка словаря только те данные,
                            # которые соответствуют выбранной заметки. Индексы заметки и индексы по которым
                            # идет обращение к общим спискам совпадают. Пример обращения
                            # key в notes == index_note в словаре note содержится списки всех разделов и для каждой
                            # заметки в словаре есть свой список и свое значение
                            index_note = int(index_note)
                            for key, value in note.items():
                                if key.lower() == 'дата создания заметки' or key.lower() == 'дата окончания заметки(дедлайн)':
                                    print(f'{key} : {value[index_note][:5]}')
                                elif key.lower() == 'заголовки':
                                    print(f'{key} : {value[index_note]}')
                                elif key.lower() == 'описание заметки':
                                    print(f'{key} : {value[index_note]}')
                                elif key.lower() == 'имя пользователя':
                                    print(f'{key} : {value[index_note]}')
                                elif key.lower() == 'статус заметки':
                                    print(f'{key} : {value[index_note]}')
                                else:
                                    print(f'{key} : {value}')
                            deadline = note['Дата окончания заметки(дедлайн)'][index_note]
                            check_deadline(deadline)
                    else:
                        print('У вас нет заметок. Создайте заметки.')

                # создаем возможность корректного завершения программы
                case '5':
                    break
        break
    # создаем блок перехвата значений для корректной работы программы
    except ValueError:
        print('Вы что-то делаете не так попробуйте ввести корректное значение')
    except IndexError:
        print('Вы что-то делаете не так попробуйте ввести корректное значение')
