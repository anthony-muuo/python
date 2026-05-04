# creating classes and using it!
class User:
    # initialize attributes of the class
    def __init__(self, user_id, username):
        self.id = user_id
        self.name= username
        self.followers = 0
        self.following = 0
        
    # creating a method
    def follow(self, user):
        user.followers += 1
        self.following += 1




user_1 = User("001", "Ducci")
user_2 = User("002", "Anto")

user_1.follow(user_2)

print(f"User1 followers: {user_1.followers}")
print(f"User1 following: {user_1.following}")
print(f"User2 followers: {user_2.followers}")
print(f"User2 following: {user_2.following}")