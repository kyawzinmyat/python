myan_list =['၀','၁','၂','၃','၄','၅','၆','၇','၈','၉']
user_list=input('enter the num--')
length = len(user_list)
for i in (user_list):
	user_list=user_list.replace(i,myan_list[int(i)])
print(user_list)
