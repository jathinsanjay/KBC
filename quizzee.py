import click
import time
name=input("Enter your name:")
print("welcome to KBC mr.",name)
time.sleep(2)
click.clear()
questions = [
  "Which of the following is an union territory?",
  "Who is the winner of Ipl 2021",
  "'Good Friday' is observed to commemorate the event of",
  "Who is the costliest player in the history of ipl auction",
  " Which of the-following is wrongly matched?"
]
options = [
  "A.Chennai B.chandigarh C.Bangalore D.mumbai", "A.csk B.rcb C.mi D.kkr ",
  "A.birth of Jesus Christ B.	birth of' St. Peter C.	crucification 'of Jesus Christ D.	rebirth of Jesus Christ",
  "A.sam curran B.Benstokes C.Cameroon green D.virat kohli",
  "A.	Qutab Minar- Delhi B.	Taj Mahal -Agra C.	Ajanta Caves -Maharashtra D.	Charminar -Lucknow"
]
choosen = " "
amountwon = 0
life = 1
lifeline = [
  " B.chandigarh   D.mumbai", "A.csk  C.mi  ",
  " C.	crucification 'of Jesus Christ D.	rebirth of Jesus Christ",
  "A.sam curran B.Benstokes ",
  "C.	Ajanta Caves -Maharashtra D.	Charminar -Lucknow"
]
answers = ["B", "A", "C", "A", "D"]
print(
  "RULES OF GAME:", "\n",
  "1>>There are 5 questions with an increment of 2000 rs for every question..",
  "\n", "2>>Player must answer all the question correctly to win the game,",
  "\n",
  "3>>If any question is answered wrong ,the player is eliminated with the amount he won previously ",
  "\n",
  "4>> If player wins the game ,he gets a bonus of 10,000 rs which gets added to the amount he won previously",
  "\n",
  "5>>You have  1 life line 50:50 which deletes 2 options from choices ,enter '50:50' for lifeline",
  "\n", "\n")
time.sleep(15)
click.clear()


def end():
  print("\n", "\n", "Sorry, you are eliminated , the correct answer is ",
        answers[i], "\n", "You ended up  at", i + 1, "th question")


for i in range(5):
  print(questions[i], "\n")
  print(options[i], "\n")
  choosen = input("choose an option:")
  if choosen == answers[i]:
    print("CONGRATS!! You won ", 2 * (i + 1) * 1000, "rupees", "\n")
    time.sleep(2)
    click.clear()
    amountwon = (i + 1) * 1000
  elif choosen == "50:50" and life == 1:

    print("You chose a life line", "\n", lifeline[i])
    life = 0
    choosen = input("choose an option:")
    if choosen == answers[i]:
      print("CONGRATS!! You won ", 2 * (i + 1) * 1000, "rupees", "\n")
      time.sleep(2)
      click.clear()
    else:
      end()

      break
  elif choosen == "50:50" and life == 0:

    print("You are out of life lines", "\n")

    choosen = input("choose an option:")
    if choosen == answers[i]:
      print("CONGRATS!! You won ", 2 * (i + 1) * 1000, "rupees", "\n")

      time.sleep(2)
      click.clear()
    else:
      end()
      break
  else:
    end()
    break

if i == 4:
  print("JACKPOT!!,You are the winner of game ", name,"..You won Rs.20,000/-")
else:
  print("Hard luck,Mr.",name,"But well done you won rs", amountwon)
