"""
Cool Text Maker
By MetaKor
"""

data     = ['01101001111110011001'] 		#A
data.append('11101001111010011110')			#B
data.append('01111000100010000111')			#C
data.append('11101001100110011110')			#D
data.append('11111000111010001111')			#E
data.append('11111000111010001000')			#F
data.append('01111000101110010110')			#G
data.append('10011001111110011001')			#H
data.append('111010010010111')				#I
data.append('11110001000110010110')			#J
data.append('10011010110010101001')			#K
data.append('10001000100010001111')			#L
data.append('1000111011101011000110001')	#M
data.append('1000111001101011001110001')	#N
data.append('01101001100110010110')			#O
data.append('11101001111010001000')			#P
data.append('01101001100110100111')			#Q
data.append('11101001111010101001')			#R
data.append('01111000011000011110')			#S
data.append('111010010010010')				#T
data.append('10011001100110010110')			#U
data.append('1000110001010100101000100')	#V
data.append('1000110001101011101110001')	#W
data.append('1000101010001000101010001')	#X
data.append('1000101010001000010000100')	#Y
data.append('1111100010001000100011111')	#Z
data.append('0000000000')					#
data.append('01101101101110010110')			#0
data.append('110010010010111')				#1
data.append('11100001001001001111')			#2
data.append('11100001011100011110')			#3
data.append('10011001111100010001')			#4
data.append('11111000111000011110')			#5
data.append('01101000111010010110')			#6
data.append('11110001001001001000')			#7
data.append('01101001011010010110')			#8
data.append('01101001011100010001')			#9
data.append('00001')						#.
data.append('00011')						#,
data.append('11101')						#!
data.append('11100001001000000010')			#?
data.append('01010')						#:
data.append('01011')						#;
data.append('11000')						#'
data.append('000000111000000')				#-
data.append('000000000000111')				#_
data.append('000111000111000')				#=
data.append('000010111010000')				#+
data.append('0000100010001000100010000')	#/

chars  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789.,!?:;'-_=+/"
binary = ['','','','','']
cool   = ['','','','','']

uncool = raw_input('\nUncool text to be made cool: ')
uncool = uncool.upper()

#makes binary array of uncool text in binary
for letter in uncool:
	cur_data = data[chars.index(letter)] #cur_data contains binary data for current char
	x = 0 #tracks place in char_data
	y = 0 #tracks line
	while x < len(cur_data):
		binary[y] = binary[y] + cur_data[x:x+(len(cur_data)/5)] + '0'
		x += len(cur_data)/5
		y += 1

#makes and prints cool text from binary array
item_num = 0
for item in binary:
	cool[item_num] = cool[item_num] + ' '*(len(binary)-item_num-1)
	for letter in binary[item_num]:
		if letter == '0':
			cool[item_num] = cool[item_num] + '  '
		elif letter == '1':
			cool[item_num] = cool[item_num] + '_/'
	print cool[item_num]
	item_num += 1
