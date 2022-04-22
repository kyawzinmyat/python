
from general_rolling_hash import RollingHash
from StringMatchwithRollingHash import KarpRabinStringMatch


## suggest use lower case at all bcz this fun captilize the matched string		



def test_rolling_hash():
	docs = "jkjklmn abcdef gh i"
	pattern ="jkjklmn a"
	rh = RollingHash(docs,pattern)
	
	cap_index(docs,rh.roll())

	

				
def test_karprabin_string_match():
	docs="the fox is in thethe house"
	pattern ="the"
	kr= KarpRabinStringMatch(pattern,docs)
	
	cap_index(docs,kr.match())
	
	
	

def cap_index(docs,index_list):
	answer = list(docs)
	for index_pair in index_list:
		for index in range(index_pair[0],index_pair[1]):
			answer[index]=answer[index].upper()
	answer = "".join(answer)
	print(answer)
	
	
	
if __name__ =="__main__":
	test_rolling_hash()	
	test_karprabin_string_match()


