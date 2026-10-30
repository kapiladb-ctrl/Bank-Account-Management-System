# ==========================================
# 1. බැංකු ගිණුම සඳහා OOP සැලසුම (Class) නිර්මාණය
# ==========================================
class BankAccount:
    
    # ගිණුම් හිමියාගේ නම ඇතුළත් කර Object එකක් සෑදීමේ මූලික ශ්‍රිතය (Constructor)
    def __init__(self, owner_name):
        self.owner = owner_name                     # ගිණුම් හිමියාගේ නම 'owner' පෙට්ටියට දැමීම
        self.balance = self.load_balance()          # ගොනුවෙන් පැරණි සල්ලි ගණන කියවා 'balance' පෙට්ටියට දැමීම

    # Hard Drive එකේ ඇති 'balance.txt' ගොනුවෙන් පැරණි ශේෂය කියවන ශ්‍රිතය (Read File)
    def load_balance(self):
        try:
            file = open("balance.txt", "r")         # කියවීම සඳහා 'balance.txt' විවෘත කිරීම
            bal = float(file.read())                # ගොනුවේ ඇති අගය කියවා දශම සංඛ්‍යාවක් බවට හැරවීම
            file.close()                            # වැඩේ නිම වූ පසු ගොනුව වසා දැමීම
            return bal                              # කියවා ගත් ශේෂය පිටතට ලබා දීම
        except (FileNotFoundError, ValueError):
            return 0.0                              # තවමත් ගොනුවක් සාදා නැත්නම් හෝ වැරදි අගයක් තිබේ නම් සල්ලි 0.0 ලෙස ගැනීම

    # නවතම ශේෂය (Balance) Hard Drive එක තුළ ස්ථිරවම සුරකින ශ්‍රිතය (Write File)
    def save_balance(self):
        file = open("balance.txt", "w")             # ලිවීම සඳහා 'balance.txt' විවෘත කිරීම (පැරණි දේ මැකී අලුත් දේ ලියවේ)
        file.write(str(self.balance))               # වත්මන් ශේෂය string එකක් බවට හරවා ගොනුව තුළ ලිවීම
        file.close()                            # වැඩේ නිම වූ පසු ගොනුව වසා දැමීම

    # මුදල් තැන්පත් කිරීම (Deposit)
    def deposit(self, amount):
        if amount > 0:                              # ඇතුළත් කළ මුදල බිංදුවට වඩා වැඩි දැයි බැලීම
            self.balance += amount                  # වත්මන් ශේෂයට එම මුදල එකතු කිරීම (self.balance = self.balance + amount)
            self.save_balance()                     # අලුත් වූ ශේෂය Hard Drive එකෙහි සුරැකීම
            print(f"🎯 රු. {amount} සාර්ථකව තැන්පත් කරන ලදී.")
        else:
            print("❌ වලංගු මුදලක් ඇතුළත් කරන්න.")

    # මුදල් ලබාගැනීම (Withdraw)
    def withdraw(self, amount):
        if amount > self.balance:                   # ලබාගැනීමට ඉල්ලන මුදල ගිණුමේ ඇති මුදලට වඩා වැඩි දැයි බැලීම
            print("❌ ගිණුමේ ප්‍රමාණවත් මුදලක් නොමැත!")
        elif amount <= 0:                           # ඇතුළත් කළ මුදල බිංදුවට වඩා අඩු හෝ සමාන දැයි බැලීම
            print("❌ වලංගු මුදලක් ඇතුළත් කරන්න.")
        else:
            self.balance -= amount                  # వත්මන් ශේෂයෙන් එම මුදල අඩු කිරීම (self.balance = self.balance - amount)
            self.save_balance()                     # අලුත් වූ ශේෂය Hard Drive එකෙහි සුරැකීම
            print(f"🎯 රු. {amount} ගිණුමෙන් ලබාගන්නා ලදී.")

    # ගිණුමේ වත්මන් ශේෂය පෙන්වීම (Check Balance)
    def check_balance(self):
        print(f"👤 ගිණුම් හිමියා: {self.owner} | 💰 වත්මන් ශේෂය: රු. {self.balance}")


# ==========================================
# 2. ප්‍රධාන මෘදුකාංග පද්ධතිය ක්‍රියාත්මක වන කොටස (Main Program)
# ==========================================
print("=== අපේ ප්‍රථම Capstone බැංකු පද්ධතිය ===")
name = input("කරුණාකර ඔබේ නම ඇතුළත් කරන්න: ")      # පරිශීලකයාගෙන් නම ලබා ගැනීම

# පරිශීලකයාගේ නමට අදාළව බැංකු ගිණුම් වස්තුව (Object) නිර්මාණය කිරීම
user_account = BankAccount(name)

# මෘදුකාංගය නොනවත්වා ධාවනය කිරීමට while Loop එකක් භාවිතා කිරීම
while True:
    print("\n--- මෙනුව ---")
    print("1. ගිණුම් ශේෂය පරීක්ෂා කිරීම (Check Balance)")
    print("2. මුදල් තැන්පත් කිරීම (Deposit)")
    print("3. මුදල් ලබාගැනීම (Withdraw)")
    print("4. පද්ධතියෙන් ඉවත් වීම (Exit)")
    
    # පරිශීලකයාට අවශ්‍ය සේවාවේ අංකය ලබා ගැනීම
    choice = input("ඔබට අවශ්‍ය සේවාවේ අංකය ඇතුළත් කරන්න (1-4): ")
    
    # 1 එබුවහොත්: ශේෂය පරීක්ෂා කිරීමේ ශ්‍රිතය කැඳවීම
    if choice == "1":
        user_account.check_balance()
        
    # 2 එබුවහොත්: මුදල් තැන්පත් කිරීම
    elif choice == "2":
        try:
            amt = float(input("තැන්පත් කරන මුදල: ")) # මුදල ලබා ගැනීම (අකුරු දැමුවහොත් try-except මඟින් බේරාගනී)
            user_account.deposit(amt)                 # තැන්පත් කිරීමේ ශ්‍රිතය කැඳවීම
        except ValueError:
            print("❌ වැරදි ආදානයක්! ඉලක්කම් පමණක් ඇතුළත් කරන්න.")
            
    # 3 එබුවහොත්: මුදල් ලබාගැනීම
    elif choice == "3": 
        try:
            amt = float(input("ලබාගන්නා මුදල: "))     # මුදල ලබා ගැනීම
            user_account.withdraw(amt)                # මුදල් ලබාගැනීමේ ශ්‍රිතය කැඳවීම
        except ValueError:
            print("❌ වැරදි ආදානයක්! ඉලක්කම් පමණක් ඇතුළත් කරන්න.")
            
    # 4 එබුවහොත්: මෘදුකාංගයෙන් ඉවත් වීම
    elif choice == "4":
        print(f"ස්තූතියි {name} මහත්මයා! සුභ දවසක්!")
        break                                         # break මඟින් while loop එක නතර කර මෘදුකාංගය වසා දමයි
        
    # වෙනත් ඕනෑම වැරදි අංකයක් හෝ අකුරක් ඇතුළත් කළහොත්:
    else:
        print("❌ වැරදි අංකයක්! කරුණාකර 1 සිට 4 දක්වා අංකයක් තෝරන්න.")
