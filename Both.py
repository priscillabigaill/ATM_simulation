from Account import Account
from Customer import Customer
from Bank import Bank
from CustATM import CustATM
from Admin import Admin

class Both:

    def __init__(self):

        self.data = [
            {
                'fname': 'First1',
                'lname': 'Last1',
                'balance': 100000
            },
            {
                'fname': 'First2',
                'lname': 'Last2',
                'balance': 200000
            },
            {
                'fname': 'First3',
                'lname': 'Last3',
                'balance': 300000
            }
        ]

        is_not_exit = True
        while(is_not_exit):
            is_not_exit = self.main_menu()

    def main_menu(self):

        main_menu_str = f"""
        Who are you? (input number)
        > (1) Customer
        > (2) Admin
        > (3) Exit
        """

        opt_number = input(main_menu_str)

        while opt_number not in ["1","2","3"]: 
            print("""
            Please try again.
            """)

            opt_number = input(main_menu_str)

        if opt_number == '1': 
            ATM = CustATM(self.data)
            return True

        if opt_number == '2':       
            admin = Admin(self.data)
            self.data = admin.data
            return True

        if opt_number == "3":
            print("Goodbye! :)")
            return False
    


