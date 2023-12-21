import os

# Solution by Cuong Vo
def folder_size_recursion(folder):
    total_size = 0
    for f in os.listdir(folder):
        tmp = os.path.join(folder, f)
        if os.path.isfile(tmp):
            total_size += os.path.getsize(tmp)
        elif os.path.isdir(tmp):
            total_size += folder_size_recursion(tmp)
    return total_size


folder = '.'
print(f'Folder size : {round(folder_size_recursion(folder) / 1024, 3)} KB')