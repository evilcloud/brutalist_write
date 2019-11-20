from subprocess import call
from os import name as osname
from os import path as ospath
import os.path
from datetime import date, datetime
import csv

# CONFIG
global session_start_time
global session_date
session_start_time = datetime.now()
session_date = str(session_start_time.date())

# FILE FUNCTIONS
def save_txt(line):
    file_name = "bas" + session_date + ".txt"
    saving_process(line + "\n", file_name)
    return


# ANOTHER FILESYSTEM
# THE FILES, AS BEFORE, WOULD BE ISSUED DAILY, BECAUSE WRITING IS TO BE SPLIT INTO GEOTEMPORAL REALITY
# THIS MEANS THAT ANY WRITING COMMITED AT AND AFTER 00:00 OF THE NEXT DAY, EVEN IF SESSION STARTED THE DAY BEFORE,
# WILL CREATE AND SAVE INTO THE NEW-DAY'S FILE. THIS IS A CONTIOUS DESIGN DECISION, BASED ON THE PHILOSOPHY
# OF THE PROJECT

# FILE FORMAT: CSV, TWO COLLUMNS, COMMA SEPARATED
# FIRST VALUE: TIMESTAMP. SECOND VALUE: STRING.
# SESSION START WILL HAVE SPECIAL SESSION START CHAR IN THE TIMESTAMP FIELD AND TIMESTAMP IN STRING
def save_line(line):
    file_name = str(session_date) + ".bru"
    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerow(line)
    return


#####################################
# ALL OF THIS IS ABOUT TO GET DELETED
# AS WE ARE MOVING TO CSV FROM 4F
#  ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

# WORKING ON THIS RIGHT NOW
def temporary_function():
    file_line_assets = {
        "git_md": ["gmd", ".md", "<br/>"],
        "vanila_md": ["vmd", ".md", "<br/>"],
        "timedata": ["tds", ".ser", str(datetime.timestamp(datetime.now())) + "\n"],
        "overshare": [
            "ooo",
            ".md",
            line
            + f"<br/>    {(humanise_timedelta(datetime.now() - session_start_time))}<br/><br/>",
        ],
    }


def save_git_md(line):
    file_name = "gmd" + session_date + ".md"
    saving_process(line + "<br/>", file_name)
    return


def save_vanila_md(line):
    file_name = "vmd" + session_date + ".md"
    final_line = line + "\n"
    saving_process(final_line, file_name)
    return


def register_timedata():
    file_name = "tds" + session_date + ".ser"
    final_line = str(datetime.timestamp(datetime.now())) + "\n"
    saving_process(final_line, file_name)
    return


def save_oversharing(line):
    file_name = "ooo" + session_date + ".md"
    final_line = (
        line
        + "<br>    "
        + (humanise_timedelta(datetime.now() - session_start_time) + "<br/><br/>")
    )
    saving_process(final_line, file_name)
    return


def saving_process(final_line, file_name):
    with open(file_name, "a") as target_file:
        target_file.write(final_line)
    return


def save_to_all_files(line):
    save_txt(line)
    save_git_md(line)
    save_vanila_md(line)
    save_oversharing(line)
    register_timedata()
    return


def save_except_txt(line):
    save_txt("")
    save_git_md(line)
    save_vanila_md(line)
    save_oversharing(line)
    register_timedata()
    return

# THE END OF THE ABOUT-TO-BE-DELETED SECION
###################################


# SYSTEM
def quit_app():
    save_except_txt("⌹")
    print("   " + session_duration())
    print("\nbye")
    quit()


def clear_screen():
    _ = call("cls" if osname == "nt" else "clear")
    return


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


def first_line(check_file):
    if os.path.exists(check_file):
        opening_line = (
            "⌸" + " " * 15 + str(session_start_time.time().replace(microsecond=0))
        )
    else:
        opening_line = "⌷   " + str(session_start_time.replace(microsecond=0))
    return opening_line


# MAIN
# INITIALIZE
clear_screen()

############################ ABOUT TO BE GONE
save_except_txt(first_line("tds" + session_date + ".ser"))
save_to_all_files("")
##############################

# NEW FILE FORMAT PROC - ABOUT TO BE SET AS DEFAULT
save_line(["⌸", str(datetime.timestamp(datetime.now()))])

# TEXT ENTRY
while True:
    line = input("    ")
    print("\n\n")
    if menu(line):
        ############### BE GONE
        save_to_all_files(line)
        
        # NEW FILE FORMAT -- TO BE SET AS DEFAULT
        csv_line = [str(datetime.timestamp(datetime.now())), line]
        save_line(csv_line)
