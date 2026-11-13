games = []

isContinue = True

while isContinue == True:
    answer = input("do you know any games(yes/no): ").lower()

    if answer == "yes":
        games = input("game name: ")
        games.append