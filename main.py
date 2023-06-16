#from functions import get_todos, write_todos,
# but now you have to write todos = functions.get_todos()
import functions
import time

cur_date_time = time.strftime("%B %d %Y, %H:%M:%S")
print(cur_date_time)

while True:
    # Get user input, strip spaces and convert to lowercase
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()
        # or get_todos = (filepath = "files/dddd.txt")

        todos.append(todo.capitalize() + '\n')

        functions.write_todos(todos)
        # = filepath = "files/todos.txt", todo_arg = todos
        # =  todos

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # list-comprehensions
        # "new_todos = [item.strip('\n') for item in todos]"

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:].strip())
            print(number)
            number = number - 1

            todos = functions.get_todos()

            print("Here are the existing todos", todos)

            new_todo = input("Enter a new todo: ")
            new_todo = new_todo.capitalize()
            todos[number] = new_todo + '\n'
            print("Here are the current todos", todos)

            functions.write_todos(todos)

        except ValueError:
            print("Your command for 'edit' is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

        except ValueError:
            print("Type the number of the todo to complete.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command not valid")

print("Bye!")

