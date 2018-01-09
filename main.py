#from Tkinter import *
import Tkinter as tk
import urllib2
import urllib
import cStringIO
import webbrowser
import os
from BeautifulSoup import BeautifulSoup
from PIL import ImageTk, Image

class Product(object):
	def __init__(self, title, href, asin, price):
		self.title = title
		self.href = href
		self.asin = asin
		self.price = price
	
	
def callback(event):
	print "call callback"
    #webbrowser.open_new(event.widget.cget("text"))
    

url = 'file://' + urllib.quote(os.path.abspath("./amzsrch.html"))
page = urllib2.urlopen(url)
#print page.read()
soup = BeautifulSoup(page.read())
#print soup.prettify()



resultListFindParameters = "ul", {"id":"s-results-list-atf"}

#result_list = soup.find("ul", {"id":"s-results-list-atf"})
result_list = soup.find(resultListFindParameters)
#print result_list.prettify()




result1 = result_list.find("li", {"id":"result_1"})
result1Title = result1.find("h2")["data-attribute"]
result1Href = result1.find("a")["href"]
result1Asin = result1["data-asin"]
result1PriceSpan = result1.find("span", {"class":"sx-price sx-price-large"})
result1ImgSrc = result1.find("img")["src"]


file = cStringIO.StringIO(urllib.urlopen(result1ImgSrc).read())
img = Image.open(file)

root = tk.Tk()

tkimg = ImageTk.PhotoImage(img)
imglabel = tk.Label(root, image=tkimg, cursor="hand") #.grid(row=1, column=1)
#Label(root, text=result1Asin, borderwidth=2, relief="solid").grid(row=1,column=2)
#lbl = Label(root, text="hello", fg="blue", cursor="hand2")
imglabel.pack()
imglabel.bind("<Button-1>", callback)
#Label(root, text=result1Href).grid(row=1,column=3)
#Label(root, text=result1Title).grid(row=1,column=3)
#Label(root, text=result1PriceSpan.text[:-2] + '.' + result1PriceSpan.text[-2:]).grid(row=1,column=4)
#print result1PriceSpan


#root.pack()
root.mainloop()

#print result1Title
#print result1Href
#print result1Asin
#print result1PriceSpan.text[:-2] + '.' + result1PriceSpan.text[-2:]
#print "*"


#root = Tk()
#app = Application(master=root)
#app.mainloop()
#root.destroy()
