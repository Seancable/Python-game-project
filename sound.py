from playsound import playsound
class Sound:
    def __init__(self):
        self.menu='MartiansTriumphant.wav'
        self.lvl_1='Sting1.wav'
        self.lvl_2='Sting2.wav'
        self.lvl_3='Sting3.wav'
        self.enemy='enemy_2.mp3'
        self.player='player.mp3'
        self.rick='rick_astley.mp3'
    def menu_song(self):
        playsound(self.menu)
    def lvl1_song(self):
        playsound(self.lvl_1)
    def lvl2_song(self):
        playsound(self.lvl_2)
    def lvl3_song(self):
        playsound(self.lvl_3)
    def enemy_song(self):
        playsound(self.enemy)
    def player_song(self):
        playsound(self.player)
    def rick_song(self):
        playsound(self.rick)

song=Sound()
song.rick_song()


