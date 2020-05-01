import random

class warrior_state:
    def _init_ (self):
        self.can_strike = True
        self.countering = False
        self.striking = False
        self.balance = 10
        self.health = 10
    
    def counter(self, opponent):
        print("they strike!", self.health, self.balance)
        self.countering = True
        self.striking = False
        if opponent.striking == True:
            opponent.balance - 5
            if self.balance <= 5:
                self.balance += 5
    def strike(self, opponent):
        print("they counter", self.health, self.balance)
        self.countering = False
        self.striking = True
        if self.balance == 10:
            if opponent.balance == 10 and opponent.countering == False:
                opponent.health -= 2
                opponent.balance -= 2
            elif opponent.balance < 10 and opponent.balance > 5 and opponent.countering == False:
                opponent.health -= 3
                opponent.balance -= 3

warrior_one = warrior_state()
warrior_two = warrior_state()
warrior_one_moves = {1:  warrior_one.counter, 2: warrior_one.strike}

warrior_two_moves = {1:  warrior_two.counter, 2: warrior_two.strike}

warrior_one_choice = [1,2]

warrior_two_choice = [1,2]

# def fight():
#     while warrior_one.health > 0 or warrior_two.health > 0:
#          warrior_one_moves[random.choice(warrior_one_choice)](warrior_two)
#          warrior_two_moves[random.choice(warrior_two_choice)](warrior_one)
# fight()

    