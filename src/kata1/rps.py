from random import randint

options = ["Piedra", "Papel", "Tijeras"]
pierde_contra = ["papel", "tijeras", "piedra"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
	player = player.lower()
	ai = ai.lower()

	if player == ai:
		return "Empate!"

	if player == "piedra":
		if pierde_contra[0] == ai:
			return "Perdiste!"
		else: 
			return "Ganaste!"
	elif player == "papel":
		if pierde_contra[1] == ai:
			return "Perdiste!"
		else: 
			return "Ganaste!"
	elif player == "tijeras":
		if pierde_contra[2] == ai:
			return "Perdiste!"
		else: 
			return "Ganaste!"



# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player,ai)

    print(winner)