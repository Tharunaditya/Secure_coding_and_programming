"""
Log errors in the following function

"""
import logging

def add_em_up(*args):
    sum = 0
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    for item in args:
        try:
            sum += item
        except TypeError as e :
            # something
            print(f"TypeError occured while adding {item} : {e}")
    return sum


## Your logging should be able to report what went wrong with the follow code
print(add_em_up(1, 2, 3, 4))
print(add_em_up(1, 2, 3, "hi"))
print(add_em_up(1, 2, {3, 4}, "hi"))
print(add_em_up([1, 2, 3], [2, 3, 4], {3, 4}, "hi"))

