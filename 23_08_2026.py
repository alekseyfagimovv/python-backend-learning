# Асинхронный генератор которая принимает количество чанков (кусков файла) и их размер
# и отдаёт наружу нужный объем данных
# import asyncio


# async def download_cat(cat_data: int, size_chunk: int):
#     downloaded = 0
#     while downloaded < cat_data:
#         await asyncio.sleep(1)
#         downloaded += size_chunk
#         current_chunk = min(size_chunk, cat_data - (downloaded - size_chunk))
#         yield current_chunk

# async def monitor_cat():
#     async for cat in download_cat(5, 2):
#         print(f"Получены данные: {cat}")

# asyncio.run(monitor_cat())



# Асинхронную функция, которая проверяет статус API трех сторонних банков     
# import asyncio
# import time

# def check_single_bank_sync(bank_name):
#     time.sleep(3) 
#     return "Данные из синхронного источника"

# async def async_heavy_sync(bank_name):
#     result = await asyncio.to_thread(check_single_bank_sync, bank_name)
#     print(f"Получил: {result}")

# async def heck_all_banks(banks_list):
#     await asyncio.gather(
#         async_heavy_sync(),
#         banks_list # мы здесь список других задач я так понял дропаем 
#     )

# asyncio.run(main())