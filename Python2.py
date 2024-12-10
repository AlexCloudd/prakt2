from functools import reduce

users = [
    {'username': 'alex_user', 'password': 'password123', 'role': 'user', 'subscription_type': 'Premium', 'history': [], 'created_at': '2024-01-15'},
    {'username': 'admin_user', 'password': 'adminpass', 'role': 'admin', 'history': [], 'created_at': '2024-01-10'}
]

services = [
    {'name': 'Йога', 'price': 1000, 'duration': 60, 'popularity': 5},
    {'name': 'Силовая тренировка', 'price': 1200, 'duration': 90, 'popularity': 4},
    {'name': 'Плавание', 'price': 800, 'duration': 60, 'popularity': 3}
]

def login():
    print("Добро пожаловать в фитнес-клуб!")
    username = input("Логин: ")
    password = input("Пароль: ")

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if user:
        print(f"Добро пожаловать, {user['username']}!")
        return user
    else:
        print("Неверный логин или пароль.")
        return None

def display_services(services_list):
    for i, service in enumerate(services_list, start=1):
        print(f"{i}. {service['name']} | Цена: {service['price']} | Время: {service['duration']} мин | Популярность: {service['popularity']}")

def sort_services_by_price(services_list):
    sorted_services = sorted(services_list, key=lambda x: x['price'])
    display_services(sorted_services)

def sort_services_by_popularity(services_list):
    sorted_services = sorted(services_list, key=lambda x: x['popularity'], reverse=True)
    display_services(sorted_services)

def filter_services_by_price(services_list, min_price):
    filtered_services = list(filter(lambda service: service['price'] >= min_price, services_list))
    if filtered_services:
        display_services(filtered_services)
    else:
        print("Нет услуг, соответствующих указанной цене.")

def map_services_price_in_euros(services_list, exchange_rate=0.011):
    mapped_services = map(lambda x: {**x, 'price': round(x['price'] * exchange_rate, 2)}, services_list)
    display_services(list(mapped_services))

def user_menu(user):
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть доступные услуги")
        print("2. Записаться на услугу")
        print("3. Посмотреть историю записей")
        print("4. Сортировать услуги по цене")
        print("5. Сортировать услуги по популярности")
        print("6. Фильтровать услуги по цене")
        print("7. Преобразовать цену в евро")
        print("8. Изменить пароль")
        print("9. Выйти")

        choice = input("Введите номер действия: ")
        if choice == '1':
            display_services(services)
        elif choice == '2':
            try:
                service_index = int(input("Выберите услугу по номеру: ")) - 1
                if 0 <= service_index < len(services):
                    user['history'].append(services[service_index]['name'])
                    print(f"Вы записаны на услугу: {services[service_index]['name']}")
                else:
                    print("Неверный номер услуги.")
            except ValueError:
                print("Введите корректный номер услуги.")
        elif choice == '3':
            print("История ваших записей:", ", ".join(user['history']))
        elif choice == '4':
            sort_services_by_price(services)
        elif choice == '5':
            sort_services_by_popularity(services)
        elif choice == '6':
            min_price = int(input("Введите цену (минимальная цена 800): "))
            filter_services_by_price(services, min_price)
        elif choice == '7':
            map_services_price_in_euros(services)
        elif choice == '8':
            new_password = input("Введите новый пароль: ")
            user['password'] = new_password
            print("Пароль успешно изменен!")
        elif choice == '9':
            break
        else:
            print("Неверный ввод.")

def admin_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить услугу")
        print("2. Удалить услугу")
        print("3. Редактировать услугу")
        print("4. Управление пользователями")
        print("5. Просмотр статистики")
        print("6. Выйти")

        choice = input("Введите номер действия: ")
        if choice == '1':
            name = input("Введите название услуги: ")
            price = int(input("Введите цену: "))
            duration = int(input("Введите продолжительность: "))
            popularity = int(input("Введите популярность: "))
            services.append({'name': name, 'price': price, 'duration': duration, 'popularity': popularity})
            print("Услуга успешно добавлена.")
        elif choice == '2':
            try:
                service_index = int(input("Выберите услугу для удаления: ")) - 1
                if 0 <= service_index < len(services):
                    del services[service_index]
                    print("Услуга успешно удалена.")
                else:
                    print("Неверный номер услуги.")
            except ValueError:
                print("Введите корректный номер услуги.")
        elif choice == '3':
            try:
                service_index = int(input("Выберите услугу для редактирования: ")) - 1
                if 0 <= service_index < len(services):
                    name = input("Новое название услуги: ")
                    price = int(input("Новая цена: "))
                    duration = int(input("Новая продолжительность: "))
                    popularity = int(input("Новая популярность: "))
                    services[service_index] = {'name': name, 'price': price, 'duration': duration, 'popularity': popularity}
                    print("Услуга успешно обновлена.")
                else:
                    print("Неверный номер услуги.")
            except ValueError:
                print("Введите корректный номер услуги.")
        elif choice == '4':
            manage_users()
        elif choice == '5':
            print("Статистика по услугам:")
            print(f"Всего услуг: {len(services)}")
            average_price = reduce(lambda x, y: x + y, [s['price'] for s in services]) / len(services)
            print(f"Средняя цена услуги: {average_price:.2f}")
            most_popular_service = max(services, key=lambda x: x['popularity'])
            print(f"Самая популярная услуга: {most_popular_service['name']} с рейтингом {most_popular_service['popularity']}")
        elif choice == '6':
            break
        else:
            print("Неверный ввод.")

def manage_users():
    while True:
        print("\nУправление пользователями:")
        print("1. Создать пользователя")
        print("2. Удалить пользователя")
        print("3. Редактировать пользователя")
        print("4. Вернуться в меню администратора")

        choice = input("Введите номер действия: ")
        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            role = input("Введите роль (user/admin): ")
            subscription_type = input("Введите тип подписки (если есть): ")
            users.append({'username': username, 'password': password, 'role': role, 'subscription_type': subscription_type, 'history': [], 'created_at': '2024-12-01'})
            print(f"Пользователь {username} успешно создан.")
        elif choice == '2':
            username = input("Введите имя пользователя для удаления: ")
            user_to_delete = next((u for u in users if u['username'] == username), None)
            if user_to_delete:
                users.remove(user_to_delete)
                print(f"Пользователь {username} удален.")
            else:
                print("Пользователь не найден.")
        elif choice == '3':
            username = input("Введите имя пользователя для редактирования: ")
            user_to_edit = next((u for u in users if u['username'] == username), None)
            if user_to_edit:
                new_password = input("Введите новый пароль: ")
                new_role = input("Введите новую роль (user/admin): ")
                new_subscription = input("Введите новый тип подписки: ")
                user_to_edit['password'] = new_password
                user_to_edit['role'] = new_role
                user_to_edit['subscription_type'] = new_subscription
                print(f"Пользователь {username} успешно обновлен.")
            else:
                print("Пользователь не найден.")
        elif choice == '4':
            break
        else:
            print("Неверный ввод.")

def main():
    user = login()
    if user:
        if user['role'] == 'user':
            user_menu(user)
        elif user['role'] == 'admin':
            admin_menu()

if __name__ == "__main__":
    main()
