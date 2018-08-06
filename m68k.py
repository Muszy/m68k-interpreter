import sys


def is_valid_path(file_path):
	return file_path.lower().endswith('.x68')

def get_valid_paths(file_paths):
	return [p for p in file_paths if is_valid_path(p)]

def get_file_name(file_path):
        return file_path.split('\\')[-1]

def tokenize_command(command):
	s = command.lower().split()
	l = len(s)
	if l == 3:
		token = s
	elif l == 2:
		token = ['\t']+s
	return token

def print_file(file_path):
        pc = 0
        with open(file_path) as file:
                tokens = [tokenize_command(line) for line in file]

        print('{fn}\n'.format(fn=get_file_name(file_path)))
        for token in tokens:
                print('[PC]: {pc}\n[LABEL]: {lbl}\n[COMMAND]: {cmd}\n[ARGUMENTS]: {arg}\n'.format(pc=pc,lbl=token[0],cmd=token[1],arg=token[2]))
                pc += 4
                
        
def main():
	for file_path in get_valid_paths(sys.argv[1:]):
                print_file(file_path)

if __name__ == "__main__":
	main()
