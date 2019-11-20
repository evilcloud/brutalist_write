from subprocess import call
from os import name as osname
from datetime import date, datetime
import csv

# CONFIG
global session_start_time
global session_date
session_start_time = datetime.now()
session_date = str(session_start_time.date())

# FILE FUNCTIONS
def save_line(line):
    file_name = str(session_date) + ".bru"
    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerow(line)
    return


# SYSTEM
def clear_screen():
    _ = call("cls" if osname == "nt" else "clear")
    return


def quit_app():
    save_line(["⌹", str(datetime.timestamp(datetime.now()))])
    print("   " + session_duration())
    print("\nbye")
    quit()


# DOESN'T WORK FOR SOME REASON
# def timestamp_line():
#     timestamped_line = str(datetime.timestamp(datetime.now()))
#     return timestamped_line


# MENU
def help_screen():
    print(
        "\x1b[1;33;40m"
        + """
          
          BRUTALIST HELP MENU
          
          quit() or .....
          help() or ?????
          
          no SAVE necessary, as
          the texts saves line-by-line
          
          """,
        "\x1b[0;30;43m",
        session_duration(),
        "\x1b[0m \n\n",
    )
    return


def stat_screen():
    session_duration()
    return


def menu(line):
    commands = {
        ".....": "quit_app()",
        "?????": "help_screen()",
        "/////": "stat_screen()",
    }
    if line in commands:
        eval(commands[line])
    else:
        return True
    return False


# DATAPROC
def humanise_timedelta(td):
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    plural = lambda x: "s" if x > 1 else ""
    show_noshow = lambda n, time_unit: (str(n) + time_unit + plural(n)) if n > 0 else ""
    time_string = (
        show_noshow(hours, " hour")
        + " "
        + show_noshow(minutes, " minute")
        + " "
        + show_noshow(seconds, " second")
    )
    return time_string


def session_duration():
    """Returns [str] "session duration: [huminized time]
    gets data from [huminise_timedelta]"""
    sess_dur = datetime.now() - session_start_time
    return "session duration: " + humanise_timedelta(sess_dur)


# MAIN
clear_screen()
save_line(["⌸", str(datetime.timestamp(datetime.now()))])

# TEXT ENTRY
while True:
    line = input("    ")
    print("\n\n")
    if menu(line):
        csv_line = [str(datetime.timestamp(datetime.now())), line]
        save_line(csv_line)
