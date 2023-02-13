def get_todos(filepath="todo.txt"):
    with open(filepath, "r") as f_local:
        todo_local = f_local.readlines()
        return todo_local
"""
 read file of todo.txt and retun as a list
"""

def write_todos(todo_arg,filepath="todo.txt"):
    with open(filepath, "w") as f_local:
        f_local.writelines(todo_arg)
""" 
write file of todo.txt and retun as a list
"""