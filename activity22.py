#shonen
tanjiro = ["water","sun","smell"]
zenitsu = ["hearing","six fold","godspeed"]
inosuke = ["touch","beast","dual blade"]
demon_salyer = [tanjiro,zenitsu,inosuke]
goku = ["kamehameha","super saiyan","instant transmission"]
vegeta = ["galick gun","ego","battle armor"]
broly = ["legendary","green","big"]
dragon_ball = [goku,vegeta,broly]
Naruto = ["shadow clone","rasengun","rasenshiruken"]
sasuke = ["chidori","sharingan","amaterasu"]
sakura = ["strong","medic","useless"]
naruto = [Naruto,sasuke,sakura]
#isekai
rudeus = ["water magic","earth magic","fire magic"]
sylphie = ["water magic","healing magic","elf"]
eris = ["sword emperor","north saint","water king"]
mushoku_tensei = [rudeus,sylphie,eris]
ainz = ["skeleton","magic caster","swordsman"]
albedo = ["wings","succubus","lvl999"]
shaltear = ["vampire","lvl999","life steal"]
Overlord = [ainz,albedo,shaltear]
subaru = ["return by death","weak"]
emilia = ["useless","magic"]
roswaal = ["vilain","martial arts","multi casing"]
Re_zero = [subaru,emilia,roswaal]
#comedy
kazuma = ["steal","luck","water"]
aqua = ["bad luck","water purification","goddess"]
megumin = ["explosion""staff","fire"]
KonoSuba = [kazuma,aqua,megumin]
saiki = ["teleport","mind reading","psychic"]
nendou = ["dumb","unreadable","funny"]
kaido = ["imaginative""funny","also dumb"]
Saiki_k = [saiki,nendou,kaido]
gintoki = ["swordsmanship","toned","unserious"]
kagura = ["strength","speed","regeneration"]
shinpachi = ["swordsmanship","normal human"]
Gintama = [gintoki,kagura,shinpachi]


shonen = [demon_salyer,dragon_ball,naruto]
isekai = [mushoku_tensei,Overlord,Re_zero]
comedy = [KonoSuba,Saiki_k,Gintama]
animes = [shonen,isekai,comedy]
animes_d = {"fighting":shonen,"fantasy":isekai,"tawa":comedy}

print(animes[0][0][0])
print("\n")
print(animes_d["fighting"][-1][0])
