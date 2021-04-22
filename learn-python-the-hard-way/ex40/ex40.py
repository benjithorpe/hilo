class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

twinkle_little_star =["Twinkle twinkle, little star", 
                      "How I wondered what you are",
                      "Up above the world so high",
                      "Like a diamond in the sky!"]
twinkle_twinkle = Song(twinkle_little_star)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

twinkle_twinkle.sing_me_a_song()
