#Функция обёртка с любым количеством аргументов и вызовом имени функции 
# from functools import wraps


# def track_api_call(func):
#     @wraps(func) 
#     def wrapper(*args, **kwargs): 
#         print("[LOG]: Старт")
#         result = func(*args, **kwargs) 
#         print(f"[API LOG] Вызвана функция: {func.__name__} | Передано позиционных аргументов: {len(args)}")
#         print("[LOG]: Финиш")
#         return result 
#     return wrapper

# @track_api_call
# def create_booking(user_id: int, room_type: str):
#     return f"Booking {room_type} for {user_id} created"

# print(create_booking(2, "тип комнаты"))



# Асинхронный пинг серверов
# import asyncio


# async def ping_server(server_name, delay):
#     print(f'Пингуем сервер {server_name}')
#     await asyncio.sleep(delay)
#     print(f'{server_name} Работает!')

# async def main():
#         await asyncio.gather(ping_server("server_a", 3), 
#                              ping_server("server_b", 1),
#                              ping_server("server_v", 2)
#                              )
#         print("Пинг завершён")
    
# asyncio.run(main()) 



# Реализуйте функцию-генератор, которая принимает на вход список словарей (сырые логи) 
# и лениво фильтрует только успешные транзакции (статус "success") НЕДОДЕЛАЛ
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
#     try:
#         return {item.get('id'): item for item in success_data}
#     except KeyError:
#         return {item.get('id'): item for item in success_data}

# result = batch_to_send(filter_success(raw_logs))
# print(result)

# print(sys.getsizeof(list))
# print(sys.getsizeof(dict))