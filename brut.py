from subprocess import call
from os import name as osname
from datetime import datetime

def parse_markdown(line):
    return line

def save(line, file_name):
    with open(str(file_name) + ".md", "a") as file:
        file.write(line + "\n")
    current_timestamp = datetime.timestamp(datetime.now())
    with open("zed" + str(file_name) + ".ser", "a") as service_file:
        service_file.write(str(str(current_timestamp) + "\n"))
    return


def save_no_parse(line):
    pass


def quit(line):
    yes = ["quit()", "let me out of here", "....."]
    if line in yes:
        return True
    return False

def clear_screen():
    _ = call("cls" if osname == "nt" else "clear")
    return
    
    
# MAIN
clear_screen()
file_name = datetime.timestamp(datetime.now())

while True:
    line = input("    ")
    print("\n\n")
    if quit(line):
        break
    parsed_line = parse_markdown(line)
    save(parsed_line, file_name)
print("bye")

