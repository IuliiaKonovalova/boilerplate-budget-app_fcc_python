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
      if self.check_funds(amount):
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
      else:
          return False

    def get_balance(self):
      return self.total

    def transfer(self, amount, another_category):
        if self.check_funds(amount):
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
        else:
            return False

    def check_funds(self, amount):
        fund = 0
        n = len(self.ledger)
        for i in range(n):
            fund = fund + self.ledger[i]["amount"]
        if amount > fund:
            return False
        else:
          return True

    def __str__(self):
        title = self.name.center(30, "*")
        count = 0
        lines = []
        for amount in self.ledger:
            amount = self.ledger[count]["amount"]
            amount = format(amount, "2f").rjust(7)
            description = self.ledger[count]["description"]
            if len(description) > 23:
                description = description[23:]
            else:
                description = description.ljust(23)
            lines.append(description + amount)
            count += 1
        each_line_print = "\n".join(lines)
        total = format(self.total, "2f")
        total_line = f'Total: {total}'
        display_budget = title + "\n" + each_line_print + "\n" + total_line
        return display_budget









# def create_spend_chart(categories):