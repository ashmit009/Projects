import tkinter

import pyshorteners


root=tkinter.Tk()
root.title("Ashmit URL SHORTNER")
root.geometry("500x500")

def shorten():
    shortner=pyshorteners.Shortener()
    short_url=shortner.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0,short_url))



longurl_label=tkinter.Label(root,text="Enter long url",fg="#A52A2A")
longurl_entry=tkinter.Entry(root)
shorturl_label=tkinter.Label(root,text="shortened url",fg="#00FFFF")
shorturl_entry=tkinter.Entry(root)
shorten_button=tkinter.Button(root,text="shorten url",command=shorten,fg="#4B0082")

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()

root.mainloop()