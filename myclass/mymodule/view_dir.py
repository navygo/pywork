import os
def view_dir(path='.'):
    """
    :args path: 
    """
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name,end=' ')
    print()

