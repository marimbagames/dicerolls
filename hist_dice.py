def start_tracking():
	roll_dict = {}
	exp = { 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
	total_rolls = 0
	while True:
		roll_str = raw_input('Enter roll: ')
		roll = 0
		try:
			roll = int(roll_str)
		except ValueError:
			print bcolors.FAIL + 'Invalid input. Enter a number between 2 & 12' + bcolors.ENDC
			continue

		if roll != 0 and (roll < 2 or roll > 12):
			print bcolors.FAIL + 'Invalid input. Enter a number between 2 & 12' + bcolors.ENDC
			continue
		if roll == 0:
			print '\n'
			for key in sorted(roll_dict):
				print "%02d: " % key,
				print bcolors.OKBLUE,
				for _ in range(roll_dict[key]):
					print "*",
				print bcolors.ENDC,
				print bcolors.FAIL + "(%d, %d)" % (roll_dict[key], int(round(float(exp[key] * total_rolls) / 36.0))),
				print bcolors.ENDC
			return
		if roll in roll_dict:
			roll_dict[roll] = roll_dict[roll] + 1
		else:
			roll_dict[roll] = 1
		total_rolls = total_rolls + 1

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

if __name__ == '__main__':
	start_tracking()
