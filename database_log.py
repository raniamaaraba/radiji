import psycopg2

try:
    connection = psycopg2.connect(user="rankuluw",
                                  password="password",
                                  host="localhost",
                                  port="5432",
                                  database="radiji")
    cursor = connection.cursor()
    result = cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(record)

except Exception as e:
    print(e)

