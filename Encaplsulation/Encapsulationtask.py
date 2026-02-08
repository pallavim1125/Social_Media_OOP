class InstagramAccount:
    def __init__(self, username, password, bio=""):
        self.username = username          
        self.bio = bio                    
        self.__password = password        
        self.__followers = 0              
        self.__following = 0             

    
    def get_followers(self):
        return self.__followers

    
    def get_following(self):
        return self.__following

    
    def follow(self):
        self.__following += 1
        print(f"{self.username} followed someone.")

    
    def gain_follower(self):
        self.__followers += 1
        print(f"{self.username} got a new follower!")

    
    def unfollow(self):
        if self.__following > 0:
            self.__following -= 1
            print(f"{self.username} unfollowed someone.")
        else:
            print("You are not following anyone.")


    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            if len(new_password) >= 6:
                self.__password = new_password
                print("Password updated successfully ✅")
            else:
                print("Password must be at least 6 characters.")
        else:
            print("Incorrect old password ❌")

    
    def view_profile(self):
        print("\n--- Instagram Profile ---")
        print("Username:", self.username)
        print("Bio:", self.bio)
        print("Followers:", self.__followers)
        print("Following:", self.__following)

acc1 = InstagramAccount("pallavi_11", "pass123", "Just a bio here!")

acc1.view_profile()


acc1.gain_follower()
acc1.gain_follower()


acc1.follow()

acc1.change_password("pass123", "newpass456")

acc1.view_profile()
