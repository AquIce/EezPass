import os
import random
import datetime


class EezPass:
    '''
    EezPass class provides a simple passwords administration interfaces
    '''

    def __init__(self, password):
        self.admin_password = password
        self.length = 8
        self.charsets = 'amn'
        self.passwordLogsEnabled = False
        self.logsEnabled = False
        self.includeString = False
        self.pos = 0
        self.passwordLogs = 'passwords'
        self.logs = 'default'
        self.password = ['a'] * self.length
        self.logged = False
        self.logFiles = 'default.log'

        self.ALPHA = 'abcdefghijklmnopqrstuvwxyz'
        self.MAJ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.NUM = '0123456789'
        self.SPECIAL = ',.-;:_^![]{}+"*ç%&/()=?'

        self.ERRORS = ('SYSTEM.GENERAL.FAILURE', '! ERROR !\n<invalid_index> in pos (value passed with \'set_include_string_position\' or the input of \'include_string\')', '! ERROR !\n<invalid_admin_password>', '! ERROR !\n<invalid_charsets>')

    def set_length(self, min_length):
        if self.logged:
            self.length = min_length
        else:
            p = input('What is the password ? ')
            if p == self.admin_password:
                self.logged = True
            if self.logged:
                self.length = min_length
                with open(self.logFiles, 'a') as file:
                    file.write('Logged as ADMIN\n')
            else:
                with open(self.logFiles, 'a') as file:
                    file.write('Logging as ADMIN failed with password \'' + p + '\'\n')
                self.ERROR(2)
        self.password = ['a'] * self.length

    def set_charsets(self, charsets):
        if self.logged:
            self.charsets = charsets
        else:
            p = input('What is the password ? ')
            if p == self.admin_password:
                self.logged = True
            if self.logged:
                if len(charsets.replace('a', '').replace('m', '').replace('n', '').replace('s', '')) != 0:
                    self.ERROR(3)
                else:
                    self.charsets = charsets
                    with open(self.logFiles, 'a') as file:
                        file.write('Logged as ADMIN\n')
            else:
                with open(self.logFiles, 'a') as file:
                    file.write('Logging as ADMIN failed with password \'' + p + '\'\n')
                self.ERROR(2)

    def get_properties(self):
        properties = (self.length, self.charsets)
        return properties

    def print_properties(self):
        properties = self.get_properties()
        print('Password length : ', properties[0])
        prop = []
        for i in properties[1]:
            if i == 'a':
                prop.append('Lower letters')
            elif i == 'm':
                prop.append('Upper letters')
            elif i == 'n':
                prop.append('Numbers')
            else:
                prop.append('Special characters')

        props = ', '.join(prop).capitalize()

        print('Enabled charsets : ', props)
        with open(self.logFiles, 'a') as file:
            file.write('Properties printed\n')

    def generate_password(self):
        string = ''
        if 'a' in self.charsets:
            string += self.ALPHA
        if 'm' in self.charsets:
            string += self.MAJ
        if 'n' in self.charsets:
            string += self.NUM
        if 's' in self.charsets:
            string += self.SPECIAL

        for i in range(self.length):
            self.password[i] = string[random.randint(0, len(string) - 1)]

        if self.includeString:
            for i in range(self.pos, self.pos + len(self.stringToInclude)):
                self.password[i] = self.stringToInclude[i - self.pos]

        if self.passwordLogsEnabled:
            if not os.path.exists(self.passwordLogs + '.log'):
                with open(self.passwordLogs + '.log', 'a') as file:
                    file.write('')

            with open(self.passwordLogs + '.log', 'a') as file:
                for i in self.password:
                    file.write(i)
                file.write('\n')
        
        with open(self.logFiles, 'a') as file:
            file.write('Password generated : \''+ ''.join(self.password) + '\'\n')

    def print_password(self):
        self.generate_password()
        for i in self.password:
            print(i, end='')
        print('\n')
        with open(self.logFiles, 'a') as file:
            file.write('Password printed\n')
            file.write('Success [] (Programm exited successfully)\n')

    def enable_password_logs(self, trueOrFalse):
        self.passwordLogsEnabled = trueOrFalse
        with open(self.logFiles, 'a') as file:
            file.write('Password logs enabled set to ' + str(self.passwordLogsEnabled) + '\n')

    def include_string(self, trueOrFalse):
        if trueOrFalse:
            self.includeString = True
            self.stringToInclude = input('Which string do you want to include ? ')
            if len(self.password) - len(self.stringToInclude) >= 0 :
                self.pos = random.randint(0, len(self.password) - len(self.stringToInclude))
                with open(self.logFiles, 'a') as file:
                    file.write('Include string turned to True with the string \'' + self.stringToInclude + '\'\n')
            else:
                self.ERROR(1)
                
        else:
            self.includeString = False
            with open(self.logFiles, 'a') as file:
                file.write('Include string turned to False\n')

    def set_include_string_position(self, position):
        if position == '*':
            self.pos = random.randint(0, len(self.password)- len(self.stringToInclude))
        elif position <= len(self.password):
            self.pos = position
            with open(self.logFiles, 'a') as file:
                file.write('String include position set to ' + str(self.pos) + '\n')
        else:
            self.ERROR(1)

    def enable_logs(self, trueOrFalse):
        if trueOrFalse:
            self.enableLogs = True
            self.logFiles = self.logs + '.log'
            if not os.path.exists(self.logFiles):
                with open(self.logFiles, 'x') as file:
                    file.write('')
            with open(self.logFiles, 'a') as file:
                time = datetime.datetime.now()
                file.write('LOGS ENABLED at [' + str(time) + ']\n')
        
        else:
            self.enableLogs = False
            with open(self.logFiles, 'a') as file:
                time = datetime.datetime.now()
                file.write('LOGS DISABLED at [' + str(time) + ']\n')


    def print_passlogs(self, index):
        with open(self.passwordLogs + '.log', 'r') as file:
            passwords = file.readlines()
        if index == '*':
            for i in passwords:
                print(i, end='')
        else:
            print(passwords[index])

    def ERROR(self, code):
        with open(self.logFiles, 'a') as file:
            file.write('Error [' + str(code) + '] (' + self.ERRORS[code].replace('\n', ' ') + ') raised\n\n')
        print(self.ERRORS[code])
        quit()

def end():
    input('Press enter to continue...')
