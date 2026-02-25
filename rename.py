import os

directory = 'C:\\Users\\vjadhav\\Documents\\DBT\\Tutorials\\'

for file in os.listdir(directory):
    file_num = file.split('.')[0]
    if file_num.isdigit():
        if int(file_num) > 9:
            new_filename = str(int(file_num) + 1) + "." + ".".join(file.split('.')[1:])
            print(f'Renaming {file} to {new_filename}')
            # os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))



a = [1, 2, 3, 4]

print (type)