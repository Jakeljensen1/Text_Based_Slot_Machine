import random

MAX_LINES = 3 #All caps, because this is a constant value
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2,
  "K": 4,
  "Q": 6,
  "J": 10,
}

symbol_values = {
  "A": 8,
  "K": 6,
  "Q": 4,
  "J": 2,
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)
 
  return winnings, winning_lines

def get_slot_machine_spin (rows, cols, symbols):
  all_symbols = []

  for symbol, symbol_count in symbols.items(): # loops through dictionary
    for  _ in range(symbol_count): # loops through symbol_counts within the dictionary, using '_' as anonymous variable
      all_symbols.append(symbol)

  columns = [] #Storing columns not rows
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:] # Colon is for copying a list, refered to as the slice operator. If we don't add this 'current_symbols' and 'all_symbols' just refer to the same list
    for _ in range(rows):
      value = random.choice(current_symbols) # can use this on list, not dictionary, because they don't support indexing
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)

  return columns

def print_slot_machine (columns): # transposing
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")

    print()

def deposit():
  while True:
    amount = input("What would you like to deposit? $ ")

    if amount.isdigit(): #Valid whole num on strings
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0")
    else:
      print("Please enter a valid deposit number")

  return amount

def get_num_of_lines():
  while True:
    lines = input("How many lines would you like to play (1-" + str(MAX_LINES) + ")? ")

    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Please enter valid betting lines")
    else: print("Please enter valid line number")

  return lines

def get_bet():
  while True: 
    bet = input("How much would you like to bet per line (" + str(MIN_BET) + "-" + str(MAX_BET) + ")? ")

    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else:
        print (f"Please enter a valid bet amount between ${MIN_BET} and ${MAX_BET}")
    else:
      print("Please enter a valid bet number")

  return bet

def spin(balance):
  lines = get_num_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"You do not have enough balance to place this bet. Current balance: {balance}")
      
    else:
      break     
  print(f"You are betting ${bet} on {lines} lines, for a total bet of ${total_bet}")

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)

  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

  print(f"You won ${winnings} at line(s):")
  print(f"You won on lines:",  *winning_lines)

  return winnings - total_bet

def main():
  balance = deposit()
  while True:
    print(f"Current balance is: ${balance}")
    spin_input = input("press any button to spin (or q to quit).")
    if spin_input == "q":
      break
    balance += spin(balance)

  print(f"You left with ${balance}") 

main()