# this is inside database.py file

import sqlite3

#make a connection to the database
connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()

# # 1. Create shipments table if it doesn't exist
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS shipments (
#         id INTEGER PRIMARY KEY,
#         weight REAL,
#         content TEXT,
#         status TEXT,
#         destination INTEGER
#     )
# """)

# # 2. Add shipments data
# cursor.execute("""
#     INSERT INTO shipments (id, weight, content, status, destination) 
#     VALUES (12702, 11.5, 'Table', 'Shipped', 100),
#     (12703, 15.0, 'Pencil', 'Pending', 101)
# """)
# connection.commit()

# # 3. Read all shipment
# cursor.execute("SELECT * FROM shipments")
# result = cursor.fetchall()   # there is option to use fetchone() if only one record is expected, but fetchall() is safer, and fetchmany() is also available use like fetchmany(5) to get 5 records at a time
# print("Shipment Details:", result)

# # 4. Read a shipment by id
# cursor.execute("SELECT * FROM shipments WHERE id = ?", (12701,))
# result = cursor.fetchone()  
# print("Shipment Details:", result)

# # 5. Delete a shipment by id
# cursor.execute("DELETE FROM shipments WHERE id = ?", (2,))  
# connection.commit()

# # 6. Update shipment status by id
# cursor.execute("UPDATE shipments SET status = ? WHERE id = ?", ('Delivered', 12702))
# connection.commit()

# or 

# # 6. Update shipment status by id
# id = 12702
# status = 'Delivered'
# cursor.execute("UPDATE shipments SET status = ? WHERE id = ?", (status, id))
# connection.commit()


# # # 6. Update shipment status by id and parameter as dictionary
# id = 12702
# status = 'Delivered'
# cursor.execute("UPDATE shipments SET status = :status WHERE id = :id", {'status': status, 'id': id})
# connection.commit()


# close the connection
connection.close()