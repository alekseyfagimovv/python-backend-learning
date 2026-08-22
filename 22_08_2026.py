# Пример запуска кода с asyncio.TaskGroup()
# import asyncio


# async def book_flight():
#     print('Взлёт бронирования')
# async def book_hotel():
#     print('Бронирование отеля')
# async def book_insuranc():
#     print('Бронирование страхование')


# async def reserve_tour_pack():
#     try:
#         async with asyncio.TaskGroup() as tg:
#             task1 = tg.create_task(book_flight())
#             task2 = tg.create_task(book_hotel())
#             task3 = tg.create_task(book_insuranc())
#             print(f"Успешно забронировано: {task1.result()}, {task2.result()}, {task3.result()}")
#     except ExceptionGroup as eg: #Светиться красным т.к. ruff думает что мы на питон 3.10 и ниже
#         print(f"Тур не забронирован, отмена броней ERROR {eg}")

# asyncio.run(reserve_tour_pack())
