import json  # импортируем модуль json для работы с json файлами
def save_initial_data():
    data = [
        {"id": 1, "name": "Model S", "manufacturer": "Tesla", "is_petrol": False, "tank_volume": 100},
        {"id": 2, "name": "Mustang", "manufacturer": "Ford", "is_petrol": True, "tank_volume": 60},
        {"id": 3, "name": "Civic", "manufacturer": "Honda", "is_petrol": True, "tank_volume": 50},
        {"id": 4, "name": "Corolla", "manufacturer": "Toyota", "is_petrol": True, "tank_volume": 55},
        {"id": 5, "name": "Leaf", "manufacturer": "Nissan", "is_petrol": False, "tank_volume": 0}
    ]
    with open('cars.json', 'w', encoding='utf-8') as file:  # открываем файл cars.json для записи с кодировкой utf-8
        json.dump(data, file, ensure_ascii=False, indent=4)  # записываем данные в файл в формате json
def load_data():
    with open('cars.json', 'r', encoding='utf-8') as file:  # открываем файл cars.json для чтения с кодировкой utf-8
        return json.load(file)  # загружаем данные из файла и возвращаем их
def save_data(data):
    with open('cars.json', 'w', encoding='utf-8') as file:  # открываем файл cars.json для записи с кодировкой utf-8
        json.dump(data, file, ensure_ascii=False, indent=4)  # записываем данные в файл в формате json
def show_all_records():
    data = load_data()  # загружаем данные из файла
    for record in data:  # проходим по всем записям в данных
        print(json.dumps(record, ensure_ascii=False, indent=4))  # выводим каждую запись в формате json
def show_record_by_id():
    record_id = int(input("Введите ID: "))  # запрашиваем у пользователя id записи
    data = load_data()  # загружаем данные из файла
    for index, record in enumerate(data):  # проходим по всем записям в данных
        if record['id'] == record_id:  # если id записи совпадает с введенным
            print(f"Позиция в словаре: {index}")  # выводим позицию записи в списке
            print(json.dumps(record, ensure_ascii=False, indent=4))  # выводим запись в формате json
            return  # выходим из функции
    print("Запись не найдена")  # если запись не найдена, выводим сообщение
def add_record():
    data = load_data()  # загружаем данные из файла
    new_record = {
        'id': int(input("Введите ID: ")),  # запрашиваем у пользователя id
        'name': input("Введите название модели: "),  # запрашиваем у пользователя название модели
        'manufacturer': input("Введите название производителя: "),  # запрашиваем у пользователя название производителя
        'is_petrol': input("Заправляется ли машина бензином (True/False): ").lower() == 'true',  # запрашиваем у пользователя тип топлива
        'tank_volume': int(input("Введите объем бака в литрах: "))  # запрашиваем у пользователя объем бака
    }
    data.append(new_record)  # добавляем новую запись в данные
    save_data(data)  # сохраняем обновленные данные в файл
    print("Запись добавлена")  # выводим сообщение о добавлении записи
def delete_record_by_id():
    record_id = int(input("Введите ID: "))  # запрашиваем у пользователя id записи
    data = load_data()  # загружаем данные из файла
    for index, record in enumerate(data):  # проходим по всем записям в данных
        if record['id'] == record_id:  # если id записи совпадает с введенным
            del data[index]  # удаляем запись из данных
            save_data(data)  # сохраняем обновленные данные в файл
            print("Запись удалена")  # выводим сообщение об удалении записи
            return  # выходим из функции
    print("Запись не найдена")  # если запись не найдена, выводим сообщение
# Основная логика программы
save_initial_data()  # сохраняем начальные данные перед запуском программы
operations_count = 0  # инициализируем переменную для подсчета операций
while True:  # основной цикл программы
    print("\nМеню:")  # выводим меню
    print("1. Вывести все записи")  # пункт меню 1
    print("2. Вывести запись по полю")  # пункт меню 2
    print("3. Добавить запись")  # пункт меню 3
    print("4. Удалить запись по полю")  # пункт меню 4
    print("5. Выйти из программы")  # пункт меню 5
    choice = input("Выберите пункт меню: ")  # запрашиваем выбор пользователя
    if choice == '1':  # если выбран пункт 1
        show_all_records()  # вызываем функцию для вывода всех записей
        operations_count += 1  # увеличиваем счетчик операций
    elif choice == '2':  # если выбран пункт 2
        show_record_by_id()  # вызываем функцию для вывода записи по id
        operations_count += 1  # увеличиваем счетчик операций
    elif choice == '3':  # если выбран пункт 3
        add_record()  # вызываем функцию для добавления новой записи
        operations_count += 1  # увеличиваем счетчик операций
    elif choice == '4':  # если выбран пункт 4
        delete_record_by_id()  # вызываем функцию для удаления записи по id
        operations_count += 1  # увеличиваем счетчик операций
    elif choice == '5':  # если выбран пункт 5
        print(f"Количество выполненных операций: {operations_count}")  # выводим количество выполненных операций
        break  # выходим из цикла, завершая программу
    else:  # если выбран неверный пункт
        print("Неверный выбор. Попробуйте снова.")  # выводим сообщение об ошибке