# Фильтрация по статусу "confirmed" и значению "price" int
raw_bookings = [
    {"booking_id": 1, "room": "Standard", "price": 100, "status": "confirmed"},
    {"booking_id": 2, "room": "Suite", "price": 250, "status": "pending"},
    {"booking_id": 3, "room": "Standard", "price": "100", "status": "confirmed"},  # Ошибка: price — строка!
    {"booking_id": 4, "room": "Deluxe"},  # Ошибка: нет ключа price и status!
    {"booking_id": 5, "room": "Suite", "price": 300, "status": "confirmed"},
]

def process_bookings(bookings) -> list:
    new_bookings = []
    for i in bookings:
        if i.get("status") == "confirmed" and isinstance(i.get("price"), int):
            new_bookings.append(i["room"])
    return new_bookings
query = process_bookings(raw_bookings)
print(query)



# Фильтрация по "user_id" int и "user_id" > 0, далее по возрастанию если кратное число
raw_logs= [{"user_id": 10, "event": "click"}, 
            {"user_id": "5", "event": "login"}, 
            {"user_id": 10, "event": "view"}, 
            {"user_id": None, "event": "click"}, 
            {"user_id": -2, "event": "logout"}, 
            {"user_id": 4, "event": "click"}]

def filt_logs(raw_logs: list[dict]) -> list[int]:
    unique_id = {item.get("user_id") for item in raw_logs if isinstance(item.get("user_id"), int) and item.get("user_id") > 0}   
    return sorted(item for item in unique_id if item % 2 == 0)  
result = filt_logs(raw_logs)
print(result)



# Выделение определенного объема символов через генератор 
import typing


def chunk_pipeline(items: list[int], chunk_size: int) -> typing.Iterator[list[int]]:
    for i in range(0, len(items), chunk_size):
        step = i + chunk_size
        yield items[i:step]

    # Или yield items[i : i + chunk_size]

ids = [1, 2, 3, 4, 5]
chunk_size = 2

for chunk in chunk_pipeline(ids, chunk_size): print(chunk)


# Геттер Сеттер Фильтрация входного значения через ООП 
class Wallet:
    def __init__(self, initial_balance: int | float):
        self.balance = initial_balance

    @property
    def balance(self) -> int | float: 
        return self._balance
    
    @balance.setter 
    def balance(self, new_balance: int | float):
        if new_balance < 0:
            raise ValueError("Коммерческий текст ошибки!")
        self._balance = new_balance

wallet = Wallet(100)
print(wallet.balance)
wallet.balance = 250
print(wallet.balance)
wallet.balance = -50



# Безопасное клонирование структуры корзины покупок пользователя 
# перед применением скидочного промокода, 
# чтобы не повредить исходные данные в сессии кэша, copy deepcopy но без них
from typing import Any


def apply_discount(cart: dict[str, Any], discount: float) -> dict[str, Any]:
    new_items = [
        {**item, "price": item.get('price') * (1 - discount)} for item in cart.get("items", [])
    ]
    return {"promo_applied": True,
          "items": new_items
}

source_cart = {"promo_applied": False, "items": [{"name": "Python Book", "price": 100}]}
new_cart = apply_discount(source_cart, 0.1)
print(new_cart)
print(source_cart)



# Оптимизация валидатора статусов заказов для предотвращения 
# багов при сравнении динамических данных в памяти.
def validate_status(status_id: int | str, expected_id: int | str) -> bool:
    first = status_id == expected_id
    second = status_id is expected_id
    return first and second

value = 999
second = int('999')
print(validate_status(200, 200))
print(validate_status(second, value))

def verify_token(incoming_token: str, master_token: str) -> bool:
    first = incoming_token == master_token
    second = incoming_token is master_token
    return first and second

print(verify_token('admin', 'admin'))
print(verify_token('1', str(1)))


# Безопасный парсинг JSON-ответа от внешнего микросервиса бронирования, 
# где могут прийти битые или неверные данные.
import json


def parse_api_response(raw_data: str) -> dict | None:
    try:
        result = json.loads(raw_data)
        if isinstance(result, dict):
            return result
        else:
            raise TypeError("Response is not a dictionary")
    except (TypeError, json.JSONDecodeError):
        return None
    
print(parse_api_response('{"status": "ok"}'))
print(parse_api_response('{"status": "ok"'))
print(parse_api_response(''))



#Функция обёртка с любым количеством аргументов и вызовом имени функции 
from functools import wraps


def track_api_call(func):
    @wraps(func) 
    def wrapper(*args, **kwargs): 
        print("[LOG]: Старт")
        result = func(*args, **kwargs) 
        print(f"[API LOG] Вызвана функция: {func.__name__} | Передано позиционных аргументов: {len(args)}")
        print("[LOG]: Финиш")
        return result 
    return wrapper

@track_api_call
def create_booking(user_id: int, room_type: str):
    return f"Booking {room_type} for {user_id} created"

print(create_booking(2, "тип комнаты"))



# Реализуйте функцию-генератор, которая принимает на вход список словарей (сырые логи) 
# и лениво фильтрует только успешные транзакции (статус "success") НЕДОДЕЛАЛ
import sys
from typing import Any, Iterator


raw_logs = [{"id": 1, "status": "success", "card_pan": "4444...1111", "amount": 100}, 
            {"id": 2, "status": "failed", "card_pan": "5555...2222", "amount": 200}, 
            {"id": 3, "status": "success", "amount": 300}]

def filter_success(raw_data: list[dict]) -> Any:
    for item in raw_data:
        if item.get('status') == 'success':
            yield {k: v for k, v in item.items() if k != 'card_pan'}

def batch_to_send(success_data: Iterator) -> Any:
    try:
        return {item.get('id'): item for item in success_data}
    except KeyError:
        return {item.get('id'): item for item in success_data}

result = batch_to_send(filter_success(raw_logs))
print(result)

print(sys.getsizeof(list))
print(sys.getsizeof(dict))



# Реализуйте функцию-генератор, которая принимает на вход список словарей (сырые логи) 
# и лениво фильтрует только успешные транзакции (статус "success") и избавляется от 
# чувствительных данных (данных карты клиента)
import sys
from typing import Any, Iterator


raw_logs = [{"id": 1, "status": "success", "card_pan": "4444...1111", "amount": 100}, 
            {"id": 2, "status": "failed", "card_pan": "5555...2222", "amount": 200}, 
            {"id": 3, "status": "success", "amount": 300}]

def filter_success(raw_data: list[dict]) -> Any:
    for item in raw_data:
        if item.get('status') == 'success':
            yield {k: v for k, v in item.items() if k != 'card_pan'}

def batch_to_send(success_data: Iterator) -> Any:
    result = {}
    for item in success_data:
        try:
            transaction_id = item['id']
            result[transaction_id] = item
        except KeyError:
            continue
    return result            

result = batch_to_send(filter_success(raw_logs))
for chunk in filter_success(raw_logs): print(chunk)
print(result)


print(sys.getsizeof([]))
print(sys.getsizeof({}))


# Декоратор для функции обработки платежа который показывает какая ошибка в функции появилась
from functools import wraps
 

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception:
            print(f'[ERROR] {func.__name__} failed')
            raise
    return wrapper

@log_action
def process_payment(amount: int):
    """Обработка платежа."""
    if amount < 0:
        raise ValueError("Сумма не может быть отрицательной")
    return True

print(process_payment.__name__)
print(process_payment.__doc__)
process_payment(-50)



