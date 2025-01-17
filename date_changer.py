from datetime import datetime
username = 'username'
title = 'title'
content = 'content'
status = 'status'
issue_date = 'issue_date'
created_date = ''
#print(f'Имя пользователя: {username}')
#print(f'Заголовок заметки: {title}')
#print(f'Описание заметки: {content}')
#print(f'Статус заметки: {status}')
#print(f'Дата создания заметки в формате "день-месяц-год", например "10:11:2024":'
 #     f' {created_date}')
#print(f'Дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10:12:2024":'
 #     f' {issue_date}')
flag = True
def check_date_format(date_string):
    try:
        datetime.strptime(date_string, '%d:%m:%Y')
        return True
    except ValueError:
        return False

while flag == True:
    temp_created_date = input()
    if check_date_format(temp_created_date):
        print(f"Дата введена корректно: {temp_created_date[:5]}")
        created_date = temp_created_date
        flag=False
    else:
        print(f"Некорректный формат даты,введите дату снова:")
        flag=True

print(created_date)