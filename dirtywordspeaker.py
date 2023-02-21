#!/usr/bin/env python3

import os, time, random, pygame

pygame.mixer.init()

def play(sound, text):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    print(f"\033[38;2;42;214;205m{text}\033[0m")
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def curse():
    word = random.choice(['bastard', 'cunt', 'damn', 'fuck', 'vagina', 'motherfucker', 'tits', 'piss', 'cocksucker', 'ass', 'shit'])
    play(f'sounds/{word}.mp3', word.upper())
    time.sleep(0.5)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    play('sounds/1.mp3', 'Dirty Word Speaker - A good piece of software by Fat Man')
    play('sounds/2.mp3', 'Aughhh Yea Folks!   Its time to listen to some dirty words!\nPress any key to make me speak some dirty words...')
    input()
    while True:
        curse()


if __name__ == '__main__':
    main()
