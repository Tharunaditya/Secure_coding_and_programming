"""
Look up how to use the argv module in python
Run this program as command line and use the argv module to indicate the logging level
Write your logging code to have all the levels of severity
Practice using the different levels of severity on your dog code below. be creative!

"""

import logging
class Dog:
    def __init__(self, limbs=None, eyes=None, color=None, kindness=None):
        self.limbs = limbs
        self.eyes = eyes
        self.color = color
        self.kindness = kindness  # nice, mean, angry, sad, lonely
  
        ## write some logging code in here
        logger = logging.getLogger(__name__)
        ## if limbs < 4 -- log a warning! dog needs help (it's missing legs!)
        if limbs <4:
            logger.warning("Dog legs missed, it needs help")
        if kindness in  ["sad","lonely"]:
            logger.warning("Dog feeling sad or lonely, it needs love")
        ## if kindness is sad or lonely, log a warning. If it's mean or angry it's critical! we must be careful
        elif kindness in ["mean","angry"]:
            logger.warning("Be careful! Dog is angry or mean")

if __name__ == "__main__":
    a = Dog(limbs=3, eyes=1, color="red", kindness="angry") 
    b = Dog(limbs=2, eyes=2, color="red", kindness="mean")
    c = Dog(limbs=1, eyes=1, color="red", kindness="good")
    d = Dog(limbs=4, eyes=2, color="red", kindness="happy")
    # create different dogs and see your logger in action!


