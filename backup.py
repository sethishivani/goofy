class Node1:
	def __init__(self,name,initmoney):
		self.name=name
		self.money=initmoney
		self.next=None
		self.prev=None
	def getmoney(self):
		return self.money
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
	def add(self,name,money):
		temp=Node1(name,money)
		find=self.head
		if find==None:
			self.head=temp
		else:
			while(find.next!=None):
				find=find.getNext()
			find.setNext(temp)
			temp.setPrev(find)
	def display(self,start):
		while(start.next!=None):
			print start.getmoney()
			start=start.getNext()
		print start.getmoney()
	

mylist=UnorderedList1()
mylist.add('ajay',31)
mylist.add('vijay',41)
mylist.add('lolu',51)
mylist.display(mylist.head)