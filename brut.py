from subprocess import call
from os import name as osname
from datetime import date, datetime

# CONFIG
global start_time
global file_name_component
start_time = datetime.now()
file_name_component = str(start_time)
file_name_component = file_name_component[:10]

# FILE FUNCTIONS
def save_txt(line):
    file_name = "bas" + file_name_component + ".txt"
    with open(file_name, "a") as text_file:
        text_file.write(line)
    return

def save_git_md(line):
    file_name = "gmd" + file_name_component + ".md"
    with open(file_name, "a") as gitmd_file:
        gitmd_file.write(line + "<br/>")
    return

def save_vanila_md(line):
    file_name = "vmd" + file_name_component + ".md"
    with open(file_name, "a") as vanmd_file:
        vanmd_file.write(line)
    return

def register_timedata():
    file_name = "tds" + file_name_component + ".ser"
    with open(file_name, "a") as time_file:
        time_file.write(datetime.timestamp(datetime.now()))
    return

def oversharing_gmd(line):
    file_name = "ooo" + file_name_component + ".md"
    with open(file_name, "a") as overshare:
        overshare.write("    " + line + "<br/>")
        overshare.write(humanise_timedelta(datetime.now()-start_time))
    return
    

def save(line):
    file_name = "dbrut" + str(date.today())
    with open(file_name + ".md", "a") as file:
        file.write(line + "\n")
    current_timestamp = datetime.timestamp(datetime.now())
    with open("zed" + file_name + ".ser", "a") as service_file:
        service_file.write(str(str(current_timestamp) + "\n"))
    return


def quit_app():
    save("---")
    print("   " + session_duration())
    print("\nbye")
    quit()


def help_screen():
    print(
        """
          
          BRUTALIST HELP MENU
          
          quit() or .....
          help() or ?????
          
          no SAVE necessary, as
          the texts saves line-by-line
          
          """,
        session_duration(),
    )
    return


def stat_screen():
    session_duration()
    return


def menu(line):
    quit_command = ["quit()", "....."]
    help_command = ["help()", "?????"]
    stats_command = ["stats()", "/////"]
    if line in quit_command:
        quit_app()
    elif line in help_command:
        help_screen()
    elif line in stats_command:
        stat_screen()
    else:
        return True # was a true line, not a command
    return False # this was a command line


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
    sess_dur = datetime.now() - start_time
    return "session duration: " + humanise_timedelta(sess_dur)


def clear_screen():
    _ = call("cls" if osname == "nt" else "clear")
    return


# MAIN


clear_screen()
save("***")
save("[" + str(datetime.now()) + "]")
save("")
while True:
    line = input("    ")
    print("\n\n")
    if menu(line):
        save(line)

