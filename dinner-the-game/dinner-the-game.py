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
	pass

class Ghost(Player):
	pass

class Monster(object):

	# randomly generate some monster qualities
	monster_kind = [
		"gingerbread golem",
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
		print "The dungeon contains a %s %s." % (
			Monster.random_monster_size,
			Monster.random_monster_kind,
		)
		print "It is %s %s." % (
			Monster.random_monster_action,
			Monster.random_monster_mood
		)

class Engine(object):
	pass

class Zone(object):
	pass

class Sidewalk(Zone):
	pass

class Restaurant(Zone):
	pass

class Dungeon(Zone):

	# make a Dungeon spawn a Monster
	def __init__(self):
		self.monster = Monster()

	def create_monster(self):
		self.monster.create_monster()

class DungeonA(Dungeon):
	pass

class DungeonB(Dungeon):
	pass

class DungeonC(Dungeon):
	pass

class Escape(Zone):
	pass

class Death(Zone):
	pass

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

# test to call a Monster in a given Dungeon
dungeon_a = DungeonA()
dungeon_a.create_monster()