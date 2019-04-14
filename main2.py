exec("""import sys
with open(sys.argv[1])as s:r=s.read()
j=p=T=R=0
t=[0]*999
def S(P,Q):
	global j,p,R;R+=j
	if r[R]==P:p+=1
	elif r[R]==Q:
		if p!=0:p-=1
		else:j=0
while R<len(r):
	c=r[R]
	if j==1:S('[',']')
	elif j==-1:S(']','[')
	elif c=='['and t[T]==0:j=0
	elif c==']'and t[T]!=0:j=-1
	else:A.':print(chr(t[T]),end='')A,':t[T]=ord(sys.read(1))A+':t[T]+=1A-':t[T]-=1A>':T+=1A<':T-=1
		R+=1""".replace('A',"\n		if c=='"))