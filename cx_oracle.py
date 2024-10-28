import cx_Oracle

# Connect to the Oracle database
connection = cx_Oracle.connect('username', 'password', 'hostname/service_name')
cursor = connection.cursor()

# Create a PL/SQL procedure
plsql_code = '''
CREATE OR REPLACE PROCEDURE add_user(p_name IN VARCHAR2, p_age IN NUMBER) AS
BEGIN
    INSERT INTO users (name, age) VALUES (p_name, p_age);
END add_user;
'''

# Execute the PL/SQL code to create the procedure
cursor.execute(plsql_code)

# Call the PL/SQL procedure
cursor.callproc('add_user', ['Charlie', 35])

# Query the data to see the result
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)  # Output will include the new entry for 'Charlie'

# Clean up: Drop the procedure
cursor.execute("DROP PROCEDURE add_user")

# Commit and close the connection
connection.commit()
cursor.close()
connection.close()
