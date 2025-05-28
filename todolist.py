import sqlite3
import os

class List:
    def __init__(self, db_name="todo.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.initialize_tables()

    def initialize_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0,
                user_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        ''')
        self.conn.commit()

    def add_user(self, name = None):
        if not name:
            name = input('Enter user name:')
        self.cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        self.conn.commit
        print(f'user"{name}" added.')

    def add_category(self,name = None):
        if not name:
            name = input('Enter category name:')
        self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        self.conn.commit
        print(f'category"{name}" added.')


    def add_task(self):
        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM categories')
        categories = self.cursor.fetchall()
        
        if not users or not categories:
            print('please select a user and a category')
            return
        
        print('select user:')
        for user in users:
            print(f"{user[0]}: {user[1]}")
        user_id = int(input('user ID:'))

        print("Select a category:")
        for category in categories:
            print(f"{category[0]}: {category[1]}")
        category_id = int(input("Category ID: "))

        
        description = input('Enter description:')
        self.cursor.execute('INSERT INTO tasks(description,user_id, category_id) VALUES(?, ?, ?)',(description,user_id, category_id))
        self.conn.commit()
        print('Task added')

    def list_tasks(self):
         self.cursor.execute('''
            SELECT tasks.id, tasks.description, tasks.completed, users.name, categories.name
            FROM tasks
            LEFT JOIN users ON tasks.user_id = users.id
            LEFT JOIN categories ON tasks.category_id = categories.id
        ''')
         tasks = self.cursor.fetchall()

         if not tasks:
            print("No tasks found.")
            return
       
         for task in tasks:
            status = "[✓]" if task[2] else "[ ]"
            print(f"{task[0]}. {status} {task[1]} (User: {task[3]}, Category: {task[4]})")

    def mark_task_complete(self):
        task_id = int(input("Enter task ID to mark as complete: "))
        self.cursor.execute('UPDATE tasks SET copmleted = 1 WHERE id = ?',(task_id))
        if self.cursor.rowcount:
            self.conn.commit()
            print("Task marked as complete.")
        else:
            print("Task not found.")

    

            


        


