import json # импортируем модуль json для работы с json файлами
# переменная для подсчета выполненных операций
operations_count = 0 # инициализируем переменную для подсчета операций
while True: # основной цикл программы
 # выводим меню
    print("\nМеню:\n1. Вывести все записи\n2. Вывести запись по ID\n3. Добавить запись\n4. Удалить запись по ID\n5. Выйти из программы")
    choice = input("Выберите пункт меню: ") # запрашиваем выбор пользователя
    if choice == '1': # если выбран пункт 1
        # считываем данные из файла
        with open('cars.json', 'r', encoding='utf-8') as file: # открываем файл cars.json для чтения
            data = json.load(file) # загружаем данные из файла в переменную data
        # выводим все записи
        for record in data: # проходим по всем записям в data
            print(json.dumps(record, ensure_ascii=False, indent=4)) # выводим запись в формате json
        operations_count += 1 # увеличиваем счетчик операций
    elif choice == '2': # если выбран пункт 2
        # считываем данные из файла
        with open('cars.json', 'r', encoding='utf-8') as file: # открываем файл cars.json для чтения
            data = json.load(file) # загружаем данные из файла в переменную data
            record_id = int(input("Введите ID: ")) # запрашиваем у пользователя id записи
        # ищем запись по id
        found = False # флаг для обозначения нахождения записи
        for index, record in enumerate(data): # проходим по всем записям в data
            if record['id'] == record_id: # если id записи совпадает с введенным
                print(f"Позиция в словаре: {index}") # выводим позицию записи в словаре
                print(json.dumps(record, ensure_ascii=False, indent=4)) # выводим запись в формате json
                found = True # устанавливаем флаг в True
                break # прекращаем поиск
        if not found: # если запись не найдена
            print("Запись не найдена") # выводим сообщение
        operations_count += 1 # увеличиваем счетчик операций
    elif choice == '3': # если выбран пункт 3
        # считываем данные из файла
        with open('cars.json', 'r', encoding='utf-8') as file: # открываем файл cars.json для чтения
            data = json.load(file) # загружаем данные из файла в переменную data
        # добавляем новую запись
        new_record = {} # создаем новый словарь для новой записи
        data.append(new_record) # добавляем новую запись в data
        # сохраняем обновленные данные в файл
        with open('cars.json', 'w', encoding='utf-8') as file: # открываем файл cars.json для записи
            json.dump(data, file, ensure_ascii=False, indent=4) # записываем данные в файл в формате json
        print("Запись добавлена") # выводим сообщение
        operations_count += 1 # увеличиваем счетчик операций
    elif choice == '4': # если выбран пункт 4
        # считываем данные из файла
        with open('cars.json', 'r', encoding='utf-8') as file: # открываем файл cars.json для чтения
            data = json.load(file) # загружаем данные из файла в переменную data
        record_id = int(input("Введите ID: "))
        # ищем и удаляем запись по id
        found = False # флаг для обозначения нахождения записи
        for index, record in enumerate(data): # проходим по всем записям в data
            if record['id'] == record_id: # если id записи совпадает с введенным
                del data[index] # удаляем запись из data
                found = True # устанавливаем флаг в True
                break # прекращаем поиск
        if found: # если запись найдена
            # сохраняем обновленные данные в файл
            with open('cars.json', 'w', encoding='utf-8') as file: # открываем файл cars.json для записи
                json.dump(data, file, ensure_ascii=False, indent=4) # записываем данные в файл в формате json
            print("Запись удалена") # выводим сообщение
        else: # если запись не найдена
            print("Запись не найдена") # выводим сообщение
        operations_count += 1 # увеличиваем счетчик операций
    elif choice == '5': # если выбран пункт 5
        print(f"Количество выполненных операций: {operations_count}") # выводим количество выполненных операций
        break # прекращаем поиск
    else: # если выбран неверный пункт
        print("Неверный выбор. Попробуйте снова.") # выводим сообщение
