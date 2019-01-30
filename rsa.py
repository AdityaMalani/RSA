import math
import random

def isPrime(num):
	for i in range(2,int(num/2)+1):
		if(num%i==0):
			return 0
	return 1

def calculateE(p,q,phi):
	list1 = []
	for e in range(2,phi):
		if math.gcd(e,phi) == 1:
			list1.append(e)
	return list1
	
def calculateD(phi,e):
	for d in range(1,phi):
		if (d*e)%phi is 1:
			return d
			
def charalgo(pt,e,n,d):
	print("Encrypting...")
	enc = []
	dec = []
	for i in pt:
		c = (ord(i)**e)%n
		enc.append(c)
	print("Encrpyted text = ",end='')
	print(enc)
	print("--------------------------------------")
	print("Decrypting...")
	for j in enc:
		m = (j**d)%n
		dec.append(chr(m))
	str1 = ''.join(dec)
	print("Decrpyted text = ",end='')
	print(str1)
			
	
	
def algo(data,e,n,d):
	print("Encrypting...")
	c = (data**e)%n
	print("Encrpyted data : "+str(c))
	print("--------------------------------------")
	print("Decrypting...")
	dec = (c**d)%n
	print("Decrypted data :"+str(dec))

def driver():
	p = int(input("Enter the first prime number:"))
	while isPrime(p)==0:
		p = int(input("Please enter the first PRIME number:"))
	q = int(input("Enter the second prime number:"))
	while isPrime(q)==0:
		q = int(input("Please enter the second PRIME number:"))
	n=p*q
	phi = (p-1)*(q-1)
	list1 = calculateE(p,q,phi)
	print(list1)
	e = random.choice(list1)
	print("Selected e = "+ str(e))
	d = calculateD(phi,e)
	print("Calculated d = " +str(d))
	print("Public key is (n="+str(n)+",e="+str(e)+")")
	print("Private key is (n="+str(n)+",d="+str(d)+")")
	print("--------------------------------------")
	pt = input('Enter message : ')
	if pt.isdigit():
		pt = int(pt)
		algo(pt,e,n,d)
	else:
		charalgo(pt,e,n,d)

driver()
	

