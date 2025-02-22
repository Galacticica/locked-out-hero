import sqlite3

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE usage_log (
#                id INTEGER PRIMARY KEY,
#                building_name VARCHAR(50),
#                user_id INTEGER,
#                time_accessed TIMESTAMP,
#                FOREIGN KEY (building_name) REFERENCES building_access_building(name),
#                FOREIGN KEY (user_id) REFERENCES login_user(id)
#     );
#                """)

cursor.execute("""DROP TABLE usage_log;""")

connection.commit()
connection.close()
