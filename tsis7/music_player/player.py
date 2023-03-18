import pygame
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("MP3 Player")
root.geometry("500x300")

pygame.mixer.init()

# Add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='songs/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    song = song.replace("C:/Users/User/OneDrive/Документы/пп2/tsis7/music_player/songs/", "")
    song = song.replace(".mp3", "")

    song_box.insert(END, song)

# Add many songs to menu
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='songs/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song in songs:
        song = song.replace("C:/Users/User/OneDrive/Документы/пп2/tsis7/music_player/songs/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)


# Play Selected Song
def play():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/User/OneDrive/Документы/пп2/tsis7/music_player/songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


# Stop Playing Current Song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

global paused
paused = False

# Pause and Unpause the Current Song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# Play The Next Song in the Playlist
def forward():
    next_song = song_box.curselection()
    next_song = next_song[0]+1
    song = song_box.get(next_song)

    song = f'C:/Users/User/OneDrive/Документы/пп2/tsis7/music_player/songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar
    song_box.selection_clear(0, END)
    
    # Activate new song bar
    song_box.activate(next_song)

    # Set Active Bar to Next Song
    song_box.selection_set(next_song, last=None)


# Play the previous song 
def back():
    next_song = song_box.curselection()
    next_song = next_song[0]-1
    song = song_box.get(next_song)

    song = f'C:/Users/User/OneDrive/Документы/пп2/tsis7/music_player/songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar
    song_box.selection_clear(0, END)
    
    # Activate new song bar
    song_box.activate(next_song)

    # Set Active Bar to Next Song
    song_box.selection_set(next_song, last=None)


# Delete a Song
def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

# Delete All Songs 
def delete_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()

song_box = Listbox(root, bg = "black", fg="white", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady = 20)

controls_frame = Frame(root)
controls_frame.pack()
 
# Player Control Button Images
back_btn_img = PhotoImage(file='buttons/last.png')
forward_btn_img = PhotoImage(file='buttons/next.png')
play_btn_img = PhotoImage(file='buttons/play.png')
pause_btn_img = PhotoImage(file='buttons/pause.png')
stop_btn_img = PhotoImage(file='buttons/stop.png')

# Player Control Buttons
back_btn = Button(controls_frame, image=back_btn_img, borderwidth = 0, command=back)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth = 0, command=forward)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth = 0, command=play)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth = 0, command=lambda:pause(paused))
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth =  0, command=stop)

back_btn.grid(row=0, column=0, padx=7)
forward_btn.grid(row=0, column=1, padx=7)
play_btn.grid(row=0, column=2, padx=7)
pause_btn.grid(row=0, column=3, padx=7)
stop_btn.grid(row=0, column=4, padx=7)


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label = "Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
# Add manu songs 
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu = remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command = delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command = delete_all_songs)

root.mainloop()