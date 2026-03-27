from random import *
from turtle import *
from casioplot import *

def wait(nb):
  for i in range(nb):
    pass

def plateau():
  penup()
  goto(-75,75)
  pendown()
  setheading(0)
  for i in range(3):
    for j in range(3):
      for k in range(4):
        forward(50)
        right(90)
      forward(50)
    backward(150)
    right(90)
    forward(50)
    setheading(0)
  penup()

def croix(position):
  penup()
  goto(position[0],position[1])
  setheading(45)
  pendown()
  for i in range(4):
    forward(20)
    backward(20)
    left(90)
  penup()

def rond(position):
  goto(position[0],position[1])
  setheading(0)
  pendown()
  circle(20)
  penup()

def jeu(pion,pos):
  a=None
  while a==None:
    a=getkey()
    if a==61:
      if pos[0][0]==[]:
        pos[0][0]=pion
        penup()
        if pion=="X":
          croix((-50,50))
        else:
          rond((-50,30))
        return True
    elif a==62:
      if pos[0][1]==[]:
        pos[0][1]=pion
        penup()
        if pion=="X":
          croix((0,50))
        else:
          rond((0,30))
        return True
    elif a==63:
      if pos[0][2]==[]:
        pos[0][2]=pion
        penup()
        if pion=="X":
          croix((50,50))
        else:
          rond((50,30))
        return True
    elif a==71:
      if pos[1][0]==[]:
        pos[1][0]=pion
        penup()
        if pion=="X":
          croix((-50,0))
        else:
          rond((-50,-20))
        return True
    elif a==72:
      if pos[1][1]==[]:
        pos[1][1]=pion
        penup()
        if pion=="X":
          croix((0,0))
        else:
          rond((0,-20))
        return True
    elif a==73:
      if pos[1][2]==[]:
        pos[1][2]=pion
        penup()
        if pion=="X":
          croix((50,0))
        else:
          rond((50,-20))
        return True
    elif a==81:
      if pos[2][0]==[]:
        pos[2][0]=pion
        penup()
        if pion=="X":
          croix((-50,-50))
        else:
          rond((-50,-70))
        return True
    elif a==82:
      if pos[2][1]==[]:
        pos[2][1]=pion
        penup()
        if pion=="X":
          croix((0,-50))
        else:
          rond((0,-70))
        return True
    elif a==83:
      if pos[2][2]==[]:
        pos[2][2]=pion
        penup()
        if pion=="X":
          croix((50,-50))
        else:
          rond((50,-70))
        return True
    return False

def game(s1,s2):
  pos = [[[],[],[]],[[],[],[]],[[],[],[]]]
  V=None
  tour=0
  run=True
  start()
  plateau()
  while run:
    if tour%2==0:
     pion="X"
    elif tour%2!=0:
      pion="O"
    choix = jeu(pion,pos)
    if choix:
      tour+=1
    if pos[0][0]==pion==pos[0][1]==pos[0][2] or pos[1][0]==pion==pos[1][1]==pos[1][2] or pos[2][0]==pion==pos[2][1]==pos[2][2] or pos[0][0]==pion==pos[1][0]==pos[2][0] or pos[0][1]==pion==pos[1][1]==pos[2][1] or pos[0][2]==pion==pos[1][2]==pos[2][2]:
      V=pion
      run=False
    elif pos[0][0]==pion==pos[1][1]==pos[2][2] or pos[0][2]==pion==pos[1][1]==pos[2][0]:
      V=pion
      run=False
    else:
      if tour>=9:
        V="D"
        run=False
    if V!=None:
      clear()
      penup()
      goto(0,0)
      if V=="X":
        if premier==0:
          write("Le joueur "+J1+" a gagne")
          s1+=1
        else:
          write("Le joueur "+J2+" a gagne")
          s2+=1
      elif V=="O":
        if premier==1:
          write("Le joueur "+J1+" a gagne")
          s1+=1
        else:
          write("Le joueur "+J2+" a gagne")
          s2+=1
      else:
        write("Match nul bien joue")
      wait(200000)
      clear()
      write("Do you want to play again?")
      play=True
      while play:
        key=getkey()
        if key==24 or key==95:
          play=False
          clear()
          game(s1,s2)
        elif key==None:
          pass
        else:
          play=False
          clear()
          write(J1+" : "+str(s1)+" "+J2+" : "+str(s2))

def start():
  global premier
  premier=randint(0,1)
  if premier==0:
    goto(0,0)
    write(J1+" commence")
    wait(200000)
  else: 
    goto(0,0)
    write(J2+" commence")
    wait(200000)
  clear()

J1=input("pseudo de J1:")

if J1=="":
  J1="J1"

if J1!="":
  print(J1,"choisi\n")

J2=input("pseudo de J2:")

if J2=="":
  J2="J2"

if J2!="":  
  print(J2,"choisi\n")

penup()
hideturtle()
s1=0
s2=0  
clear()

game(s1,s2)
