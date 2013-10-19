
# Computing GC Content
def gcContent(dnaString):
	dnaLen = len(dnaString)
	cgCount  = sum(isCG(char) for char in dnaString)
	gcContent  = 100*(cgCount/float(dnaLen))
	print gcContent
	return gcContent

def isCG(pChar):
	if pChar == "c" or pChar == "C" or pChar == "g" or pChar == "G": return True
	return False

#print gcContent("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")

##############################3
# POINT MUTATIONS (HAMMING DISTANCE)

def hammingDist(pString1, pString2):
	if not len(pString1) == len(pString2): return "ERROR: param length mismatch."
	return sum(not pString1[charIndex] == pString2[charIndex] for charIndex in range(len(pString1)))

print hammingDist("1234509876", "1234567890")


################################
# PROTEIN ENCODING
def proteinEncode(rnaString):
	rnaCodons = dict()
	rnaCodons = {
		"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V", \
		"UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V", \
		"UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A", \
		"UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A", \
		"UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D", \
		"UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E", \
		"UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G", \
		"UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"
		}
		
	# IMPORTANT: DOES NOT HANDLE CODON NOT FOUND OR EXCEPTIONS
	# DOES NOT HANDLE STOPS
	codonList = [rnaString[(3*codonNum):3+(3*codonNum)] for codonNum in range(len(rnaString)/3)]
	protein = "".join([rnaCodons[codon] for codon in codonList])
	return protein

#print proteinEncode("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")

##############################
# 

