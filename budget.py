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
      """
      Checks whether the withdrawal is possible,
      if withdraw is possible, it reduce total sum in a particular category
      adds description of the operation if there are some.
      If the total sum is less than required sum for withdrawal, returns False.
      """
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
      """
      Displays the total amount
      """
      return self.total

    def transfer(self, amount, another_category):
        """
        Checks whether the transfer is possible,
        if transfer is possible, it reduce total sum in a particular category
        and adds transfer to the category where transfer is aimed,
        adds description of the operation if there are some.
        If the total sum is less than required sum for transfer, returns False.
        """
        if self.check_funds(amount):
            self.total -= amount
            another_category.total += amount
            self.ledger.append({
                "amount": -amount,
                "description": f'Transfer to {another_category.name}'
            })
            another_category.ledger.append({
                "amount": amount,
                "description": f'Transfer from {self.name}'
            })
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        Checks whether the amount for transfer and withdraw are possible
        """
        fund = 0
        n = len(self.ledger)
        for i in range(n):
            fund = fund + self.ledger[i]["amount"]
        if amount > fund:
            return False
        else:
          return True

    def __str__(self):
        """
        Method creates a table of all operations in a particular category
        with the total amount
        """
        # Center category name 
        title = self.name.center(30, "*")
        count = 0
        lines = []
        # Get descriptions and amounts for each operation
        for amount in self.ledger:
            amount = self.ledger[count]["amount"]
            amount = format(amount, "2f")
            amount = (" " + amount)[:7].rjust(7)
            description = self.ledger[count]["description"]
            if len(description) > 23:
                description = description[:23]
            else:
                description = description.ljust(23)
            lines.append(description + amount)
            count += 1
        # Get the table of spending
        each_line_print = "\n".join(lines)
        # Get total amount
        total = format(self.total, ".2f")
        total = f"Total: {self.total}"
        # Display the whole expanses with total amount in a table
        display_budget = title + "\n" + each_line_print + "\n" + total
        return display_budget

def create_spend_chart(categories):
    # Variables
    chart_title = "Percentage spent by category"
    chart = ""
    categories = []
    withdraws = []
    withdraw_percentage = []
    vertical_categories = ""