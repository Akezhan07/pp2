import csv
from connect import get_connection

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    print("The table is ready.")

def insert_from_csv(file_path):
    with open(file_path, mode ="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        contacts = [tuple(row) for row in reader]

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                contacts
            )
            conn.commit()
    print(f"Imported from {file_path}")

def add_contact(name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook(name, phone) VALUES (%s, %s)",
                (name, phone)
            )
            conn.commit()

def search_contacts(term):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE name ILIKE %s OR phone LIKE %s", (f"%{term}%", f"{term}%"))
            return cur.fetchall()
        
def update_contact(name, new_phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE name = %s",
                (new_phone, name)
            )
            conn.commit()
        
def delete_contact(identifier):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM phonebook WHERE name = %s OR phone = %s",
                (identifier, identifier)
            )
            conn.commit()

def main():
    create_table()
    while True:
        print("\n1. Add 2. From CSV 3. Search 4. Update 5. Delete 0. Exit")
        cmd = input("Choose an action: ")
        if cmd == '1':
            add_contact(input("Name: "), input("Phone: "))
        elif cmd == '2':
            insert_from_csv('contacts.csv')
        elif cmd == '3':
            results = search_contacts(input("Request: "))
            for r in results:
                print(r)
        elif cmd == '4':
            update_contact(input("Contact name: "), input("New phone: "))
        elif cmd == '5':
            delete_contact(input("Name or Phone to delete: "))
        elif cmd == '0':
            break

if __name__ == "__main__":
    main()