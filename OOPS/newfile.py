from Learning1_oops import chattingFunctionality
user1 = chattingFunctionality()

# #function
# a1 = [1,23,4]
# print(len(a1))
# #method
# user1.writeMessage()
#encapsulation
#print(user1.__name)
#cheating encapsulation
print(user1._chattingFunctionality__name)
#getter setter
print(user1.get_name())
user1.set_name("YoungBoy")
print(user1.get_name())
#static method
# print(user1.user_id)
# user2=chattingFunctionality()
# print(user2.user_id)
# user3=chattingFunctionality()
# print(user3.user_id)
#we get one in every case because its not static variable
#static variable
print(user1.id)
user2=chattingFunctionality()
print(user2.id)
user3=chattingFunctionality()
print(user3.id)
chattingFunctionality.set_id(10)
print(chattingFunctionality.get_id())