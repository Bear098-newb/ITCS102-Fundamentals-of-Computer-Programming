games = []

answer = input("do you know any games(yes/no): ").lower()

if answer == "yes":
    while True:
        games.append(input("game name: "))
        tuloy = input("continue?(yes/no): ").lower()
        if tuloy != "yes":
            break

print(games)
