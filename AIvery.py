import time

def pause(num):
    """Pauses the program for a given amount of time"""
    time.sleep(num)


def line(text):
    """Displays a line of text, then pauses the program for one second"""
    print(text)
    pause(1)


pronountype_a = ['he/him/his', "she/her/hers", "it/its", "fleur/fleurs"]
pronountype_b = ["they/them/theirs", "fae/faer/faers", "fey/fem/feirs"]
pronouns = ['he/him/his', "she/her/hers", "it/its", "fleur/fleurs",
"they/them/theirs", "fae/faer/faers", "fey/fem/feirs"]

line("Greetings!")
line("AIvery 0.0.0.2 loaded.")
line("Please enter your name.")
username = input(">>> ")
line(f"Is {username} your name?")
confirm = input("Y/N>>> ")
while confirm.lower() not in 'yn':
    line("Error One: Invalid Input.")
    line("This question requires a y/n answer.")
    confirm = input("Y/N>>> ")

while confirm.lower() != 'y':
    line("Apologies, I must have misheard.")
    line("Please enter your name.")
    username = input(">>> ")
    line(f"Is {username} your name?")
    confirm = input("Y/N>>> ")

line("It is time to choose a set of pronouns, to make your experience more pleasant.")
line("At present, I have He/Him/His, She/Her/Hers, They/Them/Theirs, and"
" It/Its in my database.")
line("In addition to this, I am also familiar with a few sets of neopronouns."
" Would you like to view them?")
answer = input("Y/N>>> ")
while answer.lower() not in "yn":
    line("Error One: Invalid Input.")
    line("This question requires a y/n answer.")
    answer = input("Y/N>>> ")

if answer.lower() == 'y':
    line("Available neopronoun sets are: Fae/Faer/Faers, Fey/Fem/Feirs,"
    " Fleur/Fleurs.")
    line("If your pronouns are not in this list, please contact the developer")

line("Please select a set of pronouns.")
pronoun_select = input(">>> ")
while pronoun_select.lower() not in pronouns:
    line("Error Two: Pronouns not recognised.")
    line("If you wish for your pronouns to be included in my database, please"
    " contact the developer.")
    line("Please enter a set of pronouns")
    pronoun_select = input(">>> ")
user_pronouns = pronoun_select
line("Thank you for completing the startup protocol.")
line("Standard functions beginning now.")
while True:
    line("How may I help you?")
    query = input(">>> ")
    if "what is your gender" in query.lower() or "what gender or you" in query.lower():
        line("I, AIvery, am above your human concept of gender.")
        line("For ease of use, however, I use the pronouns they/them.")
    else:
        line(f"I am afraid I do not understand, {username}")
        line("Please try wording the query differently, or checking the list"
        " of available queries.")
        line("If you think there is an error or mistake, please report this"
        " to the developer.")