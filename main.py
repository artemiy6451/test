import vk_api
import requests
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from package import package
import sqlite3

session = requests.Session()

vk_session = vk_api.VkApi(token='207b5701fac3bf264fc8bdf0f2416dd4fbad3f54e07d3ca91f77db5414527f04178d5538a639dbad930fc') #Токен вк

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

user_table_id = 0
user_id = '254928937'
flag = False

vk.messages.send(user_id='254928937', random_id='0',
                             message='Дай ссылку на инвентарь')

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
user_id INT PRIMARY KEY,
user TEXT,
link TEXT
)""")
db.commit()

while True:
    for event in longpoll.listen():
        try:
        if event.type == VkEventType.MESSAGE_NEW:
            if 'https://steamcommunity.com/' in event.text:
                url = event.text
                package.get(url)
                keyboard = vk_api.keyboard.VkKeyboard(one_time=True)

                '''sql.execute(f'SELECT * FROM users WHERE user = "{event.text}"')
                result = sql.fetchall()
                url = result[0][2]'''

                sql.execute(f'SELECT user FROM users WHERE user = "{package.name}"')
                if sql.fetchone() is None:
                    sql.execute(f'SELECT * FROM users')
                    result = sql.fetchall()
                    if result == []:
                        user_table_id = 0
                    else:
                        print(result)
                        user_table_id = result[-1][0] + 1
                        print(user_table_id)

                    sql.execute(f'INSERT INTO users VALUES(?,?,?)', (user_table_id,package.name, url))
                    db.commit()
                    print('done')
                else:
                    print('is gone')

                n = 0
                for i in package.game_mass:
                    if n == 4 or n == 8 or n == 12 or n == 16 or n == 20:
                        keyboard.add_line()
                        keyboard.add_button(package.game_mass[n], color=VkKeyboardColor.DEFAULT)
                        n += 1
                    else:
                        keyboard.add_button(package.game_mass[n], color=VkKeyboardColor.DEFAULT)
                        n += 1
                keyboard.add_line()
                keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
                vk.messages.send(user_id=user_id,
                                 keyboard=keyboard.get_keyboard(),
                                 random_id='0',
                                 message='Выберите игру')
                for event_1 in longpoll.listen():
                    if event_1.type == VkEventType.MESSAGE_NEW:
                        if event_1.text in package.game_mass:
                            index = package.game_mass.index(event_1.text)
                            if int(package.number_mass[index]) == 1:
                                vk.messages.send(user_id=user_id, random_id='0',
                                                 keyboard=keyboard.get_keyboard(),
                                                 message=f'Сейчас в инвентаре {package.number_mass[index]} предмет.')
                            elif int(package.number_mass[index]) <= 4:
                                vk.messages.send(user_id=user_id, random_id='0',
                                                 keyboard=keyboard.get_keyboard(),
                                                 message=f'Сейчас в инвентаре {package.number_mass[index]} предмета.')
                            else:
                                vk.messages.send(user_id=user_id, random_id='0',
                                                 keyboard=keyboard.get_keyboard(),
                                                 message=f'Сейчас в инвентаре {package.number_mass[index]} предметов.')
                        if event_1.text == 'Назад':
                            flag = True
                            if flag:
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
                    sql.execute('SELECT user FROM users')
                    result = sql.fetchall()
                    x = 0
                    for i in result:
                        i = str(i).replace("('",'').replace("',)", '')
                        if x == 4 or x == 8 or x == 12 or x == 16 or x == 20:
                            keyboard.add_line()
                            keyboard.add_button(i, color=VkKeyboardColor.DEFAULT)
                            n += 1
                        else:
                            keyboard.add_button(i, color=VkKeyboardColor.DEFAULT)
                            n += 1
                    vk.messages.send(user_id='254928937', random_id='0',keyboard=keyboard.get_keyboard(),
                                     message='Дай ссылку на инвентарь')
                    flag = False
            user = sql.execute(f'SELECT user FROM users WHERE user = "{event.text}"')
            if user.fetchone() is None:
                pass
            else:
                sql.execute(f'SELECT * FROM users WHERE user = "{event.text}"')
                result = sql.fetchall()
                url = result[0][2]
                package.get(url)
                keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
                n = 0
                for i in package.game_mass:
                    if n == 4 or n == 8 or n == 12 or n == 16 or n == 20:
                        keyboard.add_line()
                        keyboard.add_button(package.game_mass[n], color=VkKeyboardColor.DEFAULT)
                        n += 1
                    else:
                        keyboard.add_button(package.game_mass[n], color=VkKeyboardColor.DEFAULT)
                        n += 1
                keyboard.add_line()
                keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
                vk.messages.send(user_id=user_id,
                                 keyboard=keyboard.get_keyboard(),
                                 random_id='0',
                                 message='Выберите игру')
                for event_1 in longpoll.listen():
                    if event_1.type == VkEventType.MESSAGE_NEW:
                        if event_1.text in package.game_mass:
                            index = package.game_mass.index(event_1.text)
                            if int(package.number_mass[index]) == 1:
                                vk.messages.send(user_id=user_id, random_id='0',
                                                 keyboard=keyboard.get_keyboard(),
                                                 message=f'Сейчас в инвентаре {package.number_mass[index]} предмет.')
                            elif int(package.number_mass[index]) <= 4:
                                vk.messages.send(user_id=user_id, random_id='0',
                                                 keyboard=keyboard.get_keyboard(),
                                                 message=f'Сейчас в инвентаре {package.number_mass[index]} предмета.')
                            else:
                                vk.messages.send(user_id=user_id, random_id='0',
                                                 keyboard=keyboard.get_keyboard(),
                                                 message=f'Сейчас в инвентаре {package.number_mass[index]} предметов.')
                        if event_1.text == 'Назад':
                            flag = True
                            if flag:
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
                    sql.execute('SELECT user FROM users')
                    result = sql.fetchall()
                    x = 0
                    for i in result:
                        i = str(i).replace("('", '').replace("',)", '')
                        if x == 4 or x == 8 or x == 12 or x == 16 or x == 20:
                            keyboard.add_line()
                            keyboard.add_button(i, color=VkKeyboardColor.DEFAULT)
                            x += 1
                        else:
                            keyboard.add_button(i, color=VkKeyboardColor.DEFAULT)
                            x += 1
                    vk.messages.send(user_id='254928937', random_id='0', keyboard=keyboard.get_keyboard(),
                                     message='Дай ссылку на инвентарь')
                    flag = False
        except Exception:
            keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
            sql.execute('SELECT user FROM users')
            result = sql.fetchall()
            x = 0
            for i in result:
                i = str(i).replace("('", '').replace("',)", '')
                if x == 4 or x == 8 or x == 12 or x == 16 or x == 20:
                    keyboard.add_line()
                    keyboard.add_button(i, color=VkKeyboardColor.DEFAULT)
                    x += 1
                else:
                    keyboard.add_button(i, color=VkKeyboardColor.DEFAULT)
                    x += 1
            try:
                vk.messages.send(user_id='254928937', random_id='0', keyboard=keyboard.get_keyboard(),
                                 message='Случилась ошибка')
            except Exception:
                print(Exception)
