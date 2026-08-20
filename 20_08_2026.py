# Реализуйте функцию-генератор, которая принимает на вход список словарей (сырые логи) 
# и лениво фильтрует только успешные транзакции (статус "success") и избавляется от 
# чувствительных данных (данных карты клиента)
# import sys
# from typing import Any, Iterator


# raw_logs = [{"id": 1, "status": "success", "card_pan": "4444...1111", "amount": 100}, 
#             {"id": 2, "status": "failed", "card_pan": "5555...2222", "amount": 200}, 
#             {"id": 3, "status": "success", "amount": 300}]

# def filter_success(raw_data: list[dict]) -> Any:
#     for item in raw_data:
#         if item.get('status') == 'success':
#             yield {k: v for k, v in item.items() if k != 'card_pan'}

# def batch_to_send(success_data: Iterator) -> Any:
#     result = {}
#     for item in success_data:
#         try:
#             transaction_id = item['id']
#             result[transaction_id] = item
#         except KeyError:
#             continue
#     return result            

# result = batch_to_send(filter_success(raw_logs))
# for chunk in filter_success(raw_logs): print(chunk)
# print(result)


# print(sys.getsizeof([]))
# print(sys.getsizeof({}))


# Декоратор для функции обработки платежа который показывает какая ошибка в функции появилась
# from functools import wraps
 

# def log_action(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception:
#             print(f'[ERROR] {func.__name__} failed')
#             raise
#     return wrapper

# @log_action
# def process_payment(amount: int):
#     """Обработка платежа."""
#     if amount < 0:
#         raise ValueError("Сумма не может быть отрицательной")
#     return True

# print(process_payment.__name__)
# print(process_payment.__doc__)
# process_payment(-50)



# Функция для фоновой обработки задач в фоне и мгновенной отправки ответа пользователю  
# import asyncio

# async def check_achies():
#     await asyncio.sleep(1.5)

# async def deduct_bonus():
#     await asyncio.sleep(1)

# async def update_metrics():
#     await asyncio.sleep(2)

# async def process_order():
#     check = asyncio.create_task(check_achies())
#     deduct = asyncio.create_task(deduct_bonus())
#     update = asyncio.create_task(update_metrics())
#     return {"status": "processing"}

# asyncio.run(process_order())
