#   1 | 2 | 3 
#  ---+---+---
#   4 | 5 | 6 
#  ---+---+---
#   7 | 8 | 9
#  visas ovan är exempel på spelbräde
#  3x3 rutor, lägg ett nummer från vänster 1,2,3...9 som motsvara p1,p2,p3...p9 i koden   

p1=p2=p3=p4=p5=p6=p7=p8=p9=' '
flag = int(1)

# Visa spelbrädet på skärmen
def display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9) :
    print (f"\n+---+---+---+\n| {p1} | {p2} | {p3} |\n|---+---+---|\
    \n| {p4} | {p5} | {p6} |\n|---+---+---|\n| {p7} | {p8} | {p9} |\n+---+---+---+")
display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9)
     
player1_sign = input("Välj en av markörer antingen 'X' eller 'O' =>"  ).upper()

if player1_sign == 'X'  :
    player2_sign = 'O'
else :
    player2_sign = 'X'

#om spelare1 väljer en ruta som redan valt
def move_coordinator_player1(move):
    global flag 
    if(move==1) :
        global p1
        if(p1!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1 
        else : 
            p1 = player1_sign
    if(move==2) :
        global p2 
        if(p2!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p2 = player1_sign
    if(move==3) :
        global p3 
        if(p3!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p3 = player1_sign
    if(move==4) :
        global p4 
        if(p4!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p4 = player1_sign
    if(move==5) :
        global p5
        if(p5!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p5 = player1_sign
    if(move==6) :
        global p6
        if(p6!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p6 = player1_sign
    if(move==7) :
        global p7 
        if(p7!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p7 = player1_sign
    if(move==8) :
        global p8 
        if(p8!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p8 = player1_sign
    if(move==9) :
        global p9 
        if(p9!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 1
        else : 
            p9 = player1_sign

#om spelare2 väljer en ruta som redan valt
def move_coordinator_player2(move):
    global flag
    if(move==1) :
        global p1
        if(p1!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p1 = player2_sign
    if(move==2) :
        global p2 
        if(p2!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p2 = player2_sign
    if(move==3) :
        global p3 
        if(p3!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p3 = player2_sign
    if(move==4) :
        global p4 
        if(p4!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p4 = player2_sign
    if(move==5) :
        global p5
        if(p5!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p5 = player2_sign
    if(move==6) :
        global p6
        if(p6!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p6 = player2_sign
    if(move==7) :
        global p7 
        if(p7!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p7 = player2_sign
    if(move==8) :
        global p8 
        if(p8!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p8 = player2_sign
    if(move==9) :
        global p9 
        if(p9!=' ') : 
            print("Ogiltig Ruta !!!")
            flag = 2
        else : 
            p9 = player2_sign


#spela turas om med, varannan gång väljer spelare en ruta
def move_enterer() :
    global flag
    if(flag==1) :
        move = int(input("Spelare 1: Ange ditt drag =>1-9 :"))
        flag = 2
        move_coordinator_player1(move)
    else :
        move = int(input("Spelare 2: Ange ditt drag =>1-9 :"))
        flag = 1
        move_coordinator_player2(move)

winner_name = ""

#detektera vilken spelare är vunna
def win_detector(p1,p2,p3,p4,p5,p6,p7,p8,p9) :
    global winner_name
    if p1!=' ' and p1!=' ' and p2!=' ' and p3!=' ' and p4!=' ' and p5!=' ' and p6!=' ' and p7!=' ' and p8!=' ' and p9!=' ' :  
        winner_name = "None"
        return False
    if p1==p2 and p2==p3 and p1 not in ' ' and p2 not in ' ' and p3 not in ' ' :
        if(p1 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    elif p4==p5 and p5==p6 and p4 not in ' ' and p5 not in ' ' and p6 not in ' ' :
        if(p4 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    elif p7==p8 and p8==p9 and p7 not in ' ' and p8 not in ' ' and p9 not in ' ' :
        if(p7 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    elif p1==p4 and p4==p7 and p1 not in ' ' and p4 not in ' ' and p7 not in ' ' :
        if(p1 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    elif p2==p5 and p5==p8 and p2 not in ' ' and p5 not in ' ' and p8 not in ' ' :
        if(p2 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    elif p3==p6 and p6==p9 and p3 not in ' ' and p6 not in ' ' and p9 not in ' ' :
        if(p3 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    elif p3==p5 and p5==p7 and p3 not in ' ' and p5 not in ' ' and p7 not in ' ' :
        if(p3 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    elif p1==p5 and p5==p9 and p1 not in ' ' and p5 not in ' ' and p9 not in ' ' :
        if(p1 == player1_sign) :
            winner_name = 'Spelare 1'
        else :
            winner_name = 'Spelare 2'
        return False
    else :
        return True

while(win_detector(p1,p2,p3,p4,p5,p6,p7,p8,p9)) :
    move_enterer()
    display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9) 
    
    
if winner_name != 'None' :
    print(f"\n\n\n\t\tHurra!  , Vinnare är: {winner_name}" )
else :
    print("\n\n\n\t\tIngen hade vunnit: Oavgjord )")

