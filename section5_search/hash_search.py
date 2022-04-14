# Unfortunately, this does not work well

import sys
sys.path.append('../')
# from tools import input_output_tools


M = 1046527
# lines, q, input_list = input_output_tools.input_multiple_lines()
lines, q, input_list = 10, 0, [['insert', 'AAA'], ['insert', 'AAC'], ['insert', 'AGA'], ['insert', 'AGG'], ['insert', 'TTT'], ['find', 'AAA'], ['find', 'CCC'], ['find', 'CCC'], ['insert', 'CCC'], ['find', 'CCC'], ['insert', 'T']]
T = ['0'] * M
transffer_dic = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

def create_key(str, key):
	for i in range(len(str)):
	    key += transffer_dic[str[i]]
	return key


def hash1(key, M):
	return key % M


def hash2(key, M):
	return 1 + (key % (M - 1))


def hash(key, i, M):
	return (hash1(key, M) + hash2(key, M)) % M


def insert(key, M, i):
	print(len(T))
	while True:
		# print(f'i: {i}')
		j = hash(key, i, M)
		# print(f'j: {j}')
		if T[j] == '0':
			T[j] = key
			return j
		else:
			i += 1


def search(key, M, i):
	while True:
		j = hash(key, i, M)
		if T[j] == key:
			return True
		elif T[j] == "0" or i >= M:
			return False
		else:
			i += 1


for i in range(len(input_list)):
	key_word = input_list[i][1]
	key = create_key(key_word, 0)
	if input_list[i][0] == 'insert':
		insert(key, M, 0)
	else:
		if search(key, M, 0):
			print('yes')
		else:
			print('no')