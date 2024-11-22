"""
Write a function that accepps the following arguments
INPUT:
    name: str
    job : str
    * args: adjectives (str) that describe things (i.e "happy", " sad")
    **args: possessions (str): value (int / float)
Output:
   Form a  nice string that explains everything relevant



example input:
   ('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20)
output:
   "Gilad is a teacher who is happy, amazing, and sooooo cool. Gilad has a bike worth 2000, a house worth 1000, and shoes with 20"


The string should accomadate any number of *args and **kwargs.
"""


def describer(name,job,*adj, **posses):
    if adj:
       adj_str = ','.join(adj[:-1])
       if len(adj) >1:
          adj_str += f", and {adj[-1]}"
    else:
       adj_str = ""
    posses_str_list = []
    for item, value in posses.items():
       posses_str_list.append(f"a {item} worth {value}")
    if posses_str_list: 
       posses_str_list= ",".join(posses_str_list[:-1])+f" and {posses_str_list[-1][2::]}"
    else: 
       posses_str_list = ""
    return f"{name} is a {job} who is {adj_str}. {name} has {posses_str_list}"
message=describer('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20)
print(message)