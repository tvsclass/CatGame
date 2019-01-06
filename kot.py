print("прив. приветствую в игре про котов!")

Roma_ud=(0)
Mur_ud=(0)
lotok=(0)

def stat():
 printr("СТАТИСТИКА:",0)
 ent(2)
 if (lotok > 0):
  print("надо почистить лоток.")
  ent(2)
 print("удовольствие Ромео = " + str(Roma_ud)
+ " из 10")
 print("удовольствие Мурчика = " +
str(Mur_ud) + " из 10")
 catchange=("0")
 ent(2)
 wait()
 return catchange

def printr(word,ots):
 ent(1)
 razdel()
 if (ots > 0):
  ent(ots)
 print(word)
 if (ots > 0):
  ent(ots)
 razdel()
 ent(1)

class Cat:
 def __init__(self,color,name,kakur):
  self.color=color
  self.name=name
  self.kakur=kakur

Roma=Cat("чёрный","Ромео","пытается урчать, но не умеет...")

Mur=Cat("Серый","Мурчик","*громко урчит*")

def wait():
 input("нажмите enter для продолжения")
def ent(q):
 print("\n" *q)
ent(3)
def razdel():
 print("===============================")
razdel()
ent(1)
name_pl=(input("как тебя зовут? "))
catchange=("0")

while True:
 if (catchange == "Ромео"):

  while True:
   razdel()
   print("прив. я " + Roma.color + " кот "
+ Roma.name + ". мяу")
   razdel()
   chto=(input("что с ним делать? "))
   if (chto == "погладить"):
    razdel()
    print(Roma.kakur)
    razdel()
    ent(1)
    Roma_ud+=1
   elif (chto == "ударить"):
    ent(5)
    razdel()
    ent(1)
    print(name_pl + "," + " ты чо")
    ent(1)
    razdel()
    ent(3)
    Roma_ud=(-5)
    catchange=('0')
    break
   elif (chto == "ничего"):
    catchange=('0')
    break
   elif (chto == "покормить"):
    ent(5)
    razdel()
    print("*яростно пожирает еду*")
    lotok=(lotok + 1)
    razdel()
    ent(5)
    Roma_ud+=5


   wait()

 elif (catchange == "Мурчик"):

  while True:
   if (lotok > 0):
    razdel()
    print("ПОЧИСТИТЕ ЛОТОК!")
    razdel()
   chin=(input("Чистить лоток?"))
   if (chin == "да"):
    printr("Чищу...",0)
    lotok-=1
    printr("почистил",0)
    wait()
    razdel()
   if (chin == "нет"):
    print("прив. я " + Mur.color + " кот "
+ Mur.name + ". мяу")
    razdel()
    chto=(input("что с ним делать? "))
   if (chto == "погладить"):
    ent(5)
    razdel()
    print(Mur.kakur)
    razdel()
    ent(5)
    Mur_ud+=3
   elif (chto == "ударить"):
    razdel()
    ent(1)
    print(name_pl + "," + " ты чо")
    ent(1)
    razdel()
    Mur_ud=(-5)
   elif (chto == "ничего"):
    catchange=("0")
    break
   elif (chto == "покормить"):
    ent(5)
    razdel()
    print("*акуратно съедает кусочки*")
    razdel()
    ent(5)
    Mur_ud+=3
    lotok=(lotok+1)
 elif (catchange == "выйти"):
  break
 elif (catchange == "статистика"):
  catchange=(stat())
 else:
  printr("выбирите кота",0)
  ent(6)
  printr("Ромео",0)
  printr("Мурчик",0)
  ent(1)
  catchange=(input("Выберите кота: "))
stat()

