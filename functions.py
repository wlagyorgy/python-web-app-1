FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Read the todos from the file and store it in a list.
    :param filepath:
    :return: todo list
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


# print(get_todos.__doc__)
# the condtion block the exection when importing this module
print(__name__)
if __name__ == "__main__":
    print(help(get_todos))
    print("Hello")


def write_todos(todos_local, filepath=FILEPATH):
    """
    Write todos list into a file
    :param todos_local:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_local)
