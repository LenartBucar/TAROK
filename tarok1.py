#Simulator deljenja tarok kart
#Ugotovi odstotek nelegalnih razdelitev kart v izbranem stevilu partij
#Gregor Gajič, 2017

import random
import time

legalne = 0

n = int(input("Koliko partij taroka naj razdelim? "))

start = time.time()

for i in range(1,n+1):
    tarok = list(range(1, 55)) #naj bojo 1-22 taroki ;)
    #talon = []
    igralec1 = []
    igralec2 = []
    igralec3 = []
    igralec4 = []

    if i%10000 == 0 and i != n:
        print("\nSem pri partiji "+str(i))
        print("Trenutno je bilo legalnih "+str((legalne*100/i))+" odstotkov rok.")
        print("Nelegalnih je bilo "+str((100-(legalne*100/i)))+" odstotkov rok.")

    for e in range(0,6): #talon
        #karta = random.choice(tarok)
        #talon.append(karta)
        #tarok.remove(karta)
        tarok.remove(random.choice(tarok))

    for e in range(0,2): #players
        for igralec in range(0,6):
            karta = random.choice(tarok)
            igralec1.append(karta)
            tarok.remove(karta)
        for igralec in range(0,6):
            karta = random.choice(tarok)
            igralec2.append(karta)
            tarok.remove(karta)
        for igralec in range(0,6):
            karta = random.choice(tarok)
            igralec3.append(karta)
            tarok.remove(karta)
        for igralec in range(0,6):
            karta = random.choice(tarok)
            igralec4.append(karta)
            tarok.remove(karta)

    st_igralcev_legalne = 0
    for e in range(1,23):
        if e in igralec1:
            st_igralcev_legalne += 1
            break
    for e in range(1,23):
        if e in igralec2:
            st_igralcev_legalne += 1
            break
    for e in range(1,23):
        if e in igralec3:
            st_igralcev_legalne += 1
            break
    for e in range(1,23):
        if e in igralec4:
            st_igralcev_legalne += 1
            break

    if st_igralcev_legalne > 3:
        legalne += 1

print("\n\nKONEC")
print("Legalnih je bilo "+str((legalne*100/n))+" rok.")
print("Nelegalnih je bilo "+str((100-(legalne*100/n)))+" rok.")

print(time.time() - start)
