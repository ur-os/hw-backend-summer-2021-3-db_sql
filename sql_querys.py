# INFO
# Вывести топ 5 самых коротких по длительности перелетов
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = ''
'SELECT flight_no, to_char((actual_arrival - actual_departure), \'HH24:MI:SS\') AS duration'
'FROM flights'
'ORDER BY duration'
'LIMIT 5'

#  flight_no | duration 
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
"""
#  flight_no | count 
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# INFO
# Вывести число перелетов внутри одной таймзоны 
# Нузно вывести 1 значение в колонке count
TASK_3_QUERY = """
"""
#  count  
# --------
#  16824

