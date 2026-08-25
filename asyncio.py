# Асинхронный пинг серверов
import asyncio


async def ping_server(server_name, delay):
    print(f'Пингуем сервер {server_name}')
    await asyncio.sleep(delay)
    print(f'{server_name} Работает!')

async def main():
        await asyncio.gather(ping_server("server_a", 3), 
                             ping_server("server_b", 1),
                             ping_server("server_v", 2)
                             )
        print("Пинг завершён")
    
asyncio.run(main()) 



# Функция для обработки задач в фоне и мгновенной отправки ответа пользователю  
import asyncio

async def check_achies():
    await asyncio.sleep(1.5)

async def deduct_bonus():
    await asyncio.sleep(1)

async def update_metrics():
    await asyncio.sleep(2)

async def process_order():
    check = asyncio.create_task(check_achies())
    deduct = asyncio.create_task(deduct_bonus())
    update = asyncio.create_task(update_metrics())
    return {"status": "processing"}

asyncio.run(process_order())



# Пример запуска кода с asyncio.TaskGroup()
import asyncio


async def book_flight():
    print('Взлёт бронирования')
async def book_hotel():
    print('Бронирование отеля')
async def book_insuranc():
    print('Бронирование страхование')


async def reserve_tour_pack():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(book_flight())
            task2 = tg.create_task(book_hotel())
            task3 = tg.create_task(book_insuranc())
            print(f"Успешно забронировано: {task1.result()}, {task2.result()}, {task3.result()}")
    except ExceptionGroup as eg: #Светиться красным т.к. ruff думает что мы на питон 3.10 и ниже
        print(f"Тур не забронирован, отмена броней ERROR {eg}")

asyncio.run(reserve_tour_pack())



# Запуск синхронной задачи асинхронно с асинхронными задачами
import asyncio
from concurrent.futures import ProcessPoolExecutor


def sync_generate_pdf_layout(user_id): # Тяжелая синхронная функция
    return "pdf"

async def async_check_stock(size): # Асинхронная легкая функция запроса 
    await asyncio.sleep(1) 
    return "https://suite"

process_executor = ProcessPoolExecutor() # Выделяет нужно кол-во ядер, либо выделяем самостоятельно
# все ядра - 1, одно оставляем для ОС

async def process_user_avatar(user_id, size):
    loop = asyncio.get_running_loop()
    result_pdf = loop.run_in_executor(
    process_executor,
    sync_generate_pdf_layout, 
    user_id           
)
    result_check = async_check_stock(size)
    
    result_pdf, result_check = await asyncio.gather(result_pdf, result_check)
    return result_pdf, result_check



# Асинхронный генератор которая принимает количество чанков (кусков файла) и их размер
# и отдаёт наружу нужный объем данных
import asyncio


async def download_cat(cat_data: int, size_chunk: int):
    downloaded = 0
    while downloaded < cat_data:
        await asyncio.sleep(1)
        downloaded += size_chunk
        current_chunk = min(size_chunk, cat_data - (downloaded - size_chunk))
        yield current_chunk

async def monitor_cat():
    async for cat in download_cat(5, 2):
        print(f"Получены данные: {cat}")

asyncio.run(monitor_cat())



# Тестовая асинхронная задача с параллельным запуском 
# нескольких асинхронных запросов и синхронным запросом 
import asyncio
import time


def save_report():
    time.sleep(2)
    return "Отчет сохранен!"


async def task(name: str, delay: int):
    await asyncio.sleep(delay)
    return f'Задача {name} выполнена!'


async def heavy_save_report_fixed():
    result = await asyncio.to_thread(save_report)
    return result


async def main():
    results = await asyncio.gather(
        heavy_save_report_fixed(),
        task('Номер 1', 1),
        task('Номер 2', 3),
        task('Номер 3', 5),
        return_exceptions=True
    )
    return results

start = asyncio.run(main())
print(start)