import math
import time
import random

#Potential User Response
answer_next = ["NEXT", "next", "n","N", "Next"]
answer_easy = ["E", "e","easy","EASY", "Easy"]
answer_medium = ["M", "m", "medium", "MEDIUM", "Medium"]
answer_hard = ["H", "h", "HARD", "Hard", "hard"]
answer_yes = ["Y","y","Yes","YES","yes"]
answer_no = ["N","n","NO","no","No"]
answer_repeat = ["R","r","REPEAT","Repeat","repeat"]


def print_and_wait(msg):
  print(msg)
  time.sleep(1)

#Game Begin Screen - Explaining how you lose
def begin(): 
  #Global Data - Add Lockdown
  global china, vaccine, answer_lockdown
  china = {
  "population": 1400000000,
  "infected": 10000,
  "dead": 0
  }
  vaccine = {
 "position": 0,
 "completion" : random.randint(10,12)
  }
  answer_lockdown = ["L", "l", "LOCKDOWN", "lockdown", "Lockdown"]
  
  username = input("\nWelcome, please enter your name\n> ")
  
  print_and_wait("\nHello " + username + "!\nWelcome to the Coronavirus Simulator.")
  
  print_and_wait("\nChina is currently facing an outbreak of COVID."
  "\nYou must contain the virus.")
  
  print_and_wait("\nThese are the current stats for China:\nPopulation: "+ str(f'{china["population"]:,}') + "\nInfected: " + str(f'{china["infected"]:,}')+ "\nDead: " + str(f'{china["dead"]:,}'))
  
  print_and_wait("\nEach round the # of infected will grow by the R rate."
  "\nIf COVID infects the entire population, you lose.")
  
  rules()


#After the Beginning - Explaining how you win - Vaccine/Lockdown stuff
def rules():
  interest = input("\nAre you interested in finding out how you win? Y/N\n")
  if interest in answer_no:
    print_and_wait("\n....brave, best of luck!")
    intro()
  if interest in answer_yes:  
    print_and_wait("\nFigure it out on your own.")
    print_and_wait("There's a vaccine involved and an opportunity \nto implement a national lockdown.")
    intro()
  else: 
    print_and_wait("\nRe-read the question... you didn't say Y or N!")
    rules()

#difficulty Selection
def intro():
  choice = input("\nNow choose an option - easy(e), medium(m) or hard(h)?\n> ")
  if choice in answer_easy:
    gameCycle(1.2)
  elif choice in answer_medium:
    gameCycle(1.3)
  elif choice in answer_hard:
    gameCycle(1.5)
  else:
    print("Sorry, that wasn't quite right!")
    return intro()


#Actual Game Function
def gameCycle(R, lockdown=False):
  global china, vaccine, answer_lockdown, lockdown_progress
  lockdown_progress = 0
  #Main while loop that ensures it only continues if infected population is lower than dead population
  while china["infected"] < china["population"]:
    # Increase the rate of R by 5% every round
    R += R*0.05
    china["infected"], china["dead"] = corona_spread(china["infected"], R)
    if china["infected"] > china["population"] :
      everyone_infected()
      startAgain()
      break
    # Below, 1 is added to var "vaccine" each turn. Game ends when this is equal to the number randomly selected above
    vaccine["position"] += 1
    #Scenario where vaccine is completed
    if vaccine["position"] == vaccine["completion"]:
      vaccine_produced()
      startAgain()
      break
    # The 5 print statements giving general update  
    general_update(R, lockdown)

    #remove this completely = too many ifs/while
    call_out_to_user(answer_lockdown)
    while next_step not in answer_next and next_step not in answer_lockdown:
      call_out_to_user(answer_lockdown)
    if next_step in answer_lockdown:
      lockdown = True
      # If lockdown is activated - increase the number of days to vaccine completion.
      # The earlier the lockdown, the lower the increase.
      vaccine["completion"] += random.randint(round(0.6 * vaccine["position"]),round(1 * vaccine["position"]))
      answer_lockdown = []
    if lockdown is True:
      lockdown_progress += 1
      # Reduce the rate of R as lockdown continues
      R -= 0.3
    if lockdown_progress == 4:
      lockdown = False
      # Restore R rate to pre-lockdown rate
      R += (lockdown_progress+1)*0.2
      lockdown_progress += 1
      
def call_out_to_user(answer_lockdown):
  global next_step
  if len(answer_lockdown) > 0:
    next_step = input("Type next(n) to continue, or type lockdown(l) to implement a national lockdown\n> ")
    return next_step
  else:
    next_step = input("Type next(n) to continue (you have used your lockdown option.)\n> ") 
    return next_step  

# Rate of Spread Calculation  
def corona_spread(infected, rInfection):
  # Each turn, the number of infected grows randomly by between: 0.75R and 1.25R * currently infected 
  # This is applied whatever the rate of 'R' is e.g. R = 1.6 on hard mode, so (0.75(1.6)*currently infected) would be the smallest increase each turn on hard mode
  infected += random.randint(math.trunc(infected *rInfection-(infected*rInfection)/4),math.trunc(infected*rInfection +(infected*rInfection)/4))
  # Each turn, the number of dead grows randomly by between 1% and 2% of the number of infected
  dead = random.randint(math.trunc(infected/100),math.trunc(infected/50)) 
  return infected, dead
  
# vaccine completed update used in GameCycle  
def vaccine_produced():
      print("\nA vaccine has been completed! You win!")
      print("\nInfected: " + str(f'{china["infected"]:,}'))
      print("Dead: " + str(f'{china["dead"]:,}'))

# Everyone infected update used in GameCycle
def everyone_infected():
      print("\nEverybody is infected! You lose")
      print("Dead: " + str(f'{china["dead"]:,}'))

# General Update every round used in the GameCycle
def general_update(R, lockdown):
    print("\nChina lockdown status: " + str(lockdown))  
    print("The current rate of R is " + str(round(R,2)))
    print("Infected: " + str(f'{china["infected"]:,}'))
    print("Dead: " + str(f'{china["dead"]:,}'))
    print("Number of rounds until vaccine: "+ str(vaccine["completion"] - vaccine["position"]))

#Start Again
def startAgain():
  time.sleep(1)
  option = input("\nIf you would like to play again, type repeat (r).\n"
  "If you don't, type anything else.\n")
  if option in answer_repeat:
    # The variables need resetting! Make more efficient?
    begin()
  else:  
    print("\nThank you for playing Coronavirus Simulator!")
    exit()

#Actually Start the Game
begin()



#Final tasks
#Stop using IF's and start using alternative
#Lockdown into its own function
#Allow game repeat if vaccine achieved
#Game is less playable 
#ADD COMMAS BACK IN
#lockdown dictionary?
