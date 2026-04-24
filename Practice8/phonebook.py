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

def search_contacts(term):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts_pattern(%s)", (term,))
            return cur.fetchall()

def add_or_update_contact(name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
            conn.commit()
    print(f"Contact '{name}' processed.")

def bulk_insert_with_validation(names, phones):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
            conn.commit()
    print("Bulk insert completed.")

def get_paginated_contacts(limit, offset):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            return cur.fetchall()

def delete_contact(identifier):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact_proc(%s)", (identifier,))
            conn.commit()
    print(f"Contact '{identifier}' deleted.")

def main():
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Add/Update Contact")
        print("2. Bulk Insert")
        print("3. Search by Pattern")
        print("4. View with Pagination")
        print("5. Delete Contact")
        print("0. Exit")
        
        cmd = input("Choose an action: ")
        
        if cmd == '1':
            add_or_update_contact(input("Enter Name: "), input("Enter Phone: "))
        
        elif cmd == '2':
            names_input = input("Enter names (comma separated): ")
            phones_input = input("Enter phones (comma separated): ")
            names = [n.strip() for n in names_input.split(',')]
            phones = [p.strip() for p in phones_input.split(',')]
            bulk_insert_with_validation(names, phones)
            
        elif cmd == '3':
            results = search_contacts(input("Enter search term: "))
            if not results:
                print("No records found.")
            for r in results: 
                print(r)
            
        elif cmd == '4':
            try:
                limit = int(input("Limit: "))
                offset = int(input("Offset: "))
                results = get_paginated_contacts(limit, offset)
                for r in results: 
                    print(r)
            except ValueError:
                print("Invalid input.")
            
        elif cmd == '5':
            delete_contact(input("Enter Name or Phone: "))
            
        elif cmd == '0':
            break

if __name__ == "__main__":
    main()