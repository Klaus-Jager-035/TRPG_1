import os
# TO DO: Доделать меню

library = [
    {
        "название": "Введение в Python. Том 1",
        "автор": "Марк Лутц",
        "год издания": 2022
    },
    {
        "название": "Введение в Python. Том 2",
        "автор": "Марк Лутц",
        "год издания": 2022
    }
]


def show_menu():

    options = [
        "- Показать все книги",
        "- Добавить книгу",
        "- Удалить книгу",
        "- Поиск по порядковому номеру",
        "- Поиск по названию",
        "- Поиск по автору",
        "- Поиск по году",
        "- Выход"
    ]
    while True:
        os.system("cls")

        for num, option in enumerate(options, 1):
            print(num, option)

        option = input("Введите номер варианта: ")

        if option == "1":
            return show_books()
        elif option == "2":
            return add_book()
        elif option == "3":
            return remove_book()
        elif option == "4":
            return search_by_number()
        elif option == "5":
            return search_book_by_key("название")
        elif option == "6":
            return search_book_by_key("автор")
        elif option == "7":
            return search_book_by_key("год издания")
        elif option == "8":
            return



def show_books():
    os.system("cls")
    if not library:
        return

    for num, book in enumerate(library, 1):
        print("номер на полке: ", num)
        print("название: ", book["название"], "\n"
            "автор: ", book["автор"], "\n"
            "год издания: ", book["год издания"], "\n"
            "")
        print("")

def find_book():
    os.system("cls")
    choice_1 = ("1 - Введите название для поиска по названию:",  "\n"
    "2 - Введите автора для поиска по имени автора:", "\n"
    "3 - Введите год издания для поиска по году: ", "\n"
    "4 - Выход")

    for book in library():
        if choice_1 == ["название"]:
            print("название: ", book["название"], "\n"
            "автор: ", book["автор"], "\n"
            "год издания: ", book["год издания"], "\n"
            "")
        elif choice_2 == ["автор"]:
            print("название: ", book["название"], "\n"
            "автор: ", book["автор"], "\n"
            "год издания: ", book["год издания"], "\n"
            "")
        elif choice_3 == ["год издания"]:
            print("название: ", book["название"], "\n"
            "автор: ", book["автор"], "\n"
            "год издания: ", book["год издания"], "\n"
            "")

def add_book():
    os.system("cls")
    title = input("Введите название книги: ")
    if not title:
        print("Ошибка! Нет названия.")
        return

    author = input("Введите имя автора книги: ")
    if not author:
        print("Ошибка! Нет автора.")
        return


    year = input("Введите год издания книги: ")
    if not year:
        print("Ошибка! Нет года издания.")
        return
    if year.isdigit():
        year = int(year)
    else:
        print("Ошибка! Год должен быть целым числом.")
        return

    book = {
        "название": title,
        "автор": author,
        "год издания": year,
    }

    if book in library:
        print("Ошибка, такая книга уже есть!")
        return

    library.append(book)
    print("Книга", book["название"], "добавлена в библиотеку")


def remove_book() -> None:
    """ удаляет книгу из библиотеки по порядковму номеру ( >0 ) """

    os.system("cls")
    num = input("Введите номер книги для удаления: ")

    if not num.isdigit():
        print("Номер должен быть целым положительным числом")
        return
    else:
       num = int(num)

    idx = num -1

    if idx < 0:
        print("Номер должен быть целым положительным числом")
        return

    if idx > len(library) - 1:
        print("Нет такой книги")
        return

    print(f"Книга {library[idx]} удалена")
    library.pop(idx)


def search_by_number():

    os.system("cls")
    if not library:
        print("В библиотеке нет книг")
        return

    number = input("Введите номер книги: ")
    if not number.isdigit():
        print("Номер должен быть числом")
        return

    number = int(number)
    idx = number - 1

    if idx < 0:
        print("Номер должен быть положительным")
        return

    if idx >= len(library):
        print("Номер слишком большой, нет книги с таким номером")
        return

    book = library[idx]

    print("номер на полке: ", number)
    print("название: ", book["название"], "\n"
            "автор: ", book["автор"], "\n"
            "год издания: ", book["год издания"], "\n"
            "")
    print("")

def search_book_by_key(user_key: str) -> None:
    """ Показывает на экране книгу, если находит её по порядковому номеру"""
    os.system("cls")
    if not library:
        print("Библиотека пуста")
        return

    user_value = input(f"Введите {user_key}: ")

    if not user_value:
        print("Нет данных для поиска")
        return

    if user_key == "год издания":
        if user_value.isdigit():
            user_value = int(user_value)

    for book in library:
        if book[user_key] == user_value:
            print(f'номер на полке: {library.index(book) + 1}')
            print(f'название: {book["название"]}')
            print(f'автор: {book["автор"]}')
            print(f'год издания: {book["год издания"]}')
            print("")


show_menu()
