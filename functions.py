
# def get_todos(filepath):
#     with open(filepath, 'r') as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
FILEPATH = "todos.txt"


def get_todos(filepath="todos.txt"):
    """Read a textfile and return the list of
    to do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("HELLO")