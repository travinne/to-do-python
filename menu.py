from todolist import List

class Menu:

    def __init__(self):
        self.todo_list = List()

    def run(self):
        while True:
            print('\noptions')
            print('1. Add user')
            print('2. Add category')
            print('3. Add task')
            print('4. List tasks')
            print('5. Mark task as complete')
            print('6. Exit')

            choice = input('choose one option:')

            if choice == '1':
                self.todo_list.add_user()
            elif choice == '2':
                self.todo_list.add_category()
            elif choice == '3':
                self.todo_list.add_task()
            elif choice == '4':
                self.todo_list.list_tasks()
            elif choice == '5':
                self.todo_list.mark_task_complete()
            elif choice == '6':
                print('see you later!')
                break
            else:
                print('sorry invalid choice!')

if __name__ == '__main__':
    Menu = Menu()
    Menu.run()
    