# For pytube: https://pytube.io/en/latest/user/quickstart.html
# https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/
# https://www.geeksforgeeks.org/dropdown-menus-tkinter/


from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox


def download(url, type):
    try:
        yt = YouTube(url)
        if type == "mp4":
            stream = yt.streams.get_highest_resolution()
            downloaded_file = stream.download()
            title = yt.title
            new_file_name = title + ".mp4"
            os.rename(downloaded_file, new_file_name)
        elif type == "mp3":
            stream = yt.streams.get_audio_only()
            mp4_found = os.path.exists(stream.title + ".mp4")
            downloaded_file = stream.download()
            title = yt.title
            new_file_name = title + " (Audio).mp3"
            os.rename(downloaded_file, new_file_name)
            if mp4_found:
                stream = yt.streams.get_highest_resolution()
                downloaded_file = stream.download()
                title = yt.title
                new_file_name = title + ".mp4"
                os.rename(downloaded_file, new_file_name)
        messagebox.showinfo("Success", f"Downloaded {type.upper()} successfully!")
    except Exception as err:
        messagebox.showinfo("Failure", str(err))
        # raise SystemExit


def download_mp4():
    url = text_box_entry.get()
    download(url, "mp4")


def download_mp3():
    url = text_box_entry.get()
    download(url, "mp3")


# Create root window
root = Tk()

# Dimensions of Window
WIDTH = 700
HEIGHT = 150

# root window dimensions and title
root.title("YouTube Downloader")
root.configure(bg="white")
# root.eval('tk::PlaceWindow . center')

x = int((root.winfo_screenwidth() / 2) - (WIDTH / 2))
y = int((root.winfo_screenheight() / 2) - (HEIGHT / 2))
root.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
root.resizable(height=False, width=False)

# Add labels to the root window
input_label = Label(root, text="Enter YouTube URL: ", font=('Helvetica', 15))
input_label.configure(bg="white")
input_label.grid(column=0, row=0, padx=20, pady=10)

# Label for Choosing Download Type
download_label = Label(root, text="Choose (MP4 / MP3): ", font=('Helvetica', 15))
download_label.configure(bg="white")
download_label.grid(column=0, row=1, padx=0, pady=0)

# Add TextBox for the URL
text_box_entry = Entry(root, width=50, font=('Helvetica', 15))
text_box_entry.grid(column=1, row=0, padx=10, pady=10)
text_box_entry.configure(bg="white")

# Dropdown menu options
options = [
    "MP4",
    "MP3"
]

# storing the value selected to a variable
clicked = StringVar()

# initial menu text
clicked.set("MP4")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.configure(bg="white")
drop.grid(column=1, row=1, padx=0, pady=0)


def download_what():
    if clicked.get() == "MP4":
        download_mp4()
    elif clicked.get() == "MP3":
        download_mp3()


# Create button, it will do the download operation
button = Button(root, text="Download", command=download_what)
button.configure(bg="white")
button.grid(column=1, row=2, padx=100, pady=10)

# Execute Tkinter
root.mainloop()
