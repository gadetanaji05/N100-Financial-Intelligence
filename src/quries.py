import sqlite3

# Database Connection
conn = sqlite3.connect("financial_data.db")
cursor = conn.cursor()
print("Database Connected Successfully!")

# Query 1 - First 5 Companies
cursor.execute("SELECT * FROM companies LIMIT 5")
rows = cursor.fetchall()

print("\nFirst 5 Companies:")
for row in rows:
    print(row)


# Query 2 - Top 10 Companies
def top_10_companies(conn):
    cursor = conn.cursor()

    cursor.execute("""
    SELECT company_name
    FROM companies
    ORDER BY company_name
    LIMIT 10
    """)
def search_company(conn):
    cursor = conn.cursor()

    company = input("Enter company name: ")

    cursor.execute("""
    SELECT * FROM companies
    WHERE company_name LIKE ?
    """, ('%' + company + '%',))

    rows = cursor.fetchall()

    print("\nSearch Results:")
    for row in rows:
        print(row)

def count_companies(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM companies")

    total = cursor.fetchone()

    print("\nTotal Companies:", total[0])

    rows = cursor.fetchall()

    print("\nTop 10 Companies:")
    for row in rows:
        print(row)

def list_companies(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT company_name FROM companies")

    rows = cursor.fetchall()

    print("\nAll Company Names:")
    for row in rows:
        print(row[0])


# Run Query 2
top_10_companies(conn)
search_company(conn)
count_companies(conn)
list_companies(conn)

# Close Database
conn.close()
print("\nDatabase Connection Closed.")