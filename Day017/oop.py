class User:
    #just creating a class
    def __init__(self,user_id,user_name):
        #it is a constructor
        self.id = user_id
        self.name = user_name
        self.following = 0
        self.followers = 0
        print("it will exicute every time when we create a obj from the User class")
        pass #pass is used to avoid error
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User(15,"tezo") # creating a object from a class
print(user_1.id) # accessing the id of the user_1
user_2 = User(16,"angela")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)