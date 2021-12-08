class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.total = 0
    
    def deposit(self, amount, description=None):
        self.total += amount
        if description == None:
            self.description = ""
        else:
            self.description = description
        self.ledger.append({
            "amount": amount,
            "description": self.description
        })

    def withdraw(self, amount, description=None):
        if amount > self.total:
            return False
        else:
            self.total -= amount
            if description == None:
                self.description = ""
            else:
                self.description = description
            self.ledger.append({
                "amount": -amount,
                "description": self.description
            })
            return True

    def get_balance(self):
      return self.total

    def transfer(self, amount, another_category):
        if amount > self.total:
            return False
        else:
            self.total -= amount
            another_category += amount
            self.ledger.append({
                "amount": -amount,
                "description": f'Transfer to {another_category}'
            })
            another_category.append({
                "amount": amount,
                "description": f'Transfer from {self.name}'
            })
            return True
            
    def check_funds(self, amount):
        fund = 0
        n = len(self.ledger)
        for i in range(n):
            fund = fund + self.ledger[i]["amount"]
        if amount > fund:
            return False
        else:
          return True










# def create_spend_chart(categories):