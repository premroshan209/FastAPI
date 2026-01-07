# 3. Read all shipment
# cursor.execute("SELECT * FROM shipments")
# result = cursor.fetchall()   # there is option to use fetchone() if only one record is expected, but fetchall() is safer, and fetchmany() is also available use like fetchmany(5) to get 5 records at a time
# print("Shipment Details:", result)

# # 4. Read a shipment by id
# cursor.execute("SELECT * FROM shipments WHERE id = ?", (12701,))
# result = cursor.fetchone()  
# print("Shipment Details:", result)