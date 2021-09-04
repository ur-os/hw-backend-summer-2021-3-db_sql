# INFO
# Вывести топ 5 самых коротких по длительности перелетов
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = 'SELECT flight_no, duration ' \
               'FROM (' \
               '    SELECT flight_no, (scheduled_arrival - scheduled_departure) AS duration ' \
               '    FROM flights' \
               ') as one ' \
               'WHERE  duration IS NOT NULL ' \
               'ORDER BY duration LIMIT 5'

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
 SELECT flight_no , qwer as "count"
        FROM (
            SELECT flight_no, COUNT(flight_no) AS qwer 
            FROM flights 
            GROUP BY flight_no
            ) as one
        WHERE  qwer < 50
        ORDER BY qwer DESC
        LIMIT 3
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
SELECT COUNT(flight_no) AS "count"
FROM(
    SELECT flight_no, a_arival.timezone , a_departure.timezone
    FROM flights AS f
    FULL OUTER JOIN airports_data AS a_arival ON a_arival.airport_code = f.arrival_airport
    FULL OUTER JOIN airports_data AS a_departure ON a_departure.airport_code = f.departure_airport
    WHERE a_arival.timezone LIKE a_departure.timezone
 ) AS same_timezones
"""
#  count  
# --------
#  16824

