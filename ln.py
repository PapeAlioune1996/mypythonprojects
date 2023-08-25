class User:
    def __init__(self, name, email):
       self.name = name
       self.email = email

alice = User("Alice", "alice@example.com")
alice.email = "contact@alice.com"
print(alice.email)