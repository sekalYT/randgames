import time
import random

def selectlanguage():
	print("Select language")
	print("Выберите язык")
	print("1 - English | Английский")
	print("2 - Russian | Русский")
	language = input()
	if language == "1":
		EN()
	if language == "2":
		RU()
		
def EN():
	print("Select the gamemode")
	print("********************")
	print("1 - Dice")
	print("2 - Slots")
	print("3 - Random number")
	print("4 - Coinflip")
	print("5 - Select language")
	choiceen = input()
	if choiceen == "1":
		diceen()
	if choiceen == "2":
		slotsen()
	if choiceen == "3":
		randomnumberen()
	if choiceen == "4":
		 coinflipen()
	if choiceen == "5":
		selectlanguage()

def diceen():
			print("Throwing the dice...")
			time.sleep(0.5)
			dice1 = random.randint(1, 6)
			print(f"Your number is {dice1}")
			time.sleep(0.5)
			print("Retry - 1")
			print("Main menu - 2")
			choiceen2 = input()
			if choiceen2 == "1":
				diceen()
			if choiceen2 == "2":
				EN()

def slotsen():
	slotsen1 = random.randint(1, 9)
	slotsen2 = random.randint(1, 9)
	slotsen3 = random.randint(1, 9)
	
	print(f"{slotsen1} {slotsen2} {slotsen3}")
	time.sleep(0.5)
	print("Retry?")
	print("Yeah - 1")
	print("Main menu - 2")
	choiceslotsen = input()
	if choiceslotsen == "1":
		slotsen()
	if choiceslotsen == "2":
		EN()

def randomnumberen():
	print("Write a min number")
	minnumber = input(int)
	print("Write a max number")
	maxnumber = input(int)
	rand1 = random.randint(int(minnumber), int(maxnumber))
	print(f"Your number - {rand1}")
	print("Retry - 1")
	print("Main Menu - 2")
	choiceennumber1 = input()
	if choiceennumber1 == "1":
		randomnumberen()
	if choiceennumber1 == "2":
		EN()

def RU():
	print("Выберите режим игры")
	print("********************")
	print("1 - Бросить кубик")
	print("2 - Слоты")
	print("3 - Случайное число")
	print("4 - Бросить монетку")
	print("5 - Изменить язык")
	choiceru = input()
	if choiceru == "1":
		diceru()
	if choiceru == "2":
		slotsru()
	if choiceru == "3":
		randomnumberru()
	if choiceru == "4":
		coinflipru()
	if choiceru == "5":
		selectlanguage()


def diceru():
			print("Бросаем кубик...")
			time.sleep(0.5)
			dice1 = random.randint(1, 6)
			print(f"Вам выпало число {dice1}")
			time.sleep(0.5)
			print("Бросить ещё раз - 1")
			print("Главное меню - 2")
			choiceru2 = input()
			if choiceru2 == "1":
				diceru()
			if choiceru2 == "2":
				RU()

def slotsru():
	slotsru1 = random.randint(1, 9)
	slotsru2 = random.randint(1, 9)
	slotsru3 = random.randint(1, 9)
	
	print(f"{slotsru1} {slotsru2} {slotsru3}")
	time.sleep(0.5)
	print("Крутануть еще раз слот-машину?")
	print("Да - 1")
	print("Главное меню - 2")
	choiceslotsru = input()
	if choiceslotsru == "1":
		slotsru()
	if choiceslotsru == "2":
		RU()
		
def randomnumberru():
	print("Укажите минимальное значение")
	minnumber = input(int)
	print("Укажите максимальное значение")
	maxnumber = input(int)
	rand = random.randint(int(minnumber), int(maxnumber))
	print(f"Ваше число - {rand}")
	print("Повторить - 1")
	print("Главное меню - 2")
	choicerunumber1 = input()
	if choicerunumber1 == "1":
		randomnumberru()
	if choicerunumber1 == "2":
		RU()
	
def coinflipru():
	possible_actions = ["Орёл", "Решка"]
	coinflipp = random.choice(possible_actions)
	print("********************")
	print(f"{coinflipp}")
	print("********************")
	RU()

def coinflipen():
	possible_actions = ["Eagle", "Tails"]
	coinflip1 = random.choice(possible_actions)
	print("********************")
	print(f"{coinflip1}")
	print("********************")
	EN()
	
selectlanguage()
