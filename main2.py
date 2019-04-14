import sys
with open(sys.argv[1]) as s:
	r=s.read()
j=p=T=R=0
t=[0]*999
def S(fro,to):
	global j,p,R
	R+=j
	if r[R]==fro:p+=1
	elif r[R]==to:
		if p!=0:p-=1
		else:j=0
while R<len(r):
	c=r[R]
	if j==1:S('[',']')
	elif j==-1:S(']','[')
	elif c=='['and t[T]==0:j=0
	elif c==']'and t[T]!=0:j=-1
	else:
		if c=='.':print(chr(t[T]),end='')
		if c==',':t[T]=ord(sys.read(1))
		if c=='+':t[T]+=1
		if c=='-':t[T]-=1
		if c=='>':T+=1
		if c=='<':T-=1
		R+=1
