
import random

class Snail:
 def __init__(self, color):
     self.color = color
     self.distance = 0

def move(self):
    self.distance += random.randint(0, 3)

def boost(self):
    self.distance += random.randint(0, 3) * 2

class SnailRace:
 def __init__(self):
     self.snails = [Snail("piros"), Snail("zöld"), Snail("kék")]
     self.rounds = 5

def race(self):
  for round_number in range(1, self.rounds + 1):
    print(f"\n{round_number}. kör:")
    for snail in self.snails:
      if random.random() < 0.2:  #20% esély a gyorsításra
           snail.boost()
         print(f"{snail.color} csiga gyorsítót kapott!")
       else:
           snail.move()
      print(f"{snail.color} csiga pozíciója:
{snail.distance}")

   winner = max(self.snails, key=lambda s: s.distance)
   print(f"\nA győztes a {winner.color} csiga
{winner.distance} egységgel!")
   return winner.color

print("Üdvözöljük a Csigaversenyen!")
bet = input("Melyik csigára fogad? (piros/zöld/kék): ").lower()

race = SnailRace()
winner = race.race()

if bet == winner:
 print("Gratulálunk, nyert a fogadása!")
else:
 print(f"Sajnos vesztett. A {winner} csiga nyert.")

