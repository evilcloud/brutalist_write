from subprocess import call
from os import name as osname
from datetime import datetime

def save(line, file_name):
    with open(str(file_name) + ".md", "a") as file:
        file.write(line + "<br/>")
    current_timestamp = datetime.timestamp(datetime.now())
    with open("zed" + str(file_name) + ".ser", "a") as service_file:
        service_file.write(str(str(current_timestamp) + "<br/>"))
    return

def help_screen():
    print("""
          
          BRUTALIST HELP MENU
          
          quit() or .....
          help() or ?????
          
          no SAVE necessary, as
          the texts saves line-by-line""")
    return

def menu(line):
    quit_command = ["quit()", "....."]
    help_command = ["help()", "?????"]
    if line in quit_command:
        return True
    elif line in help_command:
        print(help_screen())
        return False
    return False

def clear_screen():
    _ = call("cls" if osname == "nt" else "clear")
    return
    
    
# MAIN
clear_screen()
file_name = datetime.timestamp(datetime.now())
save("", file_name)

while True:
    line = input("    ")
    print("\n\n")
    save(line, file_name)
    if menu(line):
        break
print("bye")

