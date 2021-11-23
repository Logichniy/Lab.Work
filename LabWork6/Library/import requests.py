class Library(object):

    def __init__(self, name, author, year_of_publication, genre):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication
        self.genre = genre

    def book(self):
        print(self.name, self.author, self.year_of_publication, self.genre)


book1 = ("The Daily Life of the Immortal King", "Ku Xuan", "2020", "Novel")
book2 = ("Overgeared", "Park Saenal", "2014", "Manga")
book3 = ("The Beginning After the End", "TurtleMe", "2015", "Ranobe")
book4 = ("Solo Leveling", "Chugong", "2016", "Manhwa")

print("Ви відкрили домашню бібліотеку.")

while True:
    print("1. Бібліотека.\n2. Пошук.\n3. Додати книгу до бібліотеки.\n4. Видалити книгу.\n5. Вийти із бібліотеки.\n")
    userInput = str(input())

    if userInput == "1":
        print(book1)
        print(book2)
        print(book3)
        print(book4)

    elif userInput == "2":
        while True:
            choice = input("Пошук книги за допомогою...\n1. name.\n2. author.\n3. year_of_publication.\n4. genre.\n")
            if choice == "1":
                while True:
                    choice = input("ВВедіть дані для пошуку.\n")
                    if choice == 'The Daily Life of the Immortal King':
                        print("The Daily Life of the Immortal King, Ku Xuan, 2020, Novel")
                    else:
                        print("ВВедіть дані для пошуку.")
                        if choice == "Overgeared":
                            print("Overgeared, Park Saenal, 2014, Manga")
                        elif choice == "The Beginning After the End":
                            print("The Beginning After the End, TurtleMe, 2015, Ranobe")
                        elif choice == "Solo Leveling":
                            print("Solo Leveling, Chugong, 2016, Manhwa")
            if choice == "2":
                while True:
                    choice = input("ВВедіть дані для пошуку.\n")
                    if choice == "Ku Xuan":
                        print("The Daily Life of the Immortal King, 2020, Novel")
                    else:
                        print("ВВедіть дані для пошуку.")
                        if choice == "Park Saenal":
                            print("Overgeared, 2014, Manga")
                        elif choice == "TurtleMe":
                            print("The Beginning After the End, 2015, Ranobe")
                        elif choice == "Chugong":
                            print("Solo Leveling, 2016, Manhwa")
            if choice == "3":
                while True:
                    choice = input("ВВедіть дані для пошуку.\n")
                    if choice == "2020":
                        print("The Daily Life of the Immortal King, Ku Xuan, Novel")
                    else:
                        print("ВВедіть дані для пошуку.")
                        if choice == "2014":
                            print("Overgeared, Park Saenal, Manga")
                        elif choice == "2015":
                            print("The Beginning After the End, TurtleMe, Ranobe")
                        elif choice == "2016":
                            print("Solo Leveling, Chugong, Manhwa")
            if choice == "4":
                while True:
                    choice = input("ВВедіть дані для пошуку.\n")
                    if choice == "Novel":
                        print("The Daily Life of the Immortal King, Ku Xuan, 2020")
                    else:
                        print("ВВедіть дані для пошуку.")
                        if choice == "Manga":
                            print("Overgeared, Park Saenal, 2014")
                        elif choice == "Ranobe":
                            print("The Beginning After the End, TurtleMe, 2015")
                        elif choice == "Manhwa":
                            print("Solo Leveling, Chugong, 2016")
    elif userInput == "3":
        print("Додайте книгу.")
        filename = input()
        print("Операція успішна.")
    elif userInput == "4":
        import os
        os.remove(" C:\\mydoc.doc \\testfile.txt")
    elif userInput == "5":
        break