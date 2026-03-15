import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="your_password"
    )

    cursor = connection.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return (result[0], result[1])
    else:
        print(f"Airport with ICAO code {icao_code} not found in the database.")
        return None


def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ")
    icao2 = input("Enter the ICAO code of the second airport: ")

    coord1 = get_airport_coordinates(icao1)
    coord2 = get_airport_coordinates(icao2)

    if coord1 and coord2:
        distance = geodesic(coord1, coord2).kilometers
        print()
        print(f"\nDistance between {icao1} and {icao2}: {distance:.2f} kilometers")


run_airport_distance()