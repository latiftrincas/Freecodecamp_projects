class Category:

    # when instatiate requries a name and creates a list that is a ledger
    def __init__(self, cat):
        self.category = cat
        self.ledger = list()

    # deposit method that takes an amount and descrpiton, stores this into the ledger as a dictionary
    # in the form {"amount": amount, "description": description}
    # description by defaut is empty string
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    # retrieves and returns the sum amount of the ledger
    def get_balance(self):
        total = 0
        for expense in self.ledger:
            total += expense['amount']
        return total

    # takes in an amount and compares to total balance of ledger
    # returns false if amount is higher than balance
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    # similiar to deposit but holds the amount as a negative number
    # amount must be <= to total balance in ledger
    # returns true of alse wether it is added to ledger
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    # method that withdraws from self and deposits to another class
    def transfer(self, amount, other_cat):
        if amount <= self.get_balance():
            self.withdraw(amount, f'Transfer to {other_cat.category}')
            other_cat.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    # output when a category is called
    # in the form
    # *************Food*************
    # initial deposit        1000.00
    # groceries               -10.15
    # restaurant and more foo -15.89
    # Transfer to Clothing    -50.00
    # Total: 923.96
    def __repr__(self):
        transactions = ''
        total = 0
        for expense in self.ledger:
            money = expense['amount']
            descr = expense['description']
            # format the descriptin to max 23 characters and width 23 with left align
            # format moneey to max 7 charachters and right align with 2 decimal places
            transactions += f'\n{descr[0:23]:<23}{money:>7.2f}'
            total += money
        display = f'{self.category:*^30}{transactions}\nTotal: {total}'
        return display

    def percent_spent(self):
        total_spent = 0
        total_amnt = 0
        # total sum of withdrawls
        for amnt in self.ledger:
            if amnt['amount'] < 0:
                total_spent -= amnt['amount']
            else:
                total_amnt += amnt['amount']
        percentage = (total_spent/total_amnt)*100
        percentage = round(percentage, -1)
        return percentage


def create_spend_chart(catergories):
    percent = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    # emtpy string that will store the bar chart
    table = ''
    # list to hold name of category
    cat_title = []
    for cat in catergories:
        cat_title.append(cat.category)
    # for each y-axis find if the percentage spent, by category,
    # is equal or less than y-axis data
    # if true place o
    for pcnt in percent:
        table += f'{pcnt:3}|'
        # for each category find the percentage spent
        for cat in catergories:
            percentage_cat = cat.percent_spent()
            if pcnt > percentage_cat:
                table += f'   '
            else:
                table += f' o '
        table += f' \n'
    # leaves 2 - after final o
    nbars = (len(catergories)*3)+1
    table += '    ' + nbars*'-'
    letters = '    '
    counter = 0
    # find max length word for counter index
    max_word = max(cat_title, key=len)

    # while the counter is less than the maximum length word
    # go through each cateregory name and retrieve the nth letter
    # repeat till max index acheived for max length word
    while counter < len(max_word):
        for cat in cat_title:
            if counter + 1 <= len(cat):
                letters += f' {cat[counter]} '
            else:
                letters += f'   '
        counter += 1
        letters += f'\n    '
    z = table
    chart = 'Percentage spent by category\n' + table + '\n' + letters
    return chart
