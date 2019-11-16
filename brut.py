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
    return


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
    """Returns [str] "session duration: XX:XX:XX:XXXXXX"""
    sess_dur = datetime.now() - start_time
    return "session duration: " + humanise_timedelta(sess_dur)


def clear_screen():
    _ = call("cls" if osname == "nt" else "clear")
    return


# humanise_timedelta(datetime.now())
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
    menu(line)
    save(line)

