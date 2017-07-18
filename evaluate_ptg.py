#!/usr/bin/env python

from ptg import PTG
from helpers import Vehicle, show_trajectory

def main():
	vehicle = Vehicle([0,10,0, 0,0,0]) # creates vehicle with s, v, acc for s and d
	predictions = {0: vehicle}         # dict of vehicles
	target = 0                         # follow vehicle indes
	delta = [-6, 0, 0, 0, 0 ,0]
	start_s = [10, 10, 0]              # for ego vehicle
	start_d = [4, 0, 0]
	T = 5.0
	best = PTG(start_s, start_d, target, delta, T, predictions)
	show_trajectory(best[0], best[1], best[2], vehicle)

if __name__ == "__main__":
	main()