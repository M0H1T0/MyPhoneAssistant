def language_selection():
    print("Choose your language/Выберите ваш язык")
    print("English(en)/Русский(ru/ру)")
    user_language = input(">>> ")
    lang = user_language
    if lang == "en" or lang == "En" or lang == "EN":
        en_main_menu()

    elif lang == "ru" or lang == "Ru" or lang == "RU" or lang == "ру" or lang == "Ру" or lang == "РУ":
        ru_main_menu()



    def en_main_menu():
        print("hello")


    def ru_main_menu():
        print("Привет")