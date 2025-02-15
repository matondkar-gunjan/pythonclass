def add_task(tasks, task_name):
      tasks.append(task_name)
      print("Task '", task_name, "'added successfully!")
def view_task(tasks):
      if len(tasks) > 0:
            print("Tasks:")
            for i in range (len(tasks)):
                  print(i+1, ".", tasks[i])
      else:
            print("No tasks available")
def remove_task(tasks, task_index):
      remove_task = tasks.pop(task_index - 1)
      print("Task '", remove_task, "' removed successfully!")
def task_manager():
      tasks = []
      exit_program = False
      while not exit_program:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                  task_name = input("Enter task name: ")
                  add_task(tasks, task_name)
            elif choice == "2":
                  view_task(tasks)
            elif choice == "3":
                  if len(tasks) > 0:
                        view_task(tasks)
                        task_index = int(input("Enter the index of the task to remove: "))
                        if 1 <= task_index <= len(tasks):
                              remove_task(tasks, task_index)
                        else:
                              print("Invalid task index!")
                  else:
                        print("No tasks to remove")
            elif choice == "4":
                  print("Exiting Task Manager.")
                  exit_program = True
            else:
                  print("Invalid choice! Please enter a number between 1 and 4.")
task_manager()                        
      
