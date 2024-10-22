def sumDig( n ):
	a = 0
	while n > 0:
		a = a + n % 10
		n = int(n / 10)

	return a

def isValidEMEI(n):
	s = str(n)
	l = len(s)
	if l != 15:
		return False

	d = 0
	sum = 0
	for i in range(15, 0, -1):
		d = (int)(n % 10)
		if i % 2 == 0:
			d = 2 * d

		sum = sum + sumDig(d)
		n = n / 10
	return (sum % 10 == 0)
n = 490154203237518
if isValidEMEI(n):
	print("Valid IMEI Code")
else:
	print("Invalid IMEI Code")
