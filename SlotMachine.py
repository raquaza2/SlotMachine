import random
def spin_row():
    symbols = ['🍎','🍊','🍋','🍒','🍉']
    
    
    return [random.choice(symbols)for _ in range(3)]
     
def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")
   

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if  row[0] == '🍎':
            return bet * 3
        elif row[0] == '🍊':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🍒':
            return bet * 6
    return 0
            

def main():
    balance = 100
    
    print("********************")
    print("Python Slot")
    print("Symbols:🍎🍊🍋🍒🍉")
    print("********************")
    
    while balance > 0:
        print(f"Current balance: RM{balance}")
        
        bet = input("Place your bet amount:RM")
        
        if not bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient balance. Please place a bet within your balance.")
            continue
        
        if bet <= 0:
            print("Invalid bet amount. Please enter a positive number.")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won RM{payout}!")
        else:
            print("You lost this round.")

        balance += payout
        
        play_again = input("Do you want to continue (y/n)?:")
        
        if play_again.lower() != 'y':
            break
        

if __name__ =='__main__':
    main()