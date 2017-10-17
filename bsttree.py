from vision2 import *
class myTree:

	def additemintree(self):
		findkey=self.additeminputobj.text()
		findval=self.additeminputobj_2.text()
		if(findval==None ):
			self.treeinputboxobj.insertPlainText(findkey)
			self.additeminputobj.setText("")
			self.additeminputobj_2.setText("")
			dictionary.update({findkey : findval})
			self.treeinputboxobj.insertPlainText("\n")

			self.treeboolean=True
		else:
			if(self.treeboolean==True):
				self.treeinputboxobj.insertPlainText(" ")		
				self.treeinputboxobj.insertPlainText(findkey)
				self.treeinputboxobj.insertPlainText(" 		")
				self.treeinputboxobj.insertPlainText(findval)
				self.additeminputobj.setText("")
				self.additeminputobj_2.setText("")
				self.treeinputboxobj.insertPlainText("\n")
				self.ltree.append(int(findkey))
			else:
				self.treeinputboxobj.insertPlainText("You previosuly entered a key value pair")		


	def removeitemfromtree(self):
		findkey=self.removeiteminputobj.text()
		# lst=[int(i) for i in self.treeinputboxobj.toPlainText().split()]
		#print("list is", lst)
		#print("key is " + str(findkey))

		self.treeinputboxobj.setText("")

		try:
			self.ltree.remove(int(findkey))
			
		except:
			self.treeinputboxobj.setText("No such value found")
			#time.sleep(5)

		self.treeinputboxobj.setText("")

		for i in self.ltree:
			self.treeinputboxobj.insertPlainText(str(i))
			self.treeinputboxobj.insertPlainText(" ")

		self.removeiteminputobj.setText("")

	def removeallthings(self):
		self.inorderoutputobj.setText("")
		self.preorderoutputobj.setText("" )
		self.postorderoutputobj.setText("" )
		self.noofnodeobj.setText("")
		self.smallestitemobj.setText("")
		self.largestestitemobj.setText("")
		self.heightoftreeobj.setText("")
		self.treeinputboxobj .setText("")

		b=LBST()
		b.delete(b.root)
		self.openvisionwindow()

	def dotree(self):
		#lst2=[str(i) for i in self.treeinputboxobj.toPlainText().split()]
		
		# str=self.treeinputboxobj.toPlainText().split())
		# for i in 1,len(str)-1:
		# 	lst.append(str[i])
		
		#lst2.remove(lst2[0])
		#lst2.remove(lst2[1])
		
		#lst=[]
		#for i in lst2:
		#	lst.append(int(i))

		self.inorderoutputobj.setText("")
		self.preorderoutputobj.setText("" )
		self.postorderoutputobj.setText("" )
		self.noofnodeobj.setText("")
		self.smallestitemobj.setText("")
		self.largestestitemobj.setText("")
		self.heightoftreeobj.setText("")
		

		if(self.treeboolean) : 
			d=KVBST()
			#d.delete(d.root)

			for i in self.dtree:
				d.insert(int(i),int(self.dtree[i]))
			
			treesize=d.size()

			int_lst=[]
			int_lst=d.inorder()
			self.inorderoutputobj.insertPlainText("key 	Value\n")
			for i in range(0,treesize*2,2):
				self.inorderoutputobj.insertPlainText(str(int_lst[i]) )
				self.inorderoutputobj.insertPlainText(" 	 ")
				self.inorderoutputobj.insertPlainText(str(int_lst[i+1]) )
				self.inorderoutputobj.insertPlainText(" \n")

			int_lst=[]
			int_lst=d.preorder()
			self.preorderoutputobj.insertPlainText("key 	Value\n")
			for i in range(0,treesize*2,2):
				self.preorderoutputobj.insertPlainText(str(int_lst[i]) )
				self.preorderoutputobj.insertPlainText(" 	 ")
				self.preorderoutputobj.insertPlainText(str(int_lst[i+1]) )
				self.preorderoutputobj.insertPlainText(" \n")

			int_lst=[]
			int_lst=d.postorder()
			self.postorderoutputobj.insertPlainText("key 	Value\n")
			for i in range(0,treesize*2,2):
				self.postorderoutputobj.insertPlainText(str(int_lst[i]) )
				self.postorderoutputobj.insertPlainText(" 	 ")
				self.postorderoutputobj.insertPlainText(str(int_lst[i+1]) )
				self.postorderoutputobj.insertPlainText(" \n")

			self.noofnodeobj.insert(str(d.size()))
			self.smallestitemobj.insert(str(d.min_key()))
			self.largestestitemobj.insert(str(d.max_key()))
			self.heightoftreeobj.insert(str(d.height(d.root)))
		

			self.searchtreebtnobj.show()	
			self.searchtreeresultobj.show()
			self.viskeyvalbtnobj.show()	
			# self.viskeybtnobj.hide()

			self.viskeyvalbtnobj.setStyleSheet("background-color:orange;")
			self.viskeybtnobj.setStyleSheet("background-color:orange;")

		else:
			print(self.ltree)
			b=LBST()
			b.delete(b.root)
			
			for i in self.ltree:
				b.insert(i)
		
			int_lst=[]
			int_lst=b.inorder(int_lst)
			for i in int_lst:
				self.inorderoutputobj.insertPlainText(str(i) )
				self.inorderoutputobj.insertPlainText(" ")

			int_lst=[]
			b.preorder(int_lst)
			for i in int_lst:
				self.preorderoutputobj.insertPlainText(str(i) )
				self.preorderoutputobj.insertPlainText(" ")

			int_lst=[]
			b.postorder(int_lst)
			for i in int_lst:
				self.postorderoutputobj.insertPlainText(str(i) )
				self.postorderoutputobj.insertPlainText(" ")
		
			self.noofnodeobj.insert(str(b.size()))
			self.smallestitemobj.insert(str(b.min_key()))
			self.largestestitemobj.insert(str(b.max_key()))
			self.heightoftreeobj.insert(str(b.height(b.root)))
		
			self.searchtreebtnobj.show()	
			self.searchtreeresultobj.show()
			#self.viskeyvalbtnobj.show()	
			self.viskeybtnobj.show()

			self.viskeyvalbtnobj.setStyleSheet("background-color:orange;")
			self.viskeybtnobj.setStyleSheet("background-color:orange;")
	
	def searchavalue(self):
		
		if(self.treeboolean):
			d=KVBST()
			for i in self.dtree:
				d.insert(int(i),int(self.dtree[i]))
			findkey=self.searchtreeresultobj.text()
			if(d.contains( int(findkey) ) ):
				self.searchtreeresultobj.setText("Value Found.")
			else:
				self.searchtreeresultobj.setText("No Value Found.")	

		
		else:
			b=LBST()
			for i in self.ltree:
				b.insert(i)
			findkey=self.searchtreeresultobj.text()
			if(b.contains( int(findkey) ) ):
				self.searchtreeresultobj.setText("Value Found.")
			else:
				self.searchtreeresultobj.setText("No Value Found.")	


	def handletreefile(self):
		filename,garbage_value_returning_ignore_it=QtWidgets.QFileDialog.getOpenFileName(self,'open a text file')

		#------------------
		A=fileclass()
		self.treeboolean,lic,filename=A.getInput(filename)
		#print(filename)
		# 		if "txt" in filename:		
		# 			file=open(filename,"r")
		# 			self.treeinputboxobj.setText("")
		# self.treeinputboxobj.setText("")
		
		self.treeinputboxobj.setText("")

		if(self.treeboolean==True):
			self.dtree=lic
			self.treeinputboxobj.insertPlainText("Key 	Value\n")		
			for i in lic:
				self.treeinputboxobj.insertPlainText(str(i))
				self.treeinputboxobj.insertPlainText("	 ")
				self.treeinputboxobj.insertPlainText(str(lic[i]))
				self.treeinputboxobj.insertPlainText("\n")

		else:
			self.ltree=lic
			print(self.ltree)
			self.treeinputboxobj.insertPlainText("Key\n")		
			for i in lic:
				self.treeinputboxobj.insertPlainText(str(i))
				self.treeinputboxobj.insertPlainText(" ")
		# 	int_lst=[]
		# 	for line in file:
		# 		int_lst.extend([int(i) for i in line.split()])




		# 	for i in range(len(int_lst)):
		# 		self.treeinputboxobj.insertPlainText(str(int_lst[i]))
		# 		self.treeinputboxobj.insertPlainText(" ")
		# else:
		# 	self.treeinputboxobj.insertPlainText("Insert a valid file. Only text files are supported.")

	def visualize_keybst(self):
		
		b=LBST()
		for i in self.ltree:
			b.insert(i)
		self.drawtreeL(b,b.root,False)
	

	def visualize_keyvaluebst(self):
		d=KVBST()
		for i in self.dtree:
			d.insert(int(i),int(self.dtree[i]))
		self.drawtreeKV(d,d.root,False)

	
	def drawtreeKV(self,b,root,max20):
		def jumpto(x, y):
			t.penup()
			t.goto(x, y)
			t.pendown()

		def draw_square(x,y,t2):

			t2.forward(x)
			t2.right(90)
			t2.forward(y)
			t2.right(90)
			t2.forward(x)
			t2.right(90)
			t2.forward(y)


			
		def jumptowithcircle(x, y,val):
			turtle.penup()
			turtle.goto(x,y)
			turtle.pendown()
			if(len(str(val)) < 2) :
			    radius=16*len(str(val))
			else :
				radius=10*len(str(val))
			#radius=12*len(str(val))
			t2=turtle.Pen()
			t2.pendown()
			t2.begin_fill()
			t2.penup()
			if(len(str(val)) < 2) :
				t2.goto(x-30,y+28)
				t2.pendown()
				draw_square(70,25,t2)
			else:
				t2.goto(x-40,y+28)
				t2.pendown()
				draw_square(80,25,t2)

			t2.color('black')
			t2.end_fill()
			t2.penup()
			t2.hideturtle()
		
			jumpto(x,y)

		def jumpwithoutline(x,y):
			t.goto(x,y)

		def draw(node, x, y, dx):
			if node:
				t.goto(x, y)
				jumptowithcircle(x, y-15,node.key)
				t.pencolor("orange")
				t.write(str(node.key)+"," + str(node.val), align='center', font=('Time New Roman', 15, 'normal'))
				t.pencolor("black")
				draw(node.left, x-dx, y-120, dx/3+30)
				jumpto(x, y-20)
				draw(node.right, x+dx, y-120, dx/2+10)

		def exitonesc():
			turtle.bye()
			turtle.mainloop()

		t = turtle.Turtle()
		turtle.screensize(2000,1500)
		speedinput=turtle.numinput("Speed", "Enter the speed of the animation (in miliseconds)", 20, minval=10, maxval=10000)/100

		oldx,oldy=turtle.pos()
		turtle.penup()
		turtle.goto(-20 ,300)
		turtle.write("speed  =   "+ str(speedinput*100) + " ms",font=20)
		turtle.pendown()

		t.speed(speedinput)
		turtle.delay(speedinput*10)
		b=KVBST()
		h = b.height(root)

		turtle.penup()
		turtle.goto(0,30*h)
		jumpto(0, 30*h)
		turtle.pendown()
		draw(root, -10, 30*h, 40*h)

		turtle.penup()
		turtle.goto(-20,275)
		turtle.write("Press Escape key to exit",font=15)
		turtle.pendown()

		if max20==True :
			turtle.penup()
			turtle.goto(-20,250)
			turtle.write("Too much elements in the list. Only showing some of them",font=15)
			turtle.pendown()

		turtle.onkeypress(exitonesc,"Escape")
		turtle.listen()    


		t.hideturtle()
		turtle.mainloop()

	def drawtreeL(self,b,root,max20):
		def jumpto(x, y):
			t.penup()
			t.goto(x, y)
			t.pendown()

		def jumptowithcircle(x, y,val):
			turtle.penup()
			turtle.goto(x,y)
			turtle.pendown()
			if(len(str(val)) < 2) :
			    radius=16*len(str(val))
			else :
				radius=10*len(str(val))
			#radius=12*len(str(val))
			t2=turtle.Pen()
			t2.pendown()
			t2.begin_fill()
			t2.penup()
			if(len(str(val)) < 2) :
				t2.goto(x,y)
			else:
				t2.goto(x,y-10)
			t2.pendown()
			t2.circle(radius,None,None)
			t2.color('black')
			t2.end_fill()
			t2.penup()
			t2.hideturtle()
		
			jumpto(x,y)

		def jumpwithoutline(x,y):
			t.goto(x,y)

		def draw(node, x, y, dx):
			if node:
				t.goto(x, y)
				jumptowithcircle(x, y-20,node.key)
				t.pencolor("orange")
				t.write(node.key, align='center', font=('Time New Roman', 15, 'normal'))
				t.pencolor("black")
				draw(node.left, x-dx, y-80, dx/2+10)
				jumpto(x, y-20)
				draw(node.right, x+dx, y-60, dx/2+10)

		def exitonesc():
			turtle.bye()
			turtle.mainloop()

		t = turtle.Turtle()
		turtle.screensize(2000,1500)
		speedinput=turtle.numinput("Speed", "Enter the speed of the animation (in miliseconds)", 20, minval=10, maxval=10000)/100

		oldx,oldy=turtle.pos()
		turtle.penup()
		turtle.goto(-20 ,300)
		turtle.write("speed  =   "+ str(speedinput*100) + " ms",font=20)
		turtle.pendown()

		t.speed(speedinput)
		turtle.delay(speedinput*10)

		
		h = b.height(root)

		turtle.penup()
		turtle.goto(0,30*h)
		jumpto(0, 30*h)
		turtle.pendown()
		draw(root, -10, 30*h, 40*h)

		turtle.penup()
		turtle.goto(-20,275)
		turtle.write("Press Escape key to exit",font=15)
		turtle.pendown()

		if max20==True :
			turtle.penup()
			turtle.goto(-20,250)
			turtle.write("Too much elements in the list. Only showing some of them",font=15)
			turtle.pendown()

		turtle.onkeypress(exitonesc,"Escape")
		turtle.listen()    


		t.hideturtle()
		turtle.mainloop()
