paragraph ="thethe fox is in the house the"

text ="the"

def match_string(text,paragraph):
		i=0
		index_array =[]
		while i < len(paragraph):
			if paragraph[i:i+len(text)]==text:
				index_array.append((i,i+len(text)))
				i+= len(text)
			else:
				i+=1
		return index_array

	
def count():
				pass	
				

def cap_match_string(paragraph,index_array):
	answer = list(paragraph)
	for index_pair in index_array:
		for index in range(index_pair[0],index_pair[1]):
		     		answer[index]=answer[index].upper()
		
       		
	answer ="".join(answer)
	return answer
		
		

if __name__  =="__main__":
	print(cap_match_string(paragraph,match_string(text,paragraph)))
	


