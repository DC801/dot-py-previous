#!bin/python3

import os

users = []

with open('/etc/passwd', 'r') as file:
	for line in file:
		users.append(line.strip('\n').split(':'))
enabled = []

for user in users:
	if user[-1].endswith('sh'):
		print(user[0])
