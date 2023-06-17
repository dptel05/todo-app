import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            # or get_todos = (filepath = "files/dddd.txt")
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            # = filepath = "files/todos.txt", todo_arg = todos
            # =  todos
        case sg.WIN_CLOSED:
            break

window.close()
