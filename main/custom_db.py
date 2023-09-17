import psycopg2

def table():
    # Connecting to Postgresql
    conn = psycopg2.connect(database="myproject",
                            host="localhost",
                            user="myprojectuser",
                            password="myproject",
                            port="")

    # Creating a Table
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE table1(ID int,Class VARCHAR(50),Year VARCHAR(10),Details VARCHAR(100))")
    cursor.execute("INSERT INTO table1(ID,Class,Year,Details) VALUES (1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),(2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),(3, 'CLA', '2019', 'Subcompact executive fastback sedan'),(4, 'CLS', '2018', 'E-segment/executive fastback sedan'),(5, 'E-CLASS', '2017', 'E-segment/executive sedan'),(6, 'EQE', '2022', 'All-electric E-segment fastback'),(7, 'EQS', '2021', 'All-electric full-size luxury liftback'),(8, 'S-CLASS', '2020', 'F-segment/full-size luxury sedan.'),(9, 'G-CLASS', '2018', 'Mid-size luxury SUV, known as the G-Wagen'),(10, 'GLE', '2019', 'Mid-size luxury crossover SUV')")
    cursor.execute("SELECT * FROM table1")
    conn.commit()
    print(cursor.fetchall())
    conn.close()

table()