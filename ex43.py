"""Basic Object-Oriented Analysis and Design."""

# Gothons from Planet Percal #25

from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "This scene is not yet configured.\
 Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print "\n----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
        ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and"
        print "destroyed your entire crew. You are the last surviving member"
        print "and your last mission is to get to the neutron destruct bomb"
        print "from the Weapons Armory, put it in the bridge and blow the ship"
        print "up after getting into an escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory"
        print "when a Gothon jumps out, red scaly skin, dark grimy teeth, and"
        print "evil clown costume flowing around his hate-filled body. He's"
        print "blocking the door to the Armory and about to pull a weapon to"
        print "Blast you."
        action = raw_input("> ")

        if action == "shoot!":
            print "shoot! death."
            return 'death'
        elif action == "dodge!":
            print "dodge! death."
            return 'death'
        elif action == "tell a joke":
            print "tell a joke => laser weapon armory"
            return 'laser_weapon_armory'
        else:
            print 'DOES NOT COMPUTE! central corridor'
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print "There's a keypad lock in the box and you need the code to get"
        print "the neutron bomb out. If you ge the code wrong 10 times the"
        print "the lock closes forever and you can't get the bomb. The code is"
        print "3 digits."
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "you have the neutron bomb. run to the bridge where you must"
            print "put it in the right spot."
            return 'the_bridge'
        else:
            print "you did not get the bomb. death . . ."
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print "You enter the bridge. 5 Gothons are trying to get you."
        print "What do you do?"
        action = raw_input("> ")

        if action == "throw the bomb":
            print "the bomb blows. the Gothons shoot you. death . . ."
            return 'death'
        elif actrion == "slowly place the bomb":
            print "you slowly place the bomb and go to the escape pod"
            return 'escape_pod'
        else:
            print 'DOES NOT COMPUTE! return to the bridge.'
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print "you are desperately escaping before the ship explodes."
        print "choose one of the 5 escape pods 1 to 5."
        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "wrong pod. death . . ."
            return 'death'
        else:
            print "right pod. you won!"
            return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
