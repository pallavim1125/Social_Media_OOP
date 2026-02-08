# Polymorphism - many + forms


# 1.method overriding




# Syntax
# class c_n1:
   
#     def method1():
#         #implementation1


# class c_n2(c_n1):


#     def method1():
#         #implementation2


# obj1=c_n2()
# obj1.method1()






class media_player:
    def play(self):
        print("Playing media")


class audio_player(media_player):
    def play(self):
        print("Playing audio")


class video_player(media_player):
    def play(self):
        print("Playing video")


AP=audio_player()
AP.play()
VP=video_player()
VP.play()
