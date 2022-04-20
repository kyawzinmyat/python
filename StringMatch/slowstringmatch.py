paragraph ="the thefox is in the house"

text ="the"


# return the list of index of match text
def matchString(text,paragraph):
	answer_index_list=[]
	length_of_text,array_of_paragraph=init_requirements(text,paragraph)
	
	for index,string in enumerate(array_of_paragraph):
		length_of_string = len(string)
		if length_of_string >=length_of_text:
			text_counter=0
			string_counter=0
			while text_counter<length_of_text and string_counter < length_of_string:
				if string[string_counter] == text[text_counter]:
					text_counter+=1
					string_counter+=1
				else:
					string_counter+=1
				
			if text_counter == length_of_text:
				answer_index_list.append(index)	
			
	return answer_index_list



		
			
	
# capatalized the whole string that contain text	
def cap_match_string(text,paragraph,answer_index_list):
	new_paragraph = paragraph.split(" ")[:]
	for index in answer_index_list:
		new_paragraph[index]= new_paragraph[index].upper()
	
		
				
	answer =" ".join(new_paragraph)
	
	
	return answer

		
	
def init_requirements(text,paragraph):
	length_of_text = len(text)
	array_of_paragraph = paragraph.split(" ")
	return length_of_text,array_of_paragraph

	
# return the num of appeared text in paragraph	
def count(text,paragraph):
	
	return len(matchString(text,paragraph))


def run():
	print(cap_match_string(text,paragraph,matchString(text,paragraph)))


if __name__ =="__main__":
	
	
	
	run()
	print("The numbers of appearances are "+str(count(text,paragraph)))
	