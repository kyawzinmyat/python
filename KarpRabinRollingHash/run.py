
from general_rolling_hash import RollingHash
from StringMatchwithRollingHash import KarpRabinStringMatch


## suggest use lower case at all bcz this fun captilize the matched string		



def test_rolling_hash():
	docs = "wasn't right. Was this the only feeling she'd have for over five years of hard work? It had been a simple realization that had changed Debra's life perspective. It was really so simple that she was embarrassed that she had lived the previous five years with the way she measured her worth. Now that she saw what she had been doing, she could see how sad it was. That made her all the more relieved she had made the change. The number of hearts her Instagram posts received wasn't any longer the indication of her own self-worth."

	pattern ="It had been a simple realization that had changed Debra's life perspective. It was really so simple that she was embarrassed that she had lived the previous five years with the way she measured her worth. Now that she saw what she had been doing, she could see how sad it was. That made her all the more relieved she had made the change. The number of hearts her Instagram posts received wasn't any longer the indication of her own self-worth."
	rh = RollingHash(docs,pattern)
	
	print(rh.roll())
	#cap_index(docs,rh.roll())

	

				
def test_karprabin_string_match():	
	docs = "wasn't right. Was this the only feeling she'd have for over five years of hard work? It had been a simple realization that had changed Debra's life perspective. It was really so simple that she was embarrassed that she had lived the previous five years with the way she measured her worth. Now that she saw what she had been doing, she could see how sad it was. That made her all the more relieved she had made the change. The number of hearts her Instagram posts received wasn't any longer the indication of her own self-worth."
	pattern ="It had been a simple realization that had changed Debra's life perspective. It was really so simple that she was embarrassed that she had lived the previous five years with the way she measured her worth. Now that she saw what she had been doing, she could see how sad it was. That made her all the more relieved she had made the change. The number of hearts her Instagram posts received wasn't any longer the indication of her own self-worth."
	
	kr= KarpRabinStringMatch(pattern,docs)
	
	#cap_index(docs,kr.match())
	
	
	

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


