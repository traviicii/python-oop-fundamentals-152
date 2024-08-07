from helper import d
# User class

class User():

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.friends = []
        self.posts = {}

    def __repr__(self): # returns a string
        return f"User({self.username})"

    def get_info(self):
        print(f"{self.username} can be contacted at {self.email}")

    def change_pword(self, new_pword):
        self.password = new_pword

    def add_friend(self, friend): # adding functionality to add to a User's firend list, friend is expected to be another User object in this case
        if isinstance(friend, User):
            print(f"Adding {friend.username} to {self.username}'s friend list!")
            self.friends.append(friend)
        else:
            print("Hmmm, looks like that's not a valid user!")

    # view friendslist
    def friends_list(self):
        d()
        print(f"{self.username}'s Friend List")
        for friend in self.friends:
            print(friend.username)
        d()
    
    def login(self):
        logged_in.append(self)

    def logout(self):
        logged_in.remove(self)

    # create a post
    def create_post(self):
        while True:
            caption = input("Enter a caption for your post: \n")
            if len(caption) > 250:
                print("Hey that's way too long for this fake Twitter site!")
                continue
            new_id = self.new_id()
            self.posts[new_id] = caption
            break
    
    # create a new id for creating a new post based of of what the last greate number is in my post keys
    def new_id(self):
        last_id = 0
        for key in self.posts.keys():
            if key > last_id:
                last_id = key
        return last_id + 1
    

logged_in = []

travis = User("traviscpeck@codingtemple.com", "traviicii", '123456789')
gamel = User('someemail@email.com', 'Gamel78', 'g123')
zabdiel = User('zabsauce@email.com', 'sauce', 'saucysalamander')
kareem = User('kareemthedream@gmail.com', 'ksmooth', 'dreamcatcher123')

travis.add_friend(gamel)
travis.add_friend(zabdiel)
travis.add_friend(kareem)
print(travis.friends)

print(zabdiel in travis.friends)

travis.friends_list()

# travis.create_post()
# print(travis.posts)

travis.login()
zabdiel.login()
gamel.login()

print(logged_in)

travis.logout()
zabdiel.logout()
print(logged_in)