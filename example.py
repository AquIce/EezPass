from eezpass import *

os.system('cls')

myPass = EezPass('admin')

myPass.enable_logs(True)
myPass.set_charsets('amns')
myPass.set_length(16)
myPass.enable_password_logs(True)
myPass.include_string(True)
myPass.set_include_string_position(0)

myPass.print_password()