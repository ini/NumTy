def decimalToBase(num, base):
	num = int(num)
	if (num == 0):
		return "0"
	elif (num < 0):
		return "-" + decimalToBase(-num, base)
	if (base == 1):
		return '1' * num
	elif (base == 10):
		return str(num)
	elif (base < 1):
		return
		
	exp = -1
	while (base ** exp <= num):
		exp += 1
	
	remainder = num
	newBase = ""
	for x in xrange (0, exp + 1):
		divisor = int(remainder / (base ** (exp - x)))
		if (divisor < 10):
			newBase += str(divisor)
		else:
			newBase += chr(divisor + 55)
		remainder = remainder % (base ** (exp - x))
	return newBase

def baseToDecimal(num, base):
	num = str(num)
	if (num == "0"):
		return 0
	elif (num[0] == "-"):
		return -1 * baseToDecimal(num[1:], base)
	if (base == 10):
		return int(num)
	elif (base < 1):
		return
	
	decimalNum = 0
	for exp in xrange(0, len(num)):
		coefficient = 0
		if (num[exp].isalpha()):
			coefficient = ord(num[exp]) - 55
		else:
			coefficient = int(num[exp])
		decimalNum += coefficient * base ** (len(num) - exp - 1)
	return decimalNum

def baseToBase(num, oldBase, newBase):
	return decimalToBase(baseToDecimal(num, oldBase), newBase)
