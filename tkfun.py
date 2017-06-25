from Tkinter import *
import urllib2
import webbrowser
import os




#class webScrape(object):
#    def __init__(self, queryString):
#        self.url = baseUrl+queryString
#        reponse urllib2.urlopen(self.url)
        
        


class Application(Frame):
    def search(self, event):
        #results = webScrape()
        
        url = 'https://www.google.com/#q='
        url=url+self.searchEntry.get()
        print url
        
        #for right now do now open url, the below code works fine
        #response = urllib2.urlopen(url+self.searchEntry.get())
        #html = response.read()
        #print html
        

    def createWidgets(self):
        self.searchEntry = Entry(self, text="type something here", width=30)
        self.searchEntry.bind('<Return>', self.search)
        self.searchEntry.pack({"side": "left"})

        self.searchBtn = Button(self, text="search")
        self.searchBtn.bind('<Button-1>', self.search)
        self.searchBtn.pack({"side": "left"})

#    def displaySearchResult():
        


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
#root.destroy()
