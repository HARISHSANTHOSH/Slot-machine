import random
max_Lines=3
max_bet=100
min_bet=1
ROWS=3
COLS=3
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8



}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2



}
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings+=values[symbol] * bet
                winning_lines.append(line+1)
    return winnings,winning_lines




def get_slot_machie_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        curremt_symbols=all_symbols
        for _ in range(rows):
            value=random.choice(curremt_symbols)
            curremt_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:

                print(column[row],end="")
        print()



def deposit():
    while True:
        amount=input('enter the amount')
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number")
    return amount





def get_no_lines():
    while True:
        lines = input("enter the number of lines on (1-" +  str(max_Lines) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=max_Lines:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("please enter a number")
    return lines

def get_bet():
    while True:
        amount = input('What would like you bet on each line ?')
        if amount.isdigit():
            amount = int(amount)
            if min_bet<=amount<=max_bet:
                break
            else:
                print(f"Amount must be between ${min_bet}-${max_bet}")
        else:
            print("please enter a number")
    return amount


def spin(balance):
    lines = get_no_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"your do not have enough to bet that amount your current balance is ${balance}")
        else:
            break
    print(f"your are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}")
    print(balance, lines)
    slots = get_slot_machie_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on :",*winning_lines)

    return winnings - total_bet



def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        answ=input("Press enter to spin (q to quit).")
        if answ=='q':
            break
        balance +=spin(balance)

    print("you left with $(balance)")
main()
