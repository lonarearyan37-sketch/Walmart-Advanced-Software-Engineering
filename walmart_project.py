import sqlite3

print("--- STEP 1: KACHRA DATA (RAW DATA) LOAD HO RAHA HAI ---")
# Humne kachra data banaya jisme khali jagah (None) aur chote letters hain
kachra_data = [
    (1, 'Aryan Lonare', 22, 'Nagpur'),
    (2, 'Rahul Sharma', None, 'pune'),    # Age khali hai, sheher chota likha hai
    (3, 'Amit Verma', 25, 'MUMBAI'),
    (4, 'Sneha Raut', None, 'nagpur')     # Age khali hai, sheher chota likha hai
]

print("Saaf hone se pehle ka data:")
for row in kachra_data:
    print(row)

print("\n--- STEP 2: DATA CLEANING (DATA MUNGING) SHURU ---")
saaf_data = []
for row in kachra_data:
    cust_id = row[0]
    name = row[1]
    
    # 1. Agar Age khali (None) hai, toh automatic average age 23 bhar do
    age = row[2] if row[2] is not None else 23
    
    # 2. Shehero ke naam sahi format me karo (Pehla letter bada)
    city = row[3].capitalize()
    
    saaf_data.append((cust_id, name, age, city))

print("Saaf hone ke baad ka data:")
for row in saaf_data:
    print(row)

print("\n--- STEP 3: SQL DATABASE ME SAVE KARNA ---")
# 'walmart_data.db' naam ka database banaya
conn = sqlite3.connect('walmart_data.db')
cursor = conn.cursor()

# Ek Table banayi
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clean_Customers (
    Customer_ID INTEGER,
    Name TEXT,
    Age INTEGER,
    City TEXT
)
''')

# Purana data delete karke naya data insert kiya
cursor.execute("DELETE FROM Clean_Customers")
cursor.executemany("INSERT INTO Clean_Customers VALUES (?,?,?,?)", saaf_data)
conn.commit()

print("\nMubarak ho! Data saaf hokar SQL Database me save ho gaya hai.")
conn.close()