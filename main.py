import json # импортируем модуль json для работы с json файлами
# начальные данные с 5 записями
data = [
    {"id": 1, "name": "Model S", "manufacturer": "Tesla", "is_petrol": False, "tank_volume": 100},
    {"id": 2, "name": "Mustang", "manufacturer": "Ford", "is_petrol": True, "tank_volume": 60},
    {"id": 3, "name": "Civic", "manufacturer": "Honda", "is_petrol": True, "tank_volume": 50},
    {"id": 4, "name": "Corolla", "manufacturer": "Toyota", "is_petrol": True, "tank_volume": 55},
    {"id": 5, "name": "Leaf", "manufacturer": "Nissan", "is_petrol": False, "tank_volume": 0}
]
# сохраняем начальные данные в файл
with open('cars.json', 'w', encoding='utf-8') as file: # открываем файл cars.json для записи с кодировкой utf-8
    json.dump(data, file, ensure_ascii=False, indent=4) # записываем данные в файл в формате json
# переменная для подсчета выполненных операций
operations_count = 0 # инициализируем переменную для подсчета операций
while True: # основной цикл программы
    print("\nМеню:") # выводим меню
    print("1. Вывести все записи") # пункт меню 1
    print("2. Вывести запись по полю") # пункт меню 2
    print("3. Добавить запись") # пункт меню 3
    print("4. Удалить запись по полю") # пункт меню 4
    print("5. Выйти из программы") # пункт меню 5
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
        record_id = int(input("Введите ID: ")) # запрашиваем у пользователя id записи
        # считываем данные из файла
        with open('cars.json', 'r', encoding='utf-8') as file: # открываем файл cars.json для чтения
            data = json.load(file) # загружаем данные из файла в переменную data
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
        new_record['id'] = int(input("Введите ID: ")) # запрашиваем у пользователя id
        new_record['name'] = input("Введите название модели: ") # запрашиваем у пользователя название модели
        new_record['manufacturer'] = input("Введите название производителя: ") # запрашиваем у пользователя название производителя
        new_record['is_petrol'] = input("Заправляется ли машина бензином (True/False): ").lower() == 'true' # запрашиваем у пользователя тип топлива
        new_record['tank_volume'] = int(input("Введите объем бака в литрах: ")) # запрашиваем у пользователя объем бака
        data.append(new_record) # добавляем новую запись в data
        # сохраняем обновленные данные в файл
        with open('cars.json', 'w', encoding='utf-8') as file: # открываем файл cars.json для записи
            json.dump(data, file, ensure_ascii=False, indent=4) # записываем данные в файл в формате json
        print("Запись добавлена") # выводим сообщение
        operations_count += 1 # увеличиваем счетчик операций
    elif choice == '4': # если выбран пункт 4
        record_id = int(input("Введите ID: "))
        # считываем данные из файла
        with open('cars.json', 'r', encoding='utf-8') as file: # открываем файл cars.json для чтения
            data = json.load(file) # загружаем данные из файла в переменную data
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