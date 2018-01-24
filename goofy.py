import keysGen as kg

class Node1:
	def __init__(self,name,initmoney,iden,temp):
		self.name=name
		self.money=initmoney
		self.next=None
		self.prev=temp
		self.spent=0
		self.sign=None
		self.block=iden
	def getblock(self):
		return self.block
	def getmoney(self):
		return self.money
	def setspent(self):
		self.spent=1
	def getspent(self):
		return self.spent
	def getname(self):
		return self.name
	def getNext(self):
		return self.next
	def getPrev(self):
		return self.prev
	def setmoney(self,newmoney):
		self.money=newmoney
	def setNext(self,newnext):
		self.next=newnext
	def setPrev(self,newprev):
		self.prev=newprev


class UnorderedList1:
	def __init__(self):
		self.head=None
	def isEmpty(self):
		return self.head==None
	def add(self,name,money,iden,temp):
		temp=Node1(name,money,iden,temp)
		find=self.head
		if find==None:
			self.head=temp
		else:
			while(find.next!=None):
				find=find.getNext()
			find.setNext(temp)
			#temp.setPrev(find)
	def display(self,start):
		while(start!=None):
			print(start.getname(), start.getmoney(),start.getblock(),start.getspent())
			start=start.getNext()
		#print start.getmoney()
	def search(self,sender,money,reciever,idct):
		temp=self.head
		found=0
		while (temp!=None):
			#print(sender,money)
			if(temp.getname()==sender and int(temp.getmoney())>=(money) and temp.getspent()==0):
				found=1
				mylist.add(reciever,money,idct,temp)
				idct+=1
				mylist.add(sender,temp.getmoney()-money,idct,temp)
				print "found"
				temp.setspent();
				break;
			else:
				temp=temp.getNext();
		return found
	def checkUser(self,name,a_list):
		for i in range (0,len(userlist)):
				if(a_list[i][0]==name):
					return 1
		return 0


mylist=UnorderedList1()
userlist=[["goofy"]]
idcounter=0
if __name__ == '__main__':
	mylist.add('',0,idcounter,None)
	key=kg.keygen()
	userlist[0].extend(key)
	idcounter+=1
	while(1):
		flag=0
		print "1. Add money, 2. Make transaction, 3. Add user, 4. nd verify block, 5. View ledger, 6. exit, 7. View user key list"
		x = int(input("Enter a number: "))
		if(x==1):
			money = (int)(input("Enter a number: "))
			mylist.add("goofy",money,idcounter,None)
			idcounter+=1
		elif(x==2):
			sender = raw_input("Enter sender: ")
			if(mylist.checkUser(sender,userlist)==1):
				reciever = raw_input("Enter reciever: ")
				if(mylist.checkUser(reciever,userlist)==1):
					money = (int)(input("Enter a number: "))
					found=mylist.search(sender,money,reciever,idcounter)
					if(found==0):
						print "sender is "+sender
						if(sender=="goofy"):
							print "i am goofy"
							mylist.add("goofy",money,idcounter,None)
							idcounter+=1
							mylist.search(sender,money,reciever,idcounter)
							idcounter+=2
							print "Transaction Comleted"
						else:
							print "Invalid Transaction"
					else:
						#make transaction###########
						#mylist.add(reciever,money,idcounter)
						idcounter+=2
						#mylist.add(sender,temp.getmoney()-money,idcounter)
						#idcounter+=1
				else:
					flag=1
			else:
				flag=1
			if(flag==1):
				print "Invalid User"
		elif(x==3):
			user = raw_input("Enter user: ")
			key=kg.keygen()
			temp=[user]
			temp.extend(key)
			userlist.append(temp)
		elif(x==5):
			mylist.display(mylist.head)
		elif(x==6):
			break;
		elif(x==7):
			for i in range (0,len(userlist)):
				print(userlist[i][0],userlist[i][1],userlist[i][2])

		