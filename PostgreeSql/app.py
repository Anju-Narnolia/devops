import psycopg2

try:
    conn = psycopg2.connect(
        host="database-1.clasq2qci02p.ap-south-1.rds.amazonaws.com",
        port="5413",
        database="mydb",
        user="postgres",
        password="Anju#123#123"
    )
    # curr = conn.cursor()
    # # create table
    # curr.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY , name varchar(255), email varchar(255), password varchar(255))")
    print("✅ Connected to PostgreSQL successfully and create also!")

    # # Insert Values ito table
    # curr.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",("Anu","anju@g.com","Palak@123"))
    # conn.commit()
    # print("data inserted successfully")

    # # get Data 
    # curr.execute("SELECT * FROM users")
    # rows = curr.fetchall()
    # for row in rows:
    #     print(row)

except Exception as e:
    print("❌ Error:", e)

finally:
    # close connection
    curr.close()
    conn.close()
