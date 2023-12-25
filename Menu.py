import sqlite3

def create_menu_table():
    try:
        # Connect to SQLite database
        con = sqlite3.connect('Menudb.sqlite')
        cur = con.cursor()

        # Drop the Menu table if it exists
        cur.execute('DROP TABLE IF EXISTS Menu')

        # Create the Menu table with columns Dish and Cost
        cur.execute('CREATE TABLE Menu (Dish TEXT, Cost INTEGER)')

        # Add sample entries to the Menu table
        cur.execute('INSERT INTO Menu (Dish, Cost) VALUES (?, ?)', ('VadaPav', 15))
        cur.execute('INSERT INTO Menu (Dish, Cost) VALUES (?, ?)', ('SamosaPav', 18))
        cur.execute('INSERT INTO Menu (Dish, Cost) VALUES (?, ?)', ('MisalPav', 50))
        cur.execute('INSERT INTO Menu (Dish, Cost) VALUES (?, ?)', ('Tea', 15))
        cur.execute('INSERT INTO Menu (Dish, Cost) VALUES (?, ?)', ('Coffee', 15))

        # Commit the changes
        con.commit()

        print("Menu table created successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        con.close()

# Usage example
create_menu_table()





