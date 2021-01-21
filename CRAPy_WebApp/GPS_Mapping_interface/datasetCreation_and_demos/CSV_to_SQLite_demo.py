import csv, sqlite3, os

db = 'GPS_data.db'



if db not in os.listdir():
    #if database does not exist, create it
    conn = sqlite3.connect(db)
    c = conn.cursor()

    print("Creation of new database: " + db)
    c.execute("CREATE TABLE GPS_data(timestamp DATETIME, latitude NUMERIC, longitude NUMERIC, altitude NUMERIC)")
    conn.commit()
else:
    #connect to the database without creating a new table
    conn = sqlite3.connect(db)
    c = conn.cursor()

#add the values from the CSV to the database
with open('20210112-235627.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        #Skips the first row (header)
        if('lat' in row[2]):
            continue

        c.execute("INSERT INTO GPS_data VALUES((?),(?),(?),(?))",(row[1], row[2], row[3], row[5]))
        conn.commit()

# TESTING print database content
# for row in c.execute("SELECT * FROM GPS_data"):
#     print (row)

conn.close()
