from eezpass import * # Import the eezpass module

os.system('cls') # Clear the console

myPass = EezPass('admin') # Create a new instance of EezPass

myPass.enable_logs(True) # Enable general logs
myPass.enable_password_logs(True) # Enable password logs
myPass.set_charsets('amns') # Select all charsets
myPass.set_length(16) # Set the password length to 16 characters

myPass.include_string(True) # Enable string including
myPass.set_include_string_position('*') # Set it to a random position

myPass.print_properties() # Print properties
myPass.print_password() # Print the final password
myPass.print_passlogs('*') # Print all generated passwords

end() # End the program
