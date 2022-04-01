### comparisons are number 
def insertionSort(listOfNumbers):
	for index in range(1,len(listOfNumbers)):
		key=	index
		j=index-1
		while 	listOfNumbers[key]<	listOfNumbers[j] and j>=0:
			swapByIndex(key,j,listOfNumbers)
			key-=1
			j-=1			
	return 	listOfNumbers
			
			
			
def swapByIndex(firstIndex,secIndex,listOfNumbers):
				listOfNumbers[firstIndex],	listOfNumbers[secIndex]=	listOfNumbers[secIndex],	listOfNumbers[firstIndex]
				
		
l =[10,9,4,3,2,1,4,3,5,6,7,5,8,8,3,4,2,3,9,10,14]
print(insertionSort(l))

		
	
