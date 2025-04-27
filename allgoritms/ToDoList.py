# این برنامه یک تکه کد برای مدیریت کار ها هستش
# کاربر می‌تواند وظایف را اضافه کند، وضعیت آنها را تغییر دهد و لیست کامل وظایف خود را مشاهده کند   



class Task:
    def __init__(self, title, status="To-Do"):
        self.title = title
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'"{task.title}" added to list')

    def mark_as_done(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.status = "Done"
                print(f'"{task.title}" its change to done situation .')
                return
        print(f'"{task_title}" not found !!! ')

    def display_tasks(self):
        print("to do list: ")
        for task in self.tasks:
            print(f'subject: {task.title} | status: {task.status}')

# ساخت یک لیست از وظایف
todo_list = ToDoList()

# اضافه کردن وظایف
task1 = Task("first project")
task2 = Task("read book ")
todo_list.add_task(task1)
todo_list.add_task(task2)

# نمایش لیست وظایف
todo_list.display_tasks()

# علامت زدن وظیفه به عنوان انجام شده
todo_list.mark_as_done("first project")

# نمایش لیست وظایف بعد از تغییرات
todo_list.display_tasks()
