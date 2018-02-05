"""
Cool Text Maker
By Luke Raus
"""

DATA = dict()
DATA['A'] = ['0110','1001','1111','1001','1001']
DATA['B'] = ['1110','1001','1110','1001','1110']
DATA['C'] = ['0111','1000','1000','1000','0111']
DATA['D'] = ['1110','1001','1001','1001','1110']
DATA['E'] = ['1111','1000','1110','1000','1111']
DATA['F'] = ['1111','1000','1110','1000','1000']
DATA['G'] = ['0111','1000','1011','1001','0110']
DATA['H'] = ['1001','1001','1111','1001','1001']
DATA['I'] = ['111','010','010','010','111']
DATA['J'] = ['1111','0001','0001','1001','0110']
DATA['K'] = ['1001','1010','1100','1010','1001']
DATA['L'] = ['1000','1000','1000','1000','1111']
DATA['M'] = ['10001','11011','10101','10001','10001']
DATA['N'] = ['10001','11001','10101','10011','10001']
DATA['O'] = ['0110','1001','1001','1001','0110']
DATA['P'] = ['1110','1001','1110','1000','1000']
DATA['Q'] = ['0110','1001','1001','1010','0111']
DATA['R'] = ['1110','1001','1110','1010','1001']
DATA['S'] = ['0111','1000','0110','0001','1110']
DATA['T'] = ['111','010','010','010','010']
DATA['U'] = ['1001','1001','1001','1001','0110']
DATA['V'] = ['10001','10001','01010','01010','00100']
DATA['W'] = ['10001','10001','10101','11011','10001']
DATA['X'] = ['10001','01010','00100','01010','10001']
DATA['Y'] = ['10001','01010','00100','00100','00100']
DATA['Z'] = ['11111','00010','00100','01000','11111']
DATA[' '] = ['00,','00','00','00','00']
DATA['0'] = ['0110','1101','1011','1001','0110']
DATA['1'] = ['110','010','010','010','111']
DATA['2'] = ['1110','0001','0010','0100','1111']
DATA['3'] = ['1110','0001','0111','0001','1110']
DATA['4'] = ['1001','1001','1111','0001','0001']
DATA['5'] = ['1111','1000','1110','0001','1110']
DATA['6'] = ['0110','1000','1110','1001','0110']
DATA['7'] = ['1111','0001','0010','0100','1000']
DATA['8'] = ['0110','1001','0110','1001','0110']
DATA['9'] = ['0110','1001','0111','0001','0001']
DATA['.'] = ['0','0','0','0','1']
DATA[','] = ['0','0','0','1','1']
DATA['!'] = ['1','1','1','0','1']
DATA['?'] = ['1110','0001','0010','0000','0010']
DATA[':'] = ['0','1','0','1','0']
DATA[';'] = ['0','1','0','1','1']
DATA["'"] = ['1','1','0','0','0']
DATA['-'] = ['000','000','111','000','000']
DATA['_'] = ['000','000','000','000','111']
DATA['='] = ['000','111','000','111','000']
DATA['+'] = ['000','010','111','010','000']
DATA['/'] = ['00001','00010','00100','01000','10000']
DATA['#'] = ['01010','11111','01010','11111','01010']

def cooltext(uncool): # cooltext.cooltext('Heck ya')
	"""Returns cool text as an array of strings.
	Precondition: uncool is string"""

	output = []
	for item in range(len(DATA['A'])):
		output.insert(0, ' ' * item) # Staggered initialization for alignment
	
	for letter in uncool.upper():
		item_num = 0
		if not letter in DATA: # Any unimplemented input chars replaced by '#'
			letter = '#'
		for item in DATA[letter]:
			for char in item:
				if char == '0':
					output[item_num] += '  '
				elif char == '1':
					output[item_num] += '_/'
			output[item_num] += '  ' # Inter-character spacing
			item_num += 1
	
	return output

if __name__ == '__main__':
	userinput = raw_input('\nUncool text to be made cool: ')
	coolinput = cooltext(userinput)
	print
	for x in coolinput:
		print x