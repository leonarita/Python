from pygame import mixer

mixer.init()

mixer.music.load("PYA-HUA-IKRAAR-HUA.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' to volume")
    print("Press 'e' to exit")

    ch = input("['p', 'r', 'v', 'e']>>>")

    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        mixer.music.set_volume(v)
    elif ch == "e":
        mixer.music.stop()
        break