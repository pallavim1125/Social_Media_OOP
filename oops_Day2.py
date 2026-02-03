class Instagram:
    def __init__(self,title,description,creator_name,location):
     self.title=title
     self.description=description
     self.creator_name=creator_name
     self.location=location
     self.likes=0
     self.comments=[]

    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_creator_name(self):
        print("The creator of the reel is ",self.creator_name)
    def display_location(self):
        print("The location of the reel is ",self.location)
    def display_likes(self):
        print("The number of likes on the reel is ",self.likes)
    def display_comments(self):
        print("Comments on the reel:",self.comments)
    
    def like_reel(self):
        self.likes += 1
    def unlike_reel(self):
        if self.likes > 0:
            self.likes -= 1
    def add_comment(self,comment):
        self.comments.append(comment)
    def remove_comment(self):
        if self.comments:
            removed = self.comments.pop()
            print(f"Removed comment: {removed}")
        else:
            print("No comments to remove.")


reel1 = Instagram("My First Reel", "This is a description of my first reel.","John Doe","New York")
reel1.display_title()
reel1.display_description()
reel1.display_creator_name()
reel1.display_location()
reel1.display_likes()
reel1.like_reel()
reel1.unlike_reel() 
reel1.add_comment("Great reel!")
reel1.add_comment("Awesome content!")   
reel1.display_comments()
reel1.remove_comment()
reel1.display_comments()