import time
import subprocess
import random
import string

count=0

def create_file(filename):
	global count
	command=['touch']
	filename=filename+f"{count}"+'.txt'
	command.append(filename)
	subprocess.run(command)
	count=count+1

def delete_file(filename):
	global count
	command=['rm']
	fileno=random.randint(0,count)
	filename=filename+f"{fileno}"+'.txt'
	command.append(filename)
	subprocess.run(command)
	count=count-1
		
def write_file(filename,mode='w'):
	fileno=random.randint(0,count)
	filename=filename+f"{fileno}"+'.txt'
	randomtext=''.join(random.choices(string.ascii_letters,k=5))
	with open(filename,mode) as file:
		file.write(randomtext+'\n')
		
def cat_file(filename):
	global count
	command=['cat']
	fileno=random.randint(0,count)
	filename=filename+f"{fileno}"+'.txt'
	command.append(filename)
	subprocess.run(command)

#value = int(input("Press 1 to create,2 to delete,3 to write and 4 to cat:--  "))
filename='bugfile_'
create_file(filename)
value=random.randint(1,5)
match value:
	case 1:
		create_file(filename)
	case 2:
		delete_file(filename)
	case 3:
		write_file(filename)
	case 4:
		cat_file(filename)
	case _:
		print("wrong key")
	

