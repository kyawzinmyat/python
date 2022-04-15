import sys

#def get_name(case):
	#for i in range(case):		
	#	print(deter(sys.stdin.readline().strip(),i+1))
		
	
		
def get_ruler():
	case = int(input())
	for i in range(case):		
		print(deter(input(),i+1))

		
		
		
def deter(kn,num):
	
	vowel =["a","e","i","o","u","A","E","I","O","U"]
	last = kn[-1]
	if last in vowel:
		return 'Case #%d: %s is ruled by %s.' % (num , kn,"Bob")
	elif last.lower() =="y":
		return 'Case #%d: %s is ruled by %s.' % (num , kn,"nobody")
	
	return 'Case #%d: %s is ruled by %s.' % (num ,kn,"Alice" )
		
	
get_ruler()

#print(("K").lower())