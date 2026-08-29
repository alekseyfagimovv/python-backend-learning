# Пример SELECT UPDATE DELETE запросов на классическом sqlite3
import sqlite3

# 1. Подключаемся к базе данных 
conn = sqlite3.connect('scooters.db')
cursor = conn.cursor()

# Столбцы: id, model, battery_level (0-100), 
# status ('active', 'maintenance', 'charging'), zone_id

# Меняем из таблицы scooters  параметр status на зарядка где battery_level меньше 10
query = """UPDATE scooters                               
SET status = 'charging' 
WHERE battery_level < 10;"""  

# Удаляем из таблицы scooters самокаты которые подходят под критерии обслуживание и id зоны 5
query_second = """DELETE FROM scooters 
WHERE status = "maintenance" AND zone_id = 5"""  

# Выбираем из таблицы scooters самокаты которые подходят под критерии обслуживание и id зоны 5
query_tree = """SELECT AVG(battery_level) AS avg_battery, zone_id
FROM scooters                               
GROUP BY zone_id
HAVING AVG(battery_level) < 50
ORDER BY avg_battery DESC"""   

# 3. Выполняем запрос
cursor.execute(query)

# 4. Получаем результаты и выводим их на экран
results = cursor.fetchall()
for row in results:
    print(row)

# 5. Закрываем соединение
conn.close()

#Схема таблицы: students: id, name, score (0-100),
# category ('A', 'B', 'C'), is_certified (0 или 1).

"""UPDATE students                               
SET is_certified = 1 
WHERE score > 90 AND category = 'B'"""  
 
"""DELETE FROM students  
WHERE score = 0"""  

"""SELECT category, COUNT(*) AS count_students
FROM students
WHERE is_certified = 1 
GROUP BY category
HAVING COUNT(*) > 5"""  


# Три независимых запроса для таблицы products 
# (id, name, category, price, stock):

"""UPDATE products                               
SET price = 0
WHERE stock = 0 AND category = 'smartphones'"""  
 
"""DELETE FROM products  
WHERE price <= 100 AND category = 'accessories'"""  

"""SELECT category, SUM(price) AS total_cost
FROM products
WHERE stock > 10
GROUP BY category
HAVING SUM(price) > 500000"""  
