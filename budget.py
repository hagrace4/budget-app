class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False
        
    def __str__(self):
        string = self.name.center(30,"*") + "\n"
        for item in self.ledger:
            displayAmount = str("%.2f"%item["amount"])[0:7].rjust(7)
            displayDescription = item["description"][0:23].ljust(23)
            string += displayDescription + displayAmount + "\n"
        string += "Total: " + str(self.get_balance())
        return string


# Takes list of categories as an argument and return a string that is a bar chart
def create_spend_chart(categories):
  chart ="Percentage spent by category\n"
  dict = {}
  sum = 0
  for category in categories:
    spent = 0
    for item in category.ledger:
      if item["amount"] < 0:
        spent += item["amount"]
    dict[category.name] = spent
    sum += spent
  percentages = []
  for value in dict.values():
    value /= sum
    value = int(value * 10) * 10
    percentages.append(value)
  print(percentages)
  n = len(categories)
  for x in range(10, -1, -1):
    chart += (str(x*10) + "| ").rjust(5) 
    for value in percentages:
      if value >= (x*10):
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"
  bar = ""
  for b in range(n*3+1):
    bar += "-"
  chart += bar.rjust(n*3+5) + "\n"
  longest = 0
  for category in categories:
    if len(category.name) > longest:
      longest = len(category.name)
  for letter in range(longest):
    chart+= "     "
    for category in categories:
      if letter < len(category.name):
        chart += category.name[letter] + "  "
      else:
        chart += "   "
    if letter < longest-1:
      chart += "\n" 
  return chart