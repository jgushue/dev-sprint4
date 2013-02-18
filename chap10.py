# Jackie Gushue

# 10.4
def middle(x):
	x.pop(0)
	x.pop(-1)
	return x

print middle([1,2,3,4])

# 10.10

import time

def append_list():
    app_list = []
    in_file = open('words.txt')
    for line in in_file:
        word = line.strip()
        app_list.append(word)
    return app_list


def concat_list():
    concat_list = []
    in_file = open('words.txt')
    for line in in_file:
        word = line.strip()
        concat_list = concat_list + [word]
    return concat_list


start_time = time.time()
append_list()
elapsed_time = time.time() - start_time
print elapsed_time

start_time = time.time()
concat_list()
elapsed_time = time.time() - start_time
print elapsed_time