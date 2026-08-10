from codon_table import codon_table

def main():
	#Possible Codon Point Mutations
	Silent = False;
	Nonsense = False;
	Missense = False;

	Insertion = False
	Deletion = False
	PointMutation = False

	Sequence1 = ""
	Sequence2 = ""

	userinput = input("Please Enter your first DNA Sequence: ")
	Sequence1 = userinput.upper()

	userinput = input("Please Enter your Second DNA Sequence: ")
	Sequence2 = userinput.upper()

	#Sequence1 = "ATGCCATGCTAAGCT"
	#Sequence2 = "ATGCCGTCTAAGCT" 

	#equence1 = "ATGCAC"
	#Sequence2 = "ATGAC"

	if(ValidDna(Sequence1)):
		print("Sequence 1 is Valid DNA")
	else:
		print("Sequence 1 is NOT Valid DNA")
		quit()

	if(ValidDna(Sequence2)):
		print("Sequence 2 is Valid DNA")
	else:
		print("Sequence 2 is NOT Valid DNA")
		quit()
	print("\n\n")

	if(checkLength(Sequence1,Sequence2)):
		print("DNA is the Same Length")
	else:
		print(f"DNA is Different Lengths\nSequence 1 DNA is {len(Sequence1)} Nucleotides long\nSequence 2 DNA is {len(Sequence2)} Nucleotides long")

	print("")

	#sets new strings to the new returned NeedleMan-Wunsch Algorithm results
	NewOrig,NewMuta = CheckEachNucleotide(Sequence1,Sequence2)

	print("")
	for index in range(len(NewOrig)):
		#if da top got a - then that means its an insertion
		if NewOrig[index] == "-":
			print(f"Insertion at pos {index}")
			Insertion = True
		#if the bottom got a - that means its a deletion
		elif NewMuta[index] == "-":
			print(f"Deletion at pos {index}")
			Deletion = True
		#if neither happened but theyre still different that means its a mutation
		elif NewOrig[index] != NewMuta[index]:
			print(f"Point mutation at pos {index}")
			PointMutation = True

	CheckMutationType(Sequence1,Sequence2)

#Checks if both are valid dna strings
#Valid DNA Codons contain A,T,C,G
#Returns true if valid
#Returns false if invalid 
def ValidDna(Check):
	IsValid = True
	for C in Check:
		if(not(C == "A" or C == "T" or C == "C" or C == "G")):
			IsValid = False;
			return IsValid
	return IsValid

#Checks if the length of 2 DNA are the same
#Returns true if They are the same
#Returns false if they are not the same
def checkLength(Orig,Muta):
	OrigLength = len(Orig)
	MutaLength = len(Muta)

	if (OrigLength == MutaLength):
		return True 
	else:
		return False

#Finds gaps using the NeedleMan-Wunsch Algorithm
#Just learned this off of a youtube video so
#Also This website
#https://bio.libretexts.org/Bookshelves/Computational_Biology/Book%3A_Computational_Biology_-_Genomes_Networks_and_Evolution_(Kellis_et_al.)/02%3A_Sequence_Alignment_and_Dynamic_Programming/2.05%3A_The_Needleman-Wunsch_Algorithm
#Lets hope it works
#Checks for insertions Or Deletions
def CheckEachNucleotide(Orig,Muta): 
	Col = len(Orig) +1
	Rows = len(Muta) +1

	GapPenalty = -1


	matrix = []
	#initialization

	#Create matrix
	for i in range(Rows):
		row = [0] * Col
		matrix.append(row)


	
	#initialize Row values
	for i in range(Rows):
		if(i != 0):
			matrix[i][0] = i*GapPenalty

	#initialize Col values
	for j in range(Col):
		if(j != 0):
			matrix[0][j] = j*GapPenalty

	#do the calculations for each matrix spot
	for i in range(Rows):
		for j in range(Col):
			if(i!= 0 and j!=0 ):
				reward = 1
				#if the two characters are not equal then you get a bad reward so this one wont win
				if(Orig[j-1] != Muta[i-1]):
					reward = -1
				

				diagonal = matrix[i-1][j-1]+ reward
				up = matrix[i-1][j] + GapPenalty
				left = matrix[i][j-1] + GapPenalty

				#compare all and take the biggest
				first = max(diagonal,up)
				#transitive rule or smthn
				second = max(first,left)

				matrix[i][j] = second
	#TraceBack From BottomRight
	NewOrig = []
	NewMuta = []

	i = Rows - 1
	j = Col - 1
	while i > 0 or j > 0:
		#can move diagonoly?
		if (i > 0 and j > 0):
			reward = 1
			if (Orig[j-1] != Muta[i-1]):
				reward = -1
			if(matrix[i][j] == matrix[i-1][j-1] + reward):
				NewOrig.append(Orig[j-1])
				NewMuta.append(Muta[i-1])

				i -=1
				j -=1
				continue
		# Can we move up?
		if i > 0 and matrix[i][j] == matrix[i-1][j] + GapPenalty:
			NewOrig.append("-")
			NewMuta.append(Muta[i-1])

			i -= 1
			continue

		# Otherwise, move left
		if j > 0 and matrix[i][j] == matrix[i][j-1] + GapPenalty:
			NewOrig.append(Orig[j-1])
			NewMuta.append("-")

			j -= 1

	#print matrix
	#for row in matrix:
	#	print(" ".join(f"{x:3}" for x in row))


	NewOrig.reverse()
	NewMuta.reverse()

	NewOrig = "".join(NewOrig)
	NewMuta = "".join(NewMuta)

	print("Results of the NeedleMan-Wunsch Algorithm:")
	print (NewOrig)
	print (NewMuta)
	print("--------------------")
	return NewOrig,NewMuta

def CheckMutationType(Orig,Muta):

	OrigNewRNA = Orig.replace("T", "U")
	MutaNewRNA = Muta.replace("T", "U")
	
	for i in range(0, len(OrigNewRNA), 3):

		codon = OrigNewRNA[i:i+3]

		if len(codon) < 3:
			print(f"Incomplete codon  {i}")
			continue

		amino_acid = codon_table[codon]
		print(codon, amino_acid)

if __name__ == "__main__":
	main()
