class warrior_state:
    def _init_ (self):
        self.can_strike = True
        self.countering = False
        self.striking = False
        self.balance = 10
        self.health = 10
    
    def counter(self, opponent):
        opponent.balance - 5
        if self.balance <= 5:
            self.balance += 5
    def strike(self, opponent):
        if self.balance == 10:
            if opponent.balance == 10:
                pass
                

    