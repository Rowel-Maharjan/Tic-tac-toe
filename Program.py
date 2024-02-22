import os
import random,sys

#for the board layout
theBoard = {
    "topL" : " ", "topM" : " ", "topR" : " ",
    "midL" : " ", "midM" : " ", "midR" : " ",
    "bottomL" : " ", "bottomM" : " ", "bottomR" : " ",
}

#To assign the value in dictionary as list is ordered
lst = ["topL", "topM", "topR", "midL", "midM", "midR", "bottomL", "bottomM", "bottomR"]

#To make the board like Big #
def printBoard():
    print(theBoard["topL"] + " | " + theBoard["topM"] + " | " + theBoard["topR"])
    print("--+---+--")
    print(theBoard["midL"] + " | " + theBoard["midM"] + " | " + theBoard["midR"])
    print("--+---+--")
    print(theBoard["bottomL"] + " | " + theBoard["bottomM"] + " | " + theBoard["bottomR"])

def position():
  print("""Press:
  1) TopL      2)TopM       3)TopR
  4) MidR      5)MidM       6)MidR
  7) BottomR   8)BottomM    9)BottomR   
  """)

def check_winner():
  #Row check
  for i in range (0,9,3):
    if theBoard[lst[i]] == theBoard[lst[i+1]] == theBoard[lst[i+2]] != " ":
      return theBoard[lst[i]]

  #colum check
  for i in range(3):  
    if theBoard[lst[i]] == theBoard[lst[i+3]] == theBoard[lst[i+6]] != " ":
       return theBoard[lst[i]]
    
  #Diagonal check
  if theBoard[lst[0]] == theBoard[lst[4]] == theBoard[lst[8]] != " ":
     return theBoard[lst[0]]
  
  if theBoard[lst[2]] == theBoard[lst[4]] == theBoard[lst[6]] != " ":
      return theBoard[lst[2]]
  #Needs to return None as while loop is operating if winner is None
  return None
    
a = "Game of TicTacToe\n"
print(a.center(50))
printBoard()


def play():
  turn = random.choice("XO")
  winner = None
  #while(" " in theBoard.values()):
  while not winner:
      position()

      try:
        move = int(input("Turn for \"" + turn + "\". Move on which space(1-9) "))
      except:
        print("Error! Enter integer")
        continue
      
      if move < 0 or move > 9:
          print("Enter valid input")
          continue
      
      if theBoard[lst[move-1]] != " ":
        print("The position is already filled. Try different postion")
        continue
      
      theBoard[lst[move-1]] = turn
      os.system("cls")
      print("The Board looks like this: ")
      printBoard()
      if turn == "O":
          turn = "X"
      else:
          turn = "O"

      winner = check_winner()
      if " " not in theBoard.values():
        break
  
  if winner:
    print(f"Player \"{winner}\" wins the game")

  else:
    print("Its a tie")

while True:
  play()
  for i in range(9):
     theBoard[lst[i]] = " "
  printBoard()
  end = input("Press Q to quit or any to continue the game: ").lower()
  if end == "q":
     break

print("The game has ended")
