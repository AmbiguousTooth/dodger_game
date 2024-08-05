import pygame

def read_highscore():
	try:
		with open("score.txt","r") as file:
			highscore = int(file.read())
	except FileNotFound:
		highscore = 0;

	return highscore

def write_highscore(score):
	with open("score.txt", "w") as file:
		file.write(str(score))
