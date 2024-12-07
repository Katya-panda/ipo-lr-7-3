import json # импортируем модуль json для работы с json файлами
def load_data():
    with open('cars.json', 'r', encoding='utf-8') as file: # открываем файл cars.json для чтения с кодировкой UTF-8
        return json.load(file) # загружаем данные из файла и возвращаем их
def save_data(data):
    with open('cars.json', 'w', encoding='utf-8') as file: # открываем файл cars.json для записи с кодировкой UTF-8
        json.dump(data, file, ensure_ascii=False, indent=4) # сохраняем данные в файл в формате JSON
def show_all_records():
    for record in load_data(): # загружаем данные и проходим по всем записям
        print(json.dumps(record, ensure_ascii=False, indent=4)) # выводим каждую запись в формате JSON
def show_record_by_id():
    record_id = int(input("Введите ID: ")) # запрашиваем у пользователя ID записи
    for record in load_data(): # загружаем данные и проходим по всем записям
        if record['id'] == record_id: # если найден нужный ID
            print(json.dumps(record, ensure_ascii=False, indent=4)) # выводим запись в формате JSON
            return # выходим из функции, если запись найдена
    print("Запись не найдена") # сообщение, если запись не найдена
def add_record():
    data = load_data() # загружаем данные из файла
    data.append({ # добавляем новую запись, запрашивая данные у пользователя
        'id': int(input("Введите ID: ")), # запрашиваем у пользователя ID
        'name': input("Введите название модели: "), # запрашиваем у пользователя название модели
        'manufacturer': input("Введите производителя: "), # запрашиваем у пользователя название производителя
        'is_petrol': input("Заправляется ли машина бензином (True/False): ").lower() == 'true', # запрашиваем у пользователя тип топлива
        'tank_volume': int(input("Введите объем бака: ")) # запрашиваем у пользователя объем бака
    })
    save_data(data) # сохраняем обновленные данные в файл
    print("Запись добавлена") # выводим сообщение о добавлении записи
def delete_record_by_id():
    record_id = int(input("Введите ID: ")) # запрашиваем у пользователя ID записи
    data = load_data() # загружаем данные из файла
    for record in data: # проходим по всем записям
        if record['id'] == record_id: # если найден нужный ID
            data.remove(record) # удаляем запись из данных
            save_data(data) # сохраняем обновленные данные в файл
            print("Запись удалена") # выводим сообщение об удалении записи
            return # выходим из функции, если запись найдена и удалена
    print("Запись не найдена") # сообщение, если запись не найдена
operations_count = 0 # инициализируем переменную для подсчета операций
while True:
    # выводим меню
    print("\nМеню:\n1. Вывести все записи\n2. Вывести запись по ID\n3. Добавить запись\n4. Удалить запись по ID\n5. Выйти из программы")
    choice = input("Выберите пункт меню: ") # Запрашиваем выбор пользователя
    # обрабатываем выбор пользователя
    if choice == '1':
        show_all_records() # вывод всех записей
    elif choice == '2':
        show_record_by_id() # вывод записи по ID
    elif choice == '3':
        add_record() # добавление новой записи
    elif choice == '4':
        delete_record_by_id() # удаление записи по ID
    elif choice == '5':
        print(f"Количество выполненных операций: {operations_count}") # вывод количества выполненных операций
        break # выход из программы
    else:
        print("Неверный выбор. Попробуйте снова.") # сообщение о неверном выборе
    operations_count += 1 # увеличиваем счетчик операций
