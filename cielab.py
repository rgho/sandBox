


def RGBtoXYZ(pRGBList):
	pRGBList


def XYZtoCIELAB(pXYZList):
	x = pXYZList[0]
	y = pXYZList[1]
	z = pXYZList[2]

	Yn = 1
	Xn = 1
	Zn = 1

	# y/Yn is used often in this conversion 
	# so we just precompute and store it in var yYn.
	yYn = y/Yn
	
	# FIND L*
	if yYn > 0.008856: 
		L = (116 * (yYn) ** (1/3)) - 16
	else:
		L = 903.3(yYn)

	a = 500 * (CIELAB_helper(x/Xn) - CIELAB_helper(yYn))
	b = 200 * (CIELAB_helper(yYn) - CIELAB_helper(z/Zn))



		

def CIELAB_helper(p):
	if p > 0.008856:
		return p**(1/3)
	else:
		return 7.787*p + 16/116



