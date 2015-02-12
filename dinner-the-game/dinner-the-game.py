# Player: a player
#	- Ghost Player: a player who is also a ghost
# Map: our world
# Engine: a machine that creates change
# Zone: a part of the map to go to
	# Sidewalk: where it all begins
	# Restaurant: a strange restaurant
	# Dungeon: a particular type of zone (composition w/ Monster)
		# Dungeon A: the first dungeon zone 
		# Dungeon B: the second dungeon zone
		# Dungeon C: the third dungeon zone
	# Escape: escape from the dungeon
	# Death: failure
# Monster: a creature that lives in a dungeon (composition w/ Dungeon)

import random

class Player(object):
	def inheritence(self):
		print "I'm a player!"

class Ghost(Player):
	def inheritence(self):
		print "I'm a player who is a ghost!"

class Monster(object):

	# randomly generate some monster qualities
	monster_kind = [
		"owl",
		"robot",
		"starfish",
		"werebear",
		"gnome",
		"dog with a horn"
	]

	monster_mood = [
		"happily",
		"sadly",
		"furiously",
		"indifferently",
		"delightedly",
		"sleepily"
	]

	monster_size = [
		"tiny",
		"small",
		"medium-sized",
		"large",
		"huge"
	]

	monster_action = [
		"eating some spaghetti",
		"singing a song",
		"folding laundry",
		"milling about",
		"watering plants",
		"making cheese",
		"painting a porcelain egg",
		"smashing a vase"
	]

	monster_ability = [
		"cunning",
		"dancing",
		"violence",
		"potatoes",
		"kindness"
	]

	random_monster_kind = random.choice(monster_kind)
	random_monster_mood = random.choice(monster_mood)
	random_monster_size = random.choice(monster_size)
	random_monster_action = random.choice(monster_action)
	random_monster_ability = random.choice(monster_ability)

	# build a monster
	def create_monster(self):
		print "The dungeon contains a %s %s. It is %s %s." % (
			Monster.random_monster_size,
			Monster.random_monster_kind,
			Monster.random_monster_action,
			Monster.random_monster_mood
		)

class Engine(object):
	pass

class Zone(object):
	def inheritence(self):
		print "I'm a zone!"

class Sidewalk(Zone):
	def inheritence(self):
		print "I'm a zone that is a sidewalk!"

class Restaurant(Zone):
	def inheritence(self):
		print "I'm a zone that is a restaurant!"

class Dungeon(Zone):

	def inheritence(self):
		print "I'm a zone that is a dungeon!"

	# make a Dungeon have a Monster
	def __init__(self):
		self.monster = Monster()

	def create_monster(self):
		self.monster.create_monster()

class DungeonA(Dungeon):
	def inheritence(self):
		print "I'm a zone that is a dungeon that is Dungeon A!"

class DungeonB(Dungeon):
	def inheritence(self):
		print "I'm a zone that is a dungeon that is Dungeon B!"

class DungeonC(Dungeon):
	def inheritence(self):
		print "I'm a zone that is a dungeon that is Dungeon C!"

class Escape(Zone):
	def inheritence(self):
		print "I'm a zone that is the escape!"

class Death(Zone):
	def inheritence(self):
		print "I'm a zone that is death!"

class Map(object):

	# dictionary of zones for the map
	zones = {
		'sidewalk' : Sidewalk(),
		'restaurant' : Restaurant(),
		'dungeon_a' : DungeonA(),
		'dungeon_b' : DungeonB(),
		'dungeon_c' : DungeonC(),
		'escape' : Escape(),
		'death' : Death()
	}

# test to call a Monster in a Dungeon
dungeon_a = DungeonA()
dungeon_a.create_monster()