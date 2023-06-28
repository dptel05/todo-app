FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
# This function needs 'return' as it is returning the todos from the file.


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do item in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
# This custom function does not need to 'return'
# because it is a modifier/procedure  it does not return anything as it,
# modifies the file, nothing to capture.


if __name__ == "__main__":
    print("Hello")
    print(get_todos())