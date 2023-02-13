from pygame import mixer


class Sound:

    def __init__(self):
        mixer.init()


    def missle_shot(self):
        
        missle_effect = mixer.Sound('sound/mshot.wav')
        missle_effect.set_volume(0.3)
        missle_effect.play()
    
    def jet_explosion(self):
        explosion_effect = mixer.Sound('sound/explosion.wav')
        explosion_effect.set_volume(0.4)
        explosion_effect.play()

    def playback(self):
        chanela = mixer.Channel(1)
        playback_effect = mixer.Sound('sound/playback.wav')
        playback_effect.set_volume(0.7)
        chanela.play(playback_effect,loops=-1)

    def crashsound(self):
        crash_effect = mixer.Sound('sound/crash.wav')
        crash_effect.set_volume(0.5)
        crash_effect.play()
