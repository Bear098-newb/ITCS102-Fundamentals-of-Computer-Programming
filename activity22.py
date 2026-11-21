
#shonen
tanjiro = ["son of a coal worker and bearer of the demon slayer mark","tanjiro sun breather"]
zenitsu = ["a scaredy cat but gets serious when asleep","zenitsu thunder breather"]
inosuke = ["grew up in the mountains and has a beast like behaviour","inosuke beast breather"]
demon_salyer = {"1":tanjiro,"2":zenitsu,"3":inosuke}
goku = ["a saiyan sent to earth to survive his planets doom","goku:ultra instinct"]
vegeta = ["prince of the saiyans ","vegeta:ultra ego"]
broly = ["got sent far away from home due to high power level","broly:legendary super saiyan"]
dragon_ball = {"1":goku,"2":vegeta,"3":broly}
Naruto = ["an orphan and the jinchiruki of the nine tails","multi shadow clone jutsu:naruto"]
sasuke = ["sole survivor of the uchiha massacre","SUSSANOO"]
sakura = ["just plain sakura useless all the time","super strength"]
naruto = {"1":Naruto,"2":sasuke,"3":sakura}
#isekai
rudeus = ["got reincarnated to a new world becomiung rudeus","water emperor"]
sylphie = ["a half elf in buena village carrying the laplace factor","water saint"]
eris = ["a noble daughter in the asura kingdom ","sword king"]
mushoku_tensei = {"1":rudeus,"2":sylphie,"3":eris}
ainz = ["the ruler of the tomb of nazarick","Ainz ool gown"]
albedo = ["second in command of the great tomb","albedo magic caster"]
shaltear = ["fourth in command of the great tomb","vampire shaltear"]
Overlord = {"1":ainz,"2":albedo,"3":shaltear}
subaru = ["chosen one to be transported to the other world","RETURN BY DEATH"]
emilia = ["half elf magic caster","ice magic"]
roswaal = ["villain of the world ","ROSWAAL MAGIC CASTER"]
Re_zero = {"1":subaru,"2":emilia,"3":roswaal}



shonen = {"1":demon_salyer,"2":dragon_ball,"3":naruto}
isekai = {"1":mushoku_tensei,"2":Overlord,"3":Re_zero}
anime = [shonen,isekai]
animes_d = {"1":shonen,"2":isekai}

genre_names = {"1": "shonen", "2": "isekai"}
title_names = {
    "1": {"1": "demon slayer", "2": "dragon ball", "3": "naruto"},
    "2": {"1": "mushoku tensei", "2": "Overlord", "3": "Re:zero"}
}
character_names = {
    "1": {
        "1": {"1": "tanjiro kamado", "2": "zenitsu", "3": "inosuke"},
        "2": {"1": "goku", "2": "vegeta", "3": "broly"},
        "3": {"1": "naruto", "2": "sasuke", "3": "sakura"}
    },
    "2": {
        "1": {"1": "rudeus", "2": "sylphie", "3": "eris"},
        "2": {"1": "ainz", "2": "albedo", "3": "shaltear"},
        "3": {"1": "subaru", "2": "emilia", "3": "roswaal"}
    }
}

title_menus = {
    "1": "[1]demon slayer \n[2]dragon ball \n[3]naruto",
    "2": "[1]mushoku tensei \n[2]Overlord \n[3]Re:zero"
}
character_menus = {
    "1": {
        "1": "[1]tanjiro \n[2]zenitsu \n[3]inosuke",
        "2": "[1]goku \n[2]vegeta \n[3]broly",
        "3": "[1]naruto \n[2]sasuke \n[3]sakura"
    },
    "2": {
        "1": "[1]rudeus \n[2]sylphie \n[3]eris",
        "2": "[1]ainz \n[2]albedo \n[3]shaltear",
        "3": "[1]subaru \n[2]emilia \n[3]roswaal"
    }
}

print("========choose a genre========")
print("[1]shonen \n[2]isekai")
print("==============================")
genre_choice = input("choice: ")

if genre_choice in genre_names:
    print(genre_names[genre_choice] + " chosen: Titles")
    print(title_menus[genre_choice])
    title_choice = input("choice: ")

    if title_choice in title_names[genre_choice]:
        print("===", title_names[genre_choice][title_choice], "===")
        print(character_menus[genre_choice][title_choice])
        character_choice = input("choose a character: ")

        if character_choice in character_names[genre_choice][title_choice]:
            character = character_names[genre_choice][title_choice][character_choice]
            details = animes_d[genre_choice][title_choice][character_choice]
            print(character + ":", details)
        else:
            print("error:404 invalid character choice")
    else:
        print("error:404 invalid title choice")
else:
    print("error:404 invalid choice")
