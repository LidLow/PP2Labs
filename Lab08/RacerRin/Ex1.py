import pygame as zxc

import os
os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab08\RacerRin")

_songs = ["Songs\Best of Luck.mp3", "Songs\Dark Horse.mp3", "Songs\Adrenaline.mp3", "Songs\HIT ME UP.mp3", "Songs\Murder In My Mind.mp3", "Songs\\Upload Download.mp3"]

def NextSong():
    temp = _songs[0]
    _songs.pop(0)
    _songs.append(temp)

zxc.init()

SONG_END = zxc.USEREVENT + 1
zxc.mixer.music.set_endevent(SONG_END)
zxc.mixer.music.load(rf"{_songs[0]}")
zxc.mixer.music.play()

moto = zxc.image.load(r"Images\Motorcycle.png")

screen = zxc.display.set_mode((720, 720))
FPS = zxc.time.Clock()

isPressed = False
isRotated = 

while True:
    for event in  zxc.event.get():
        if event.type == zxc.QUIT:
            zxc.quit()
        if event.type == SONG_END:
            NextSong()
            zxc.mixer.music.load(rf"{_songs[0]}")
            zxc.mixer.music.play()

        if event.type == zxc.KEYDOWN and event.key == zxc.K_w:
            moto = zxc.transform.rotate(moto, 90)

    screen.fill((255, 255, 255))
    screen.blit(moto, (20, 20))

    zxc.display.flip()
    FPS.tick(60)