# . Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"added product '{item_name}': {price}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён")
        else:
            print(f"Товар '{item_name}' не найден")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на '{item_name}' обновлена до {new_price}")
        else:
            print(f"Товар '{item_name}' не найден")

# Создание 3 объектов(экземпляров)
store1 = Store(name="maga", address="Cyprus")
store2 = Store(name="maga2", address="Turkey")
store3 = Store(name="maga3", address="Greece")

# Добавление товаров
store1.add_item(item_name="apple", price=500)
store1.add_item(item_name="orange", price=600)
store1.add_item(item_name="banana", price=700)

# Тестирование методов с вводом-выводом
store1.remove_item(item_name="banana")
price = store1.get_price("apple")
print(f"Цена на 'apple': {price}") # Выводим результат
new_price = float(input("Введите новую цену для 'apple': "))
store1.update_price("apple", new_price)
# вдогонку :)
price = store1.update_price(input())
print(price)