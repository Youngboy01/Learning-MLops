class chattingFunctionality:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input(
            """Welcome to Chat Application , How would you like to proceed?
            1. Signup
            2. Login
            3. Write a message to friend
            4. write a post
            5. exit
            """
        )
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Exiting the application. Goodbye!")
            exit()

    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print("Login successful!")
        self.menu()

    def login(self):
        if self.username == "" or self.password == "":
            print("Username and password cannot be empty.\n Please press 1 to signup")
        else:
            email = input("Enter your email/username here: ")
            password = input("Enter your password here: ")
            if email == self.username and password == self.password:
                print("Login successful!")
                self.logged_in = True
            else:
                print("Invalid credentials. Please try again.")
        print("\n")
        self.menu()


c = chattingFunctionality()
