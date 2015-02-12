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

class Player(object):
	def inheritence(self):
		print "I'm a player!"

class Ghost(Player):
	def inheritence(self):
		print "I'm a player who is a ghost!"

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
	pass

class Monster(object):
	pass

# inheritence test

player = Player()
ghost = Ghost()
zone = Zone()
sidewalk = Sidewalk()
restaurant = Restaurant()
dungeon = Dungeon()
dungeon_a = DungeonA()
dungeon_b = DungeonB()
dungeon_c = DungeonC()
escape = Escape()
death = Death()

player.inheritence()
ghost.inheritence()
zone.inheritence()
sidewalk.inheritence()
restaurant.inheritence()
dungeon.inheritence()
dungeon_a.inheritence()
dungeon_b.inheritence()
dungeon_c.inheritence()
escape.inheritence()
death.inheritence()