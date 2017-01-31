# Create a GUI -Order Up! that presents the user with a simple  restaurant menu, which price_lists items and prices. Let the user select different items then show the user the total bill


from Tkinter import *

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.tax=0.65
		self.create_widgets()
		
	def create_widgets(self):
		Label(self,text="Menu").grid(row=0,column=0, sticky=W)
		Label(self,text="Breakfast Items").grid(row=1,column=0,sticky=W)
		Label(self,text="Price(Each or per pound)").grid(row=1,column=2, sticky=W)
		#Label(self,text="Selection").grid(row=1,column=6, sticky=W)
		Label(self,text="Quantity or pound").grid(row=1,column=7, sticky=W)
		Label(self,text="Lunch").grid(row=8, column=0,sticky=W)
		Label(self,text="Dinner").grid(row=16, column=0,sticky=W)
		
		# Create Check Buttons for items
		self.cb_ft=BooleanVar()
		Checkbutton(self, text="French Toast",variable=self.cb_ft,command=self.bill).grid(row=2, column=0,sticky=W)
		self.cb_bc=BooleanVar()
		Checkbutton(self,text="Bagel'O Cremecheese",variable=self.cb_bc,command=self.bill).grid(row=3, column=0,sticky=W)
		self.cb_cft=BooleanVar()
		Checkbutton(self, text="Coffee/Tea",variable=self.cb_cft,command=self.bill).grid(row=4,column=0,sticky=W)
		self.cb_js=BooleanVar()
		Checkbutton(self, text="Juices/Shakes", variable=self.cb_js,command=self.bill).grid(row=5,column=0, sticky=W)
		self.cb_dn=BooleanVar()
		Checkbutton(self, text="Donught", variable=self.cb_dn,command=self.bill).grid(row=6,column=0, sticky=W)
		self.cb_mf=BooleanVar()
		Checkbutton(self, text="Muffin", variable=self.cb_mf,command=self.bill).grid(row=7,column=0, sticky=W)
		#Price for breakfast
		self.price_list=[]
		Label(self,text="$6.30").grid(row=2, column=2, sticky=W)
		self.price_list.append(6.30)
		Label(self,text="$1.85").grid(row=3, column=2, sticky=W)
		self.price_list.append(1.85)
		Label(self,text="$1.63").grid(row=4, column=2, sticky=W)
		self.price_list.append(1.63)
		Label(self,text="$2.35").grid(row=5, column=2, sticky=W)
		self.price_list.append(2.35)
		Label(self,text="$0.85").grid(row=6, column=2, sticky=W)
		self.price_list.append(0.85)
		Label(self,text="$1.39").grid(row=7, column=2, sticky=W)
		self.price_list.append(1.39)
		
		# Lunch
		self.cb_lc=BooleanVar()
		Checkbutton(self, text="Lamb Chop", variable=self.cb_lc,command=self.bill).grid(row=9,column=0, sticky=W)
		self.cb_hbg=BooleanVar()
		Checkbutton(self, text="Ham Burger",variable=self.cb_hbg,command=self.bill).grid(row=10,column=0,sticky=W)
		self.cb_sd=BooleanVar()
		Checkbutton(self, text="Salad", variable=self.cb_sd,command=self.bill).grid(row=11,column=0, sticky=W)
		self.cb_cnd=BooleanVar()
		Checkbutton(self, text="Chicken Noodles", variable=self.cb_cnd,command=self.bill).grid(row=12,column=0, sticky=W)
		self.cb_gbg=BooleanVar()
		Checkbutton(self,text="Garden Burger",variable=self.cb_gbg,command=self.bill).grid(row=13, column=0,sticky=W)
		self.cb_P=BooleanVar()
		Checkbutton(self, text="Pasta",variable=self.cb_P,command=self.bill).grid(row=14, column=0,sticky=W)
		self.cb_wc=BooleanVar()
		Checkbutton(self, text="Water/Coke", variable=self.cb_wc,command=self.bill).grid(row=15,column=0, sticky=W)
		
		#Price for Lunch
		Label(self,text="$6.39").grid(row=9, column=2, sticky=W)
		self.price_list.append(6.39)
		Label(self,text="$2.00").grid(row=10, column=2, sticky=W)
		self.price_list.append(2.00)
		Label(self,text="$0.65").grid(row=11, column=2, sticky=W)
		self.price_list.append(0.65)
		Label(self,text="$4.40").grid(row=12, column=2, sticky=W)
		self.price_list.append(4.40)
		Label(self,text="$3.35").grid(row=13, column=2, sticky=W)
		self.price_list.append(3.35)
		Label(self,text="$5.99").grid(row=14, column=2, sticky=W)
		self.price_list.append(5.99)
		Label(self,text="$1.89").grid(row=15, column=2, sticky=W)
		self.price_list.append(1.89)
		
		# Dinner
		self.cb_cs=BooleanVar()
		Checkbutton(self, text="Chicken Soup", variable=self.cb_cs,command=self.bill).grid(row=17,column=0, sticky=W)
		self.cb_tkr=BooleanVar()
		Checkbutton(self, text="Turkey Rice",variable=self.cb_tkr,command=self.bill).grid(row=18,column=0,sticky=W)
		self.cb_clg=BooleanVar()
		Checkbutton(self, text="Cauliflower Rice", variable=self.cb_clg,command=self.bill).grid(row=19,column=0, sticky=W)
		self.cb_chr=BooleanVar()
		Checkbutton(self, text="Chicken Rice", variable=self.cb_chr,command=self.bill).grid(row=20,column=0, sticky=W)
		
		#Price for Dinner
		Label(self,text="$2.40").grid(row=17, column=2, sticky=W)
		self.price_list.append(2.40)
		Label(self,text="$2.80").grid(row=18, column=2, sticky=W)
		self.price_list.append(2.80)
		Label(self,text="$3.50").grid(row=19, column=2, sticky=W)
		self.price_list.append(3.50)
		Label(self,text="$4.60").grid(row=20, column=2, sticky=W)
		self.price_list.append(4.60)
		# price_list of Quantity/weight
		
		self.e1=Entry(self)
		self.e1.grid(row=2, column=7, sticky=W)
		
		self.e1.insert(0,"0")
		self.e2=Entry(self)
		self.e2.grid(row=3, column=7, sticky=W)
		self.e2.insert(0,"0")
		self.e3=Entry(self)
		self.e3.grid(row=4, column=7, sticky=W)
		self.e3.insert(0,"0")
		self.e4=Entry(self)
		self.e4.grid(row=5, column=7, sticky=W)
		self.e4.insert(0,"0")
		self.e5=Entry(self)
		self.e5.grid(row=6, column=7, sticky=W)
		self.e5.insert(0,"0")
		self.e6=Entry(self)
		self.e6.grid(row=7, column=7, sticky=W)
		self.e6.insert(0,"0")
		self.e7=Entry(self)
		self.e7.grid(row=9, column=7, sticky=W)
		self.e7.insert(0,"0")
		self.e8=Entry(self)
		self.e8.grid(row=10, column=7, sticky=W)
		self.e8.insert(0,"0")
		self.e9=Entry(self)
		self.e9.grid(row=11, column=7, sticky=W)
		self.e9.insert(0,"0")
		self.e10=Entry(self)
		self.e10.grid(row=12, column=7, sticky=W)
		self.e10.insert(0,"0")
		self.e11=Entry(self)
		self.e11.grid(row=13, column=7, sticky=W)
		self.e11.insert(0,"0")
		self.e12=Entry(self)
		self.e12.grid(row=14, column=7, sticky=W)
		self.e12.insert(0,"0")
		self.e13=Entry(self)
		self.e13.grid(row=15, column=7, sticky=W)
		self.e13.insert(0,"0")
		self.e14=Entry(self)
		self.e14.grid(row=17, column=7, sticky=W)
		self.e14.insert(0,"0")
		self.e15=Entry(self)
		self.e15.grid(row=18, column=7, sticky=W)
		self.e15.insert(0,"0")
		self.e16=Entry(self)
		self.e16.grid(row=19, column=7, sticky=W)
		self.e16.insert(0,"0")
		self.e17=Entry(self)
		self.e17.grid(row=20, column=7, sticky=W)
		self.e17.insert(0,"0")
	
	
		Button(self, text="Submit",command=self.bill).grid(row=22, column=0, sticky=W)
		# Text widget to show the Bill
		
		self.t=Text(self,width=40, height=100, wrap=WORD)
		self.t.grid(row=23,column=0,sticky=W)
		
		
		
	def bill(self):
		amt=0.0
		items=[]
		rate=[]
		quant_weight=[]
		if 	self.cb_ft: 
		
			a=self.e1.get()
			a1=float(a) # Quantity/weight	
			amt=amt+(self.price_list[0])*a1
			
	
		if self.cb_bc:
			
			b=self.e2.get()
			b1=float(b)
			
			amt+=(self.price_list[1])*(b1)
		
		if self.cb_cft:
			
			c=self.e3.get()
			c1=float(c)
			
			amt+=(self.price_list[2])*(c1)
		
		if self.cb_js:
			
			d=self.e4.get()
			d1=float(d)
			
			amt+=(self.price_list[3])*d1
		
		if self.cb_dn:
			
			e=self.e5.get()
			e1=float(e)
			
			amt+=(self.price_list[4])*e1
		
		if self.cb_mf:
			
			f=self.e6.get()
			f1=float(f)
			
			amt+=(self.price_list[5])*f1
			
		if self.cb_lc:
			
			g=self.e7.get()
			g1=float(g)
			
			amt+=(self.price_list[6])*g1
		
		if self.cb_hbg:
			
			h=self.e8.get()
			h1=float(h)
			amt+=(self.price_list[7])*h1
	
		if self.cb_sd:
			
			i=self.e9.get()
			i1=float(i)
			
			amt+=(self.price_list[8])*i1
		
		if self.cb_cnd:
			
			j=self.e10.get()
			j1=float(j)
			amt+=(self.price_list[9])*j1
			
		if self.cb_gbg:
			
			k=self.e11.get()
			k1=float(k)
			amt+=(self.price_list[10])*k1
	
		if self.cb_P:
			
			l=self.e12.get()
			l1=float(l)
			amt+=(self.price_list[11])*(l1)
			
		if self.cb_wc:
			
			m=self.e13.get()
			m1=float(m)

			amt+=(self.price_list[12])*(m1)
			
		if self.cb_cs:
			
			n=self.e14.get()
			n1=float(n)
			amt+=(self.price_list[13])*(n1)
		
		if self.cb_tkr:
			
			o=self.e15.get()
			o1=float(o)
		
			amt+=(self.price_list[14])*(o1)
	
		if self.cb_clg:
		
			q=self.e16.get()
			q1=float(q)
			amt+=(self.price_list[15])*(q1)
		
		if self.cb_chr:
			
			r=self.e17.get()
			r1=float(r)
			amt+=float(self.price_list[16])*float(r1)
		
		bill=0.0
		
		bill=amt+(amt*self.tax)
		
		bill_str=str(bill)
		
		Due=""
			
			
		Due+="Amount Due(inclusive of taxes): $"+bill_str
		
		self.t.delete(0.0,END)
		self.t.insert(0.0,Due)
		
		
		
		
		
	

		
		
		
		
		
		
		
		
		
		
		
		
		
# Main
root=Tk()
root.title("Order Up!")	
root.geometry("200x100")
app=Application(root)
root.mainloop()



