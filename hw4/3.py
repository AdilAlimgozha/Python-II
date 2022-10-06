class Password_manager:
    def __init__(self, last_passwords, current_password):
        self.last_passwords = last_passwords
        self.current_password = current_password
    
    def get_password(self):
        return self.current_password

    def set_password(self):
        print('current password:', self.get_password())
        while True:
            new_password = input('new password: ')
            if new_password == self.get_password():
                print('password is the same as current')
            elif new_password in self.last_passwords:
                print('password is the same as all your last')
            else:  
                break
        self.current_password = new_password
        
    def is_correct(self):
        check = input('repeat password: ')
        if check == self.current_password:
            print(True)
            print('current password:', self.get_password())
        else:
            print(False)
            
a = ['12345', 'qwerty', '54321']
current = '2003'
password_manager = Password_manager(a, current)
password_manager.set_password()
password_manager.is_correct()