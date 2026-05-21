"""Minimal file I/O helpers using explicit open()/close() calls.

These show the exact style taught in class (no context managers).
"""


def write_text_file(path, text):
	f = open(path, 'w', encoding='utf-8')
	f.write(text)
	f.close()


def append_text_file(path, text):
	f = open(path, 'a', encoding='utf-8')
	f.write(text)
	f.close()


def read_text_file(path):
	f = open(path, 'r', encoding='utf-8')
	data = f.read()
	f.close()
	return data


if __name__ == '__main__':
	# tiny demo showing the basic pattern
	p = 'demo_assignment4.txt'
	write_text_file(p, 'Line1\n')
	append_text_file(p, 'Line2\n')
	print(read_text_file(p))

