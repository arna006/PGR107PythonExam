
import random

class Bug:
    def __init__(self, position):
        self.position = position
        self.direction = "left"

    def move(self):
        self.position += 1

    """
        Makes it more fun if the bug has a "brain" of its own we decided to go with a random.choice method that decides whether 
        the ladybug goes 'left' or 'right'.
    """

    def turnDirection(self):
        turn_to_a_side = random.choice([True, False])

        if turn_to_a_side:
            if self.direction == "left":  # if it turns left it increments the total moves by 1
                self.position += 1
            else:
                self.position = -1  # if it turns right it decrements the total moves by 1

    def bugPosition(self):
        return self.position

ladybug = Bug(10)
print("Start position: ", ladybug.bugPosition())

ladybug.move()
print("The Ladybugs position is now: ", ladybug.bugPosition())

ladybug.turnDirection()
print("The Ladybugs position is now: ", ladybug.bugPosition())

ladybug.turnDirection()
ladybug.move()
print("The Ladybugs position is now: ", ladybug.bugPosition())
