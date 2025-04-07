import sqlite3

def main():
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    # Drop tables if they already exist
    cursor.execute("DROP TABLE IF EXISTS person_pet")
    cursor.execute("DROP TABLE IF EXISTS pet")
    cursor.execute("DROP TABLE IF EXISTS person")

    # Create tables
    cursor.execute('''
    CREATE TABLE person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE person_pet (
        person_id INTEGER,
        pet_id INTEGER,
        FOREIGN KEY (person_id) REFERENCES person(id),
        FOREIGN KEY (pet_id) REFERENCES pet(id)
    )
    ''')

    # Insert data into person table
    cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ])

    # Insert data into pet table
    cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", [
        (1, 'Rusty', 'Dalmatian', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ])

    # Insert data into person_pet table
    cursor.executemany("INSERT INTO person_pet VALUES (?, ?)", [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ])

    connection.commit()
    connection.close()
    print("Database pets.db created and populated.")

if __name__ == "__main__":
    main()
