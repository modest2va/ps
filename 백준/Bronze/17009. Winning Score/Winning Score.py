scorea,scoreb=0,0
scorea+=int(input())*3
scorea+=int(input())*2
scorea+=int(input())*1
scoreb+=int(input())*3
scoreb+=int(input())*2
scoreb+=int(input())*1

if scorea>scoreb:print("A")
elif scorea==scoreb:print("T")
else:print("B")