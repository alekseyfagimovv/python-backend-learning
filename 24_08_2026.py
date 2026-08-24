# Тестовая асинхронная задача с параллельным запуском 
# нескольких асинхронных запросов и синхронным запросом 
# import asyncio
# import time


# def save_report():
#     time.sleep(2)
#     return "Отчет сохранен!"


# async def task(name: str, delay: int):
#     await asyncio.sleep(delay)
#     return f'Задача {name} выполнена!'


# async def heavy_save_report_fixed():
#     result = await asyncio.to_thread(save_report)
#     return result


# async def main():
#     results = await asyncio.gather(
#         heavy_save_report_fixed(),
#         task('Номер 1', 1),
#         task('Номер 2', 3),
#         task('Номер 3', 5),
#         return_exceptions=True
#     )
#     return results

# start = asyncio.run(main())
# print(start)