product_catalog = {"продукт1": 10, "продукт2": 20, "продукт3": 30}
cart = []
admin_username = "Admin"
admin_password = "Admin"
current_user = None
while True:
    print("\nМеню:")
    print("1. Реєстрація")
    print("2. Увійти як адміністратор")
    print("3. Додати продукт до кошика")
    print("4. Введіть кількістьт товару")
    print("5. Завершити покупку та розрахуватися")
    print("6. Вийти")
    choice = input("Оберіть опцію: ")
    if choice == "1":
        username = input("Введіть ім'я користувача: ")
        password = input("Введіть пароль: ")
        current_user = (username, password)
    elif choice == "2":
        product_catalog = {
            "headphone": 4000,
            "charge": 500,
            "TV": 40000,
            "iphone": 20000,
            "android": 15800,
            "laptop": 36000
        }
        cart = []
        admin_username = "Admin"
        admin_password = "Admin"
        current_user = None
        while True:
            print("\nМеню:")
            print("1. Реєстрація")
            print("2. Увійти як адміністратор")
            print("3. Додати продукт до кошика")
            print("4. Завершити покупку та розрахуватися")
            print("5. Вийти")
            choice = input("Оберіть опцію: ")
            if choice == "1":
                username = input("Введіть ім'я користувача: ")
                password = input("Введіть пароль: ")
                current_user = (username, password)
            elif choice == "2":
                username = input("Введіть ім'я користувача: ")
                password = input("Введіть пароль: ")
                if username == admin_username and password == admin_password:
                    current_user = (username, password)
                    print("Успішно увійшли як адміністратор.")
                else:
                    print("Невірний логін або пароль.")
            elif choice == "3":
                product_name = input("Введіть назву продукту, який додаєте в кошик: ")
                if product_name in product_catalog:
                    cart.append((product_name, product_catalog[product_name]))
                    print(f"'{product_name}' додано до кошика.")
                else:
                    print("Продукт не знайдено в каталозі.")
            elif choice == "4":
                if not current_user:
                    print("Спершу увійдіть у систему.")
                elif not cart:
                    print("Кошик порожній.")
                else:
                    total_price = sum(item[1] for item in cart)
                    print(f"Загальна сума до оплати: {total_price} грн")
                    cart = []
            elif choice == "5":
                print("До побачення!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")