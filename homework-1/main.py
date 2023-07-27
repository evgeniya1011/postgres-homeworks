"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='azuhin56'
)

def customers_from_csv():
    customers = []
    with open("../homework-1/north_data/customers_data.csv", encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            line = (row['customer_id'], row['company_name'], row['contact_name'])
            customers.append(line)
    return customers

def employees_from_csv():
    employees = []
    with open("../homework-1/north_data/employees_data.csv", encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            line = (row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes'])
            employees.append(line)
    return employees

def orders_from_csv():
    orders = []
    with open("../homework-1/north_data/orders_data.csv", encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            line = (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city'])
            orders.append(line)
    return orders

try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers_from_csv())  #добавление несколько строчек в таблицу
            cur.execute("SELECT * FROM customers")
            rows = cur.fetchall()
            for row in rows:
                print(row)
                print()
            cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employees_from_csv())  # добавление несколько строчек в таблицу
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            for row in rows:
                print(row)
                print()
            cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders_from_csv())  # добавление несколько строчек в таблицу
            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            for row in rows:
                print(row)
                print()
finally:
    conn.close()

