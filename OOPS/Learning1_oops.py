class chattingFunctionality:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.menu()
        
    def menu(self):
        user_input = input(
            """Welcome to Chat Application , How would you like to proceed?
            1. Login
            2. Signup
            3. Write a message to friend
            4. write a post
            5. exit
            """
        )
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Exiting the application. Goodbye!")
            exit()
c = chattingFunctionality()