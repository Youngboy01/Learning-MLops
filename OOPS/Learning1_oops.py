class chattingFunctionality:
    __user_id = 0  # static variable
    def __init__(self):
        self.__name = "Default user"
        # self.user_id=0
        # self.user_id+=1
        self.id = chattingFunctionality.__user_id
        chattingFunctionality.__user_id += 1
        self.username = ""
        self.password = ""
        self.logged_in = False
        #self.menu()
    @staticmethod
    def get_id():
        return chattingFunctionality.__user_id
    @staticmethod
    def set_id(id):
        chattingFunctionality.__user_id = id
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

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
            self.writeMessage()
        elif user_input == "4":
            self.writePost()
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

    def writeMessage(self):
        if not self.logged_in:
            print("you need to login first")
        else:
            friend = input("Enter your friend's name: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend}: {message}")
        print("\n")
        self.menu()

    def writePost(self):
        if not self.logged_in:
            print("you need to login first")
        else:
            post = input("Write your post here: ")
            print("Post published:", post)
        print("\n")
        self.menu()


c = chattingFunctionality()
