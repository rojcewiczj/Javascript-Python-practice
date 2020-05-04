class person:
    def __init__(self, name):
        self.height = "5'8"
        self.name = name
        self.favorite_topics = {1:"piano", 2:"martial arts", 3:"philosophy"}
    def conversation(self, other):
        if other.favorite_topics[1] == "piano":
            print(f"{self.name} and {other.name} discuss {other.favorite_topics[1]}")
        
        
Charles = person("Charles")
Pete = person("Pete")
print(Charles.height)
Charles.conversation(Pete)
