import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QImage, QPalette, QBrush,QPixmap
from PyQt5.QtCore import QSize,pyqtSignal
import time,turtle
from bst import *
from tree import *
from treefiling import fileclass


qtCreatorFile = "vision.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	


#-----------------------------------------------------opening windows code----------------------------------------------


	def openvisionwindow(self):
		#show only vision widget , hide all others
		self.vision_widget.show()
		self.vision_sorting_widget.hide()
		self.vision_dp_01_widget.hide()
		self.vision_dp_widget.hide()
		self.vision_tree_widget.hide()
		self.vision_dp_matrix_widget.hide()

		self.dsobj.setMouseTracking(1)


		self.vision_widget.setStyleSheet("background-color:dark-Cyan;")
		self.label_3.setStyleSheet("color:Yellow;")
		self.label_4.setStyleSheet("color:Yellow;")
		self.dpobj.setStyleSheet("background-color:gray;")
		self.sortingobj.setStyleSheet("background-color:gray;")
		self.dsobj.setStyleSheet("background-color:gray;")

		self.vision_widget.setGeometry(QtCore.QRect(0,0,1322,849))

		if self.dsobj.underMouse()==True :
			#print("i am here")
			self.label_3.setStyleSheet("color:orange;")


		self.dpobj.clicked.connect(self.opendpwindow)
		self.dsobj.clicked.connect(self.opentreewindow)
		self.sortingobj.clicked.connect(self.opensortingwindow)


	def opendpwindow(self):
		#show only dp widget , hide all others
		self.vision_widget.hide()
		self.vision_sorting_widget.hide()
		self.vision_dp_01_widget.hide()
		self.vision_dp_widget.show()
		self.vision_tree_widget.hide()
		self.vision_dp_matrix_widget.hide()

		self.vision_dp_widget.setGeometry(QtCore.QRect(0,0,1312,848))
		
		self.vision_dp_matrix_btn_obj.clicked.connect(self.opendpmatrixwindow)
		self.vision_dp_01_btn_obj.clicked.connect(self.opendp01window)
		self.gobackobj.clicked.connect(self.openvisionwindow)
	
	def opendpmatrixwindow(self):
		#show only vision widget , hide all others
		self.vision_widget.hide()
		self.vision_sorting_widget.hide()
		self.vision_dp_01_widget.hide()
		self.vision_dp_widget.hide()
		self.vision_tree_widget.hide()
		self.vision_dp_matrix_widget.show()

		self.vision_dp_matrix_widget.setGeometry(QtCore.QRect(0,0,1312,848))

		self.gobackobjfromatrixchain.clicked.connect(self.opendpwindow)
	
	def opendp01window(self):
		#show only dp widget , hide all others
		self.vision_widget.hide()
		self.vision_sorting_widget.hide()
		self.vision_dp_01_widget.show()
		self.vision_dp_widget.hide()
		self.vision_tree_widget.hide()
		self.vision_dp_matrix_widget.hide()


		self.vision_dp_01_widget.setGeometry(QtCore.QRect(0,0,1312,848))
		
		self.filebtnobj.clicked.connect(self.handlesortingfile)
		self.sortbtnobj.clicked.connect(self.dosorting)
		self.gobackobjfrom01.clicked.connect(self.opendpwindow)


	def doitenter(self,mwidget,mfunction):
		mwidget.returnPressed.connect(mfunction)

	def opentreewindow(self):
		#show only vision widget , hide all others
		self.vision_widget.hide()
		self.vision_sorting_widget.hide()
		self.vision_dp_01_widget.hide()
		self.vision_dp_widget.hide()
		self.vision_tree_widget.show()
		self.vision_dp_matrix_widget.hide()

		self.vision_tree_widget.setGeometry(QtCore.QRect(0,0,1312,848))

		self.searchtreebtnobj.hide()	
		self.searchtreeresultobj.hide()	
		self.viskeyvalbtnobj.hide()	
		self.viskeybtnobj.hide()	

		

		self.gobackfromtree.clicked.connect(self.removeallthings)
		self.viskeyvalbtnobj.clicked.connect(self.visualize_keyvaluebst)
		self.viskeybtnobj.clicked.connect(self.visualize_keybst)
		self.uploadtreefilebtnobj.clicked.connect(self.handletreefile)
		self.dotreebtnobj.clicked.connect(self.dotree)
		self.searchtreebtnobj.clicked.connect(self.searchavalue)
		self.additembtnobj.clicked.connect(self.additemintree)
		self.removeitembtnobj.clicked.connect(self.removeitemfromtree)

		self.doitenter(self.additeminputobj,self.additemintree)
		self.doitenter(self.additeminputobj_2,self.additemintree)
		self.doitenter(self.removeiteminputobj,self.removeitemfromtree)
		self.doitenter(self.searchtreeresultobj,self.searchavalue)


	def opensortingwindow(self):
		#show only vision widget , hide all others
		self.vision_widget.hide()
		self.vision_sorting_widget.show()
		self.vision_dp_01_widget.hide()
		self.vision_dp_widget.hide()
		self.vision_tree_widget.hide()
		self.vision_dp_matrix_widget.hide()
		self.txtobj.setText("")
		self.outputsortobj.setText("")

		self.vision_sorting_widget.setGeometry(QtCore.QRect(0,0,1312,848))
		
		self.filebtnobj.clicked.connect(self.handlesortingfile)
		self.sortbtnobj.clicked.connect(self.dosorting)
		self.gobackobjfromsorting.clicked.connect(self.openvisionwindow)


#-----------------------------------------------------SORTING CODE----------------------------------------------

	def handlesortingfile(self):
		#insert ahmed file sorting input code here
		self.txtobj.setText("")

		start=time.clock()
		#self.txtobj.insertPlainText("Reading...")


		#------------------
		filename,garbage_value_returning_ignore_it=QtWidgets.QFileDialog.getOpenFileName(self,'open a text file')
		self.outputsortobj.setText("")
		#print(filename)
		if ".txt" in filename:		
			file=open(filename,"r")
			self.txtobj.setText("")

			
			int_lst=[]
			for line in file:
				int_lst.extend([int(i) for i in line.split()])

			last=time.clock()
			elapsed=last-start
			#self.txtobj.insertPlainText(str(elapsed))



			for i in int_lst:
				self.txtobj.insertPlainText(str(i))
				self.txtobj.insertPlainText(" ")
		else:
			self.txtobj.insertPlainText("Insert a valid file. Only text files are supported.")

	def dosorting(self):
		self.outputsortobj.insertPlainText("Sorting...")

		start=time.clock()

		int_lst=[int(i) for i in self.txtobj.toPlainText().split()]


		
		if(len(int_lst)!=0):
			sortchoice = self.sortchoiceobj.currentIndex()
			ascordesc = self.ascordescobj.currentIndex()
			sortchoicestr=""

			t=MyTree()
			if(sortchoice==0):
				sortchoicestr="Bubble sort"
				if(ascordesc==0):
					t.Bubblesort(int_lst)
				else:
					t.RBubblesort(int_lst)

			elif(sortchoice==1):
				sortchoicestr="Selection sort"
				# if(ascordesc==0):
				# 	t.selectionsort(int_lst)
				# else:
				# 	t.Rselectionsort(int_lst)

			elif(sortchoice==2):
				sortchoicestr="Insertion sort"
				if(ascordesc==0):
					t.insertionsort(int_lst)
				else:
					t.Rinsertionsort(int_lst)

			elif(sortchoice==3):
				sortchoicestr="Merge sort"
				if(ascordesc==0):
					t.mergesort(int_lst)
				else:
					t.Rmergesort(int_lst)

			elif(sortchoice==4):
				sortchoicestr="Quick sort"
				# if(ascordesc==0):
				# 	t.quicksort(int_lst)
				# else:
				# 	t.Rquicksort(int_lst)


			elif(sortchoice==5):
				sortchoicestr="Heap sort"
				if(ascordesc==0):
					t.heapsort(int_lst)
				else:
					t.Rheapsort(int_lst)

			done=time.clock()
			elapsed=0.0
			elapsed=done-start
			self.outputsortobj.setText("")
			self.outputsortobj.append(sortchoicestr + " \n")
			self.outputsortobj.append( "Number of items in the liste = ")
			self.outputsortobj.insertPlainText(str(len(int_lst)))
			self.outputsortobj.append("\n")

			self.outputsortobj.append("Sorted array : \n")
			for i in range(len(int_lst)):
				self.outputsortobj.insertPlainText(str(int_lst[i]) )
				self.outputsortobj.insertPlainText(" ")
			self.outputsortobj.append(" \nThe total time taken by this algorithm to sort the given list = " )

			self.outputsortobj.insertPlainText(str(elapsed))


#-----------------------------------------------------BST visualization code----------------------------------------------

	def additemintree(self):
		findkey=self.additeminputobj.text()
		findval=self.additeminputobj_2.text()
		
		# if(self.treeboolean==True):
		# 	if(findval==None ):
		# 		self.treeinputboxobj.insertPlainText(findkey)
		# 		self.additeminputobj.setText("")
		# 		self.additeminputobj_2.setText("")
		# 		dictionary.update({findkey : findval})
		# 		self.treeinputboxobj.insertPlainText("\n")
		# 		self.treeboolean=False
		# else:
		# 	if(self.treeboolean==True):
		# 		self.treeinputboxobj.insertPlainText(" ")		
		# 		self.treeinputboxobj.insertPlainText(findkey)
		# 		self.treeinputboxobj.insertPlainText("    ")
		# 		self.treeinputboxobj.insertPlainText(findval)
		# 		self.additeminputobj.setText("")
		# 		self.additeminputobj_2.setText("")
		# 		self.treeinputboxobj.insertPlainText("\n")
		# 		self.ltree.append(int(findkey))
		# 	else:
		# 		self.treeinputboxobj.insertPlainText("You previosuly entered a key value pair")		



		if(self.treeboolean):
			if(findval is not None):
				self.treeinputboxobj.insertPlainText(findkey)
				self.treeinputboxobj.insertPlainText("    ")
				self.treeinputboxobj.insertPlainText(findval)
				self.treeinputboxobj.insertPlainText("\n")
				self.additeminputobj.setText("")
				self.additeminputobj_2.setText("")
				dictionary.update({findkey : findval})
			else:
				self.treeinputboxobj.setText("Key-Value check box unchecked. Please check the box")

		else:
			if(findval is None):
				self.treeinputboxobj.insertPlainText(" ")
				self.treeinputboxobj.insertPlainText(findkey)
				self.treeinputboxobj.insertPlainText(" ")
				self.additeminputobj.setText("")
				self.additeminputobj_2.setText("")
				self.ltree.append(int(findkey))
			else:
				self.treeinputboxobj.setText("Key-Value check box checked. Please uncheck the box")


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
		

		# if(self.treeboolean) : 
		# 	d=KVBST()
		# 	#d.delete(d.root)

		# 	for i in self.dtree:
		# 		d.insert(int(i),int(self.dtree[i]))
			
		# 	treesize=d.size()

		# 	int_lst=[]
		# 	int_lst=d.inorder()
		# 	self.inorderoutputobj.insertPlainText("key 	Value\n")
		# 	for i in range(0,treesize*2,2):
		# 		self.inorderoutputobj.insertPlainText(str(int_lst[i]) )
		# 		self.inorderoutputobj.insertPlainText(" 	 ")
		# 		self.inorderoutputobj.insertPlainText(str(int_lst[i+1]) )
		# 		self.inorderoutputobj.insertPlainText(" \n")

		# 	int_lst=[]
		# 	int_lst=d.preorder()
		# 	self.preorderoutputobj.insertPlainText("key 	Value\n")
		# 	for i in range(0,treesize*2,2):
		# 		self.preorderoutputobj.insertPlainText(str(int_lst[i]) )
		# 		self.preorderoutputobj.insertPlainText(" 	 ")
		# 		self.preorderoutputobj.insertPlainText(str(int_lst[i+1]) )
		# 		self.preorderoutputobj.insertPlainText(" \n")

		# 	int_lst=[]
		# 	int_lst=d.postorder()
		# 	self.postorderoutputobj.insertPlainText("key 	Value\n")
		# 	for i in range(0,treesize*2,2):
		# 		self.postorderoutputobj.insertPlainText(str(int_lst[i]) )
		# 		self.postorderoutputobj.insertPlainText(" 	 ")
		# 		self.postorderoutputobj.insertPlainText(str(int_lst[i+1]) )
		# 		self.postorderoutputobj.insertPlainText(" \n")

		# 	self.noofnodeobj.insert(str(d.size()))
		# 	self.smallestitemobj.insert(str(d.min_key()))
		# 	self.largestestitemobj.insert(str(d.max_key()))
		# 	self.heightoftreeobj.insert(str(d.height(d.root)))
		

		# 	self.searchtreebtnobj.show()	
		# 	self.searchtreeresultobj.show()
		# 	self.viskeyvalbtnobj.show()	
		# 	# self.viskeybtnobj.hide()

		# 	self.viskeyvalbtnobj.setStyleSheet("background-color:orange;")
		# 	self.viskeybtnobj.setStyleSheet("background-color:orange;")

		# else:
		# 	print(self.ltree)
		# 	b=LBST()
		# 	b.delete(b.root)
			
		# 	for i in self.ltree:
		# 		b.insert(i)
		
		# 	int_lst=[]
		# 	int_lst=b.inorder(int_lst)
		# 	for i in int_lst:
		# 		self.inorderoutputobj.insertPlainText(str(i) )
		# 		self.inorderoutputobj.insertPlainText(" ")

		# 	int_lst=[]
		# 	b.preorder(int_lst)
		# 	for i in int_lst:
		# 		self.preorderoutputobj.insertPlainText(str(i) )
		# 		self.preorderoutputobj.insertPlainText(" ")

		# 	int_lst=[]
		# 	b.postorder(int_lst)
		# 	for i in int_lst:
		# 		self.postorderoutputobj.insertPlainText(str(i) )
		# 		self.postorderoutputobj.insertPlainText(" ")
		
		# 	self.noofnodeobj.insert(str(b.size()))
		# 	self.smallestitemobj.insert(str(b.min_key()))
		# 	self.largestestitemobj.insert(str(b.max_key()))
		# 	self.heightoftreeobj.insert(str(b.height(b.root)))
		
		# 	self.searchtreebtnobj.show()	
		# 	self.searchtreeresultobj.show()
		# 	#self.viskeyvalbtnobj.show()	
		# 	self.viskeybtnobj.show()

		# 	self.viskeyvalbtnobj.setStyleSheet("background-color:orange;")
		# 	self.viskeybtnobj.setStyleSheet("background-color:orange;")
		


		if(self.treeboolean==True):
			if(self.kvchkobj.checkState()):
				d=KVBST()
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
				self.treeinputboxobj.setText("Key-Value check box not checked.Please check the box")
				ltree=[]
				dtree={}

		else:
			if(self.kvchkobj.checkState()):
				self.treeinputboxobj.setText("Key-Value check box not checked.Please check the box")
				ltree=[]
				dtree={}
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
			if(self.kvchkobj.checkState()):
				self.dtree=lic
				self.treeinputboxobj.insertPlainText("Key 	Value\n")		
				for i in lic:
					self.treeinputboxobj.insertPlainText(str(i))
					self.treeinputboxobj.insertPlainText("	 ")
					self.treeinputboxobj.insertPlainText(str(lic[i]))
					self.treeinputboxobj.insertPlainText("\n")
			else:
				ltree=[]
				dtree={}
				buttonReply = QMessageBox.question(self, "Key-Value check box not checked.Please check the box", QMessageBox.Yes, QMessageBox.No)
#         		if buttonReply == QMessageBox.Yes:
#             		print('Yes clicked.')
#         		else:
#             		print('No clicked.')
#             	msg.setText("Key-Value check box not checked.Please check the box")
# #				self.treeinputboxobj.setText("Key-Value check box not checked.Please check the box")
		else:
			if(self.kvchkobj.checkState()):
				ltree=[]
				dtree={}
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("Key-Value check box checked. Please uncheck the box")
				self.treeinputboxobj.setText("Key-Value check box checked. Please uncheck the box")
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



#-----------------------------------------------------PYQT CODE----------------------------------------------


	def __init__(self,b):
		self.ltree=[]
		self.dtree={}
		self.treeboolean=False
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.b=b
		#show only vision widget , hide all others
		self.vision_widget.show()
		self.vision_sorting_widget.hide()
		self.vision_dp_01_widget.hide()
		self.vision_dp_widget.hide()
		self.vision_tree_widget.hide()
		self.vision_dp_matrix_widget.hide()
		self.vision_widget.setGeometry(QtCore.QRect(0,0,1322,1000))
		


		#self.dsobj=HoverButton(self)
		#buttons
		self.dpobj.clicked.connect(self.opendpwindow)
		self.dsobj.clicked.connect(self.opentreewindow)
		self.sortingobj.clicked.connect(self.opensortingwindow)
		


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	b=None
	window = MyApp(b)
	window.show()
	sys.exit(app.exec_())







#-----------------------------------------------------Commented code----------------------------------------------














"""
class Hover(QtGui.QLabel):
	def __init__(self, parent):
		QtGui.QLabel.__init__(self,parent)


class HoverButton(QPushButton):
	mouseHover = pyqtSignal(bool)

	def __init__(self, parent=None):
		QPushButton.__init__(self, parent)
		self.setMouseTracking(True)

	def enterEvent(self, event):
		self.mouseHover.emit(True)

	def leaveEvent(self, event):
		self.mouseHover.emit(False)
"""




'''
		#styling
		self.vision_widget.setStyleSheet("background-color:black;")
		self.label_3.setStyleSheet("color:Yellow;")
		self.label_4.setStyleSheet("color:Yellow;")
		self.dpobj.setStyleSheet("background-color:blue;")
		self.sortingobj.setStyleSheet("background-color:blue;")
		self.dsobj.setStyleSheet("background-color:blue;")


		if self.dsobj.underMouse()==True :
			print("i am here")
			self.label_3.setStyleSheet("color:black;")
		if self.vision_widget.underMouse()==True:
			print("here")
			self.label_4.setStyleSheet("color:black;")

		
	def func(self):
		self.dsobj.setStyleSheet("background-color:orange;")

	def mouseMoveEvent(self, event):
			print ("i am here")

'''
