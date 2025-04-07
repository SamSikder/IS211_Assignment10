import sqlite3

def main():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        person_id = input("Enter person ID (or -1 to exit): ")
        if person_id == '-1':
            break

        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone()
        if person:
            print(f"{person[0]} {person[1]}, {person[2]} years old")
            cursor.execute('''
            SELECT pet.name, pet.breed, pet.age, pet.dead
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
            ''', (person_id,))
            pets = cursor.fetchall()
            for pet in pets:
                status = 'was' if pet[3] == 1 else 'is'
                print(f"{person[0]} {person[1]} {status} the owner of {pet[0]}, a {pet[1]}, that was {pet[2]} years old.")
        else:
            print("Person not found.")

    conn.close()

if __name__ == "__main__":
    main()
