from subprocess import call
from os import name as osname
from datetime import date, datetime


def save(line):
    file_name = "dbrut" + str(date.today())
    with open(file_name + ".md", "a") as file:
        file.write(line + "\n")
    current_timestamp = datetime.timestamp(datetime.now())
    with open("zed" + file_name + ".ser", "a") as service_file:
        service_file.write(str(str(current_timestamp) + "\n"))
    return


def help_screen():
    print(
        """
          
          BRUTALIST HELP MENU
          
          quit() or .....
          help() or ?????
          
          no SAVE necessary, as
          the texts saves line-by-line
          
          """,
          session_duration()
    )
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


def session_duration():
    """Returns [str] "session duration: XX:XX:XX:XXXXXX"""
    sess_dur = datetime.now() - start_time
    return "session duration: " + str(sess_dur)


def clear_screen():
    _ = call("cls" if osname == "nt" else "clear")
    return


# MAIN
global start_time
start_time = datetime.now()
clear_screen()
save("***")
save("[" + str(datetime.now()) + "]")
save("")
while True:
    line = input("    ")
    print("\n\n")
    if menu(line):
        break
    else:
        print("\n")
    save(line)

save(session_duration())
print("   " + session_duration())
print("\nbye")

