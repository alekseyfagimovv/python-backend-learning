# Запуск синхронной задачи асинхронно с асинхронными задачами
#  import asyncio
# from concurrent.futures import ProcessPoolExecutor


# def sync_generate_pdf_layout(user_id): # Тяжелая синхронная функция
#     return "pdf"

# async def async_check_stock(size): # Асинхронная легкая функция запроса 
#     await asyncio.sleep(1) 
#     return "https://suite"

# process_executor = ProcessPoolExecutor() # Выделяет нужно кол-во ядер, либо выделяем самостоятельно
# # все ядра - 1, одно оставляем для ОС

# async def process_user_avatar(user_id, size):
#     loop = asyncio.get_running_loop()
#     result_pdf = loop.run_in_executor(
#     process_executor,
#     sync_generate_pdf_layout, 
#     user_id           
# )
#     result_check = async_check_stock(size)
    
#     result_pdf, result_check = await asyncio.gather(result_pdf, result_check)
#     return result_pdf, result_check

