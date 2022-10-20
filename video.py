from tkinter import *
from tkinter import filedialog
from os import link
from pytube import YouTube



def download_file():

    link = link_field.get()

    youtube_1 = YouTube(link)

    videos = youtube_1.streams.all()

    print(youtube_1.title)

    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    print()
    strm = int(input("enter no: "))
    videos[strm].download()
    print('video has download successfully')




screen = Tk()
title = screen.title('Youtube Video Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo_img = PhotoImage(file='download.png')

logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)


link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))



canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

download_btn = Button(screen, text="Download File", command=download_file)

canvas.create_window(250, 390, window=download_btn)




screen.mainloop()





##link = input("Paste a link: ")

#link = link_field.get()


#youtube_f = YouTube(link)

#print(youtube_f.title)

#videos = youtube_f.streams.all()


#vid = list(enumerate(videos))
#for i in vid:
 #   print(i)
#print()
#strm = int(input("enter no: "))
#videos[strm].download()


