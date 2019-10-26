from FileBinomiale import *

l=[9,2,13,43,2,3,5234,0,91,12]
def testConsIter():
	print("######## Test ConsIter #########")
	f = file_binomiale()
	f = ConsIter(f,l)
	print(f)
	f.printFile()

def testSupprMin():
	print("######## Test SupprMin #########")
	f = file_binomiale()
	f = ConsIter(f,l)
	print(">>>>>>>>>>> Avant suppression >>>>>>>>>>> ")
	f.printFile()
	print(">>>>>>>>>>> Apres suppression >>>>>>>>>>> ")
	f2 = f.SupprMin()
	print("f : ",f)
	print(f2)
	f2.printFile()

def testAjout():
	print("######## Test Ajout #########")
	f = file_binomiale()
	f = Ajout(f,3)
	print("Après ajout 3 : ")
	print(f)
	for i in range(0,10):
		f = Ajout(f,i)
	print("Après ajout [0,1...9] : ")	
	print(f)
	f.printFile()

def testUnion():
	print("######## Test Union #########")
	l1 = [3,54,24,2,5,10,9,0,10]
	l2 = [4,32,456,21,435,287,787,932,23]
	f = file_binomiale()
	f1 = ConsIter(f,l1)
	f2 = ConsIter(f,l2)
	print(">>>>>>>>>>> Avant Union >>>>>>>>>>> ")
	print("l1 = ",l1)
	print("f1 : ",f1)
	print("l2 = ",l2)   
	print("f2 : ",f2)
	f3 = UnionFile(f1,f2)
	print(">>>>>>>>>>> Apres Union >>>>>>>>>>> ")
	print(f3)
	f3.printFile()
	print("f1 : ",f1)
	print("f2 : ",f2)

# testConsIter()
# testSupprMin()
# testAjout()
testUnion()


