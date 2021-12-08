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

    









# def create_spend_chart(categories):