# class intSet(object):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""
#
#     def __init__(self):
#         """Create an empty set of integers"""
#         self.vals = []
#
#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self"""
#         if not e in self.vals:
#             self.vals.append(e)
#
#     def member(self, e):
#         """Assumes e is an integer
#            Returns True if e is in self, and False otherwise"""
#         return e in self.vals
#
#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#            Raises ValueError if e is not in self"""
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')
#
#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'
#
#     def intersect(self, other):
#         newSet = intSet()
#         for element in self.vals:
#             if element in other.vals:
#                 newSet.insert(element)
#         return newSet
#
#     def len(self):
#         i = 0;
#         for element in self.vals:
#             i += 1
#         return i
#
#
# setA = intSet()
# setA = {-13,-12,-10,-7,0,2,6,12,17,18}
#
#
# print(len(setA))


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
