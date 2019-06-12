#!/usr/bin/python
# This script will calculate the alcohol by volume
#  of homebrew cider using 2 formulas

def abv(sg, fg):
	tg = (sg - fg)
	abv = (tg * 0.132) * 1000
	abv = str(abv)
	pABV = str(abv[0:4]) + "%"
	print("Cider ABV (Cider Formula 4-6%): " + pABV)

	tg2 = (76.08 * tg / (1.775 - sg)) * (fg / 0.794)
	tg2 = str(tg2)
	abv2 = str(tg2[0:4]) + "%"
	print("Cider ABV (Wine Formula 10-14%): " + abv2)


sgrav = float(raw_input("Enter starting gravity: "))
fgrav = float(raw_input("Enter final gravity: "))

abv(sgrav, fgrav)
