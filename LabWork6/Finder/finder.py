import requests
from bs4 import BeautifulSoup
print("Аналіз сайту.")

while True:
    print("1. Перевірка існування сайту.\n1. Показ сайту.\n2. Аналіз контенту.\n3. Вихід.\4")
    userInput = str(input())

    if userInput == "1":
        print("Введіть URL-адресу.")
        userInput1 = str(input())

        try:
            r = requests.get(userInput1)
            if r.ok:
                print("Сайт з цією URL-адресою існує.")
            else:
                print("Такого сайту не існує.")
        except:
            print("Недійсна URL-адреса.")
    elif userInput == "2":
        print("Введіть URL-адресу.")
        userInput2 = str(input())

        try:
            r = requests.get(userInput2)
            if r.ok:
                def pause(url):
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    return soup
                page = pause(url)
                content = page.find('div', 'content-article')



                def inside():
                    i = 0
                    for _ in content.find_all('a', href = True):
                        i+=1
                        text = page.find('div', 'content_article').text
                        words = len(text.split())
                        img = len([tag.name for tag in page.find_all('img')])
                        links = len([tag.name for tag in page.find_all('link')])
                        tags = len([tag.name for tag in page.find_all()])
                    print("Слів у тексті:")
                    print('Слів', words)
                    print('Картинок', img)
                    print("Тегів", tags)
                    print('Посилань', links)
                print(inside())

            else:
                print("Такого сайту не існує.")
        except:
            print("Недійсна URL-адреса.")

    elif userInput == "3":

        print("Введіть URL-адресу.")
        userInput2 = str(input())
        try:
            r = requests.get(userInput2)
            if r.ok:
                pass ##########################
            else:
                print("Can`t reach a site with entered url (404)")

        except:
            print("Такого сайту не існує.")
    else:
        print("Error 404")