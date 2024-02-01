import os


def generate_files(start: int, end: int) -> int:    
    for i in range(start, end+1):
        os.system(f'echo # Solution number: {i:0>4} > {i:0>4}.py')
        print(f'File: {i:0>4}.py in {os.system("cd")} was successfully created')

generate_files(1, 1000)
