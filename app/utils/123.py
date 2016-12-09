import os
current_path = os.getcwd()
def tree(current_path):
    content = os.listdir(current_path)
    print(content)
    for each in content:
        if os.path.isdir(each)and each[0]!='.':
            print(each)


print(tree(current_path))
