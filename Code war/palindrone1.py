
#[0,2][3,5]
#[1,2] [2,1]
# 12321

import math
#[0,2][2,4]
# [1,2] [2,1]
#1331
#13 31


print(4/2)
print(math.floor(5/2))


def test(num):
	mid = math.ceil(len(str(num))/2)
	num=str(num)
	suf = num[:mid]
	pre=num[mid:]	
	
	return suf,pre

	
		
def find_pal(num):
	return str(num)== str(num)[::-1] if isinstance(num,int) and 12/num>0  else False	
	
	
num=2321
print(str(num)==str(num)[::-1])
print(isinstance(num,int))	
print(test(12321))


print(find_pal(12332))

