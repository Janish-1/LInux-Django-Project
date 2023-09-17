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
    cursor.execute("CREATE TABLE table1(ID int,class VARCHAR(50),year VARCHAR(10),details VARCHAR(100))")
    cursor.execute("INSERT INTO table1(ID,class,year,details) VALUES (1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),(2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),(3, 'CLA', '2019', 'Subcompact executive fastback sedan'),(4, 'CLS', '2018', 'E-segment/executive fastback sedan'),(5, 'E-CLASS', '2017', 'E-segment/executive sedan'),(6, 'EQE', '2022', 'All-electric E-segment fastback'),(7, 'EQS', '2021', 'All-electric full-size luxury liftback'),(8, 'S-CLASS', '2020', 'F-segment/full-size luxury sedan.'),(9, 'G-CLASS', '2018', 'Mid-size luxury SUV, known as the G-Wagen'),(10, 'GLE', '2019', 'Mid-size luxury crossover SUV')")
    cursor.execute("SELECT * FROM table1")
    conn.commit()
    print(cursor.fetchall())
    conn.close()

def read():
    # Connecting to Postgresql
    conn = psycopg2.connect(database="myproject",
                            host="localhost",
                            user="myprojectuser",
                            password="myproject",
                            port="")

    # Creating a Table
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table1")
    conn.commit()
    print(cursor.fetchall())
    conn.close()

def create(id, clas, year, car_type):
    # Connecting to PostgreSQL
    conn = psycopg2.connect(
        database="myproject",
        host="localhost",
        user="myprojectuser",
        password="myproject",
        port=""
    )

    try:
        # Creating a Table
        cursor = conn.cursor()
        # Use parameterized query to prevent SQL injection
        cursor.execute("INSERT INTO table1 (ID, class, year, details) VALUES (%s, %s, %s, %s)", (id, clas, year, car_type))

        # Fetching and printing the inserted record
        cursor.execute("SELECT * FROM table1")
        print("Inserted Record:")
        print(cursor.fetchall())

        # Commit the transaction
        conn.commit()

    finally:
        # Close the connection
        conn.close()

def update(id,clas,year,car_type):
    # Connecting to PostgreSQL
    conn = psycopg2.connect(
        database="myproject",
        host="localhost",
        user="myprojectuser",
        password="myproject",
        port=""
    )

    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE table1 SET class=%s,year=%s,details=%s WHERE ID=%s",(clas,year,car_type,id))

        #Fetching and printing the updated Record
        cursor.execute("SELECT * FROM table1")
        print(cursor.fetchall())

        #Commit the transaction
        conn.commit()

    finally:
        #Close the COnnection
        conn.close()

# Calling the function
# table() # To Create a Table
# read() # To read a table
# create(11, "B", "2023", "Hatchback") # Add new row to a table
# update(11,"A","2023","Hatchback/Offroad")