# import modules
import random

# make a list of drinks and randomly select one
drinks = ['gin and tonic', 'coffee', 'grape soda', 'mint tea']
drink_order = random.choice(drinks)

# default to not being a ghost
a_ghost = False

# get the total number of people in the party
def get_party():
	# ask how many are in the party
	party_total = raw_input("\"How many in your party?\" > ")

	# if the answer is a string of digits only, turn it into an integer
	if party_total.isdigit():
		party_total = int(party_total)

		# if the party is more than 6, require a reservation
		if party_total > 6:
			a_reservation()

		# if the party is 0, you are possibly a ghost
		elif party_total == 0:
			ghost_check()

		# if you are by yourself
		elif party_total == 1:
			print "The staff person says, \"You are very brave, and very welcome.\""
			get_seated()

		else:
			print "\"%s, very good.\"" % party_total
			get_seated()

	# if the answer is blank, also maybe be a ghost
	elif not party_total:
		ghost_check()

	# otherwise seat the nonsense string of people
	else:
		print "The staff person says, \"How wonderful!"
		print "We always have a table for %s." % party_total
		get_seated()

# set up needing a reservation
def a_reservation():
	print "The staff person says, \"Oh, I'm very sorry."
	print "We require a reservation for parties larger than 6.\""
	print "This is ridiculous. The restaurant is empty."

	# argue or not about a reservation
	cause_a_scene = raw_input("Do you argue with the staff person? > ")

	if "yes" in cause_a_scene:
		print "The staff person shakes their head gravely and intones,"
		print "\"Please, do not return.\""
		print "You find yourself transported to the outside of the restaurant."
		print "It appears closed. You go home and write a Yelp review for it,"
		print "although you have a hard time remember what the interior looked"
		print "like, or the face of the staff person you met. You wanted to give"
		print "it zero stars, but your only option as you fill out the form is to"
		print "give it five black stones."

	else:
		print "You mutter under your breath and leave the restaurant."
		print "You go instead to the corner bar with your friends and get beers"
		print "and a large order of nachos. You have a quiet but pleasant evening."
		print "You never return."

# check ghost status
def ghost_check():
	global a_ghost
	print "The staff person looks solemn."
	print "\"Are you a ghost? It's not a problem.\""
	actually_a_ghost = raw_input("Are you actually a ghost? > ")

	# if you are truly ghost, get seated in the ghost section
	if "yes" in actually_a_ghost:
		print "The staff person nods."
		print "\"I can seat you in our special ghost section.\""
		a_ghost = True
		get_seated()

	# otherwise, get asked again
	else:
		print "The staff person smiles."
		print "\"Oh, I must have misunderstood.\""
		get_party()

# set (up) the table
def the_table():
	print "Once seated, you try to order a %s." % drink_order
	print "TO BE CONTINUED...................."

# get seated at the table
def get_seated():
	print "The staff person makes a small bow."
	print "\"Please come this way.\""
	print "You follow the staff person to your table."
	the_table()

# set up the restaurant lobby
def the_lobby():
	print "You enter a restaurant."
	print "It is a new restaurant, with a very strange name."
	print "Everyone is talking about it but no one seems to have been."
	print "You want to see if the mystery is justified."
	print "A staff person approaches you and says, \"Hello, welcome to Dinner: The Game.\""
	get_party()

# start the game
the_lobby()