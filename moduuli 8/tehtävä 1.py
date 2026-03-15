import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='joonas',
    password='a72dKl20j@',
    autocommit=True
)

icao_code = input("Enter the ICAO code of an airport: ")

cursor = db.cursor()
cursor.execute("", (icao_code.upper(),))
result = cursor.fetchall()

if not result:
    print(f"No airport found with ICAO code {icao_code}")

else:
    for row in result:
        print(f"Airport name: {row[0]}")
        print(f"Location: {row[1]}")

