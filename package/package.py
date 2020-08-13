import requests
from bs4 import BeautifulSoup

url = ''
game_mass = []
number_mass = []
name = ''

def get(url):
    if url != 'Дай ссылку на инвентарь':
        global game_mass, number_mass,name
        game_mass.clear()
        number_mass.clear()
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'html.parser')
        game_list = soup.find_all('span', class_='games_list_tab_name')
        number = soup.find_all('span', class_='games_list_tab_number')
        name = soup.find('a',class_='whiteLink persona_name_text_content').get_text(strip=True)
        print(name)
        for i in game_list:
            game_mass.append(i.get_text())
        print(game_mass)
        for x in number:
            number_mass.append(int(x.get_text().replace('(','').replace(')','')))
        print(number_mass)



















'''                 keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
                    keyboard.add_button('Стим', color=VkKeyboardColor.DEFAULT)
                    keyboard.add_button('Погода', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_button('Подписка', color=VkKeyboardColor.POSITIVE)
                    keyboard.add_button('Оповещения', color=VkKeyboardColor.POSITIVE)
                    vk.messages.send(user_id=event.user_id, keyboard=keyboard.get_keyboard(), random_id='0',
                                     message='Главное меню')'''