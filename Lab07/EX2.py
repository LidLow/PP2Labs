import pygame

import os
os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab07")

#Music
_songs = ["Songs\Best of Luck.mp3", "Songs\Dark Horse.mp3", "Songs\Adrenaline.mp3"]

def NextSong():
    temp = _songs[0]
    _songs.pop(0)
    _songs.append(temp)

def PreviousSong():
    temp = _songs[-1]
    _songs.pop(-1)
    _songs.insert(0, temp)


pygame.init()

screen = pygame.display.set_mode((948, 672))
image = pygame.image.load(r"Pictures\image.png")
done = False 

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

while not done:    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_e) or event.type == SONG_END:  
            current = pygame.mixer.music.load(rf'{_songs[0]}')
            pygame.mixer.music.play(0)
            NextSong()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:  
            current = pygame.mixer.music.load(rf'{_songs[0]}')
            pygame.mixer.music.play(0)
            PreviousSong()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            pygame.mixer.music.unpause()
            
        screen.blit(image, (0, 0))

        pygame.display.flip()