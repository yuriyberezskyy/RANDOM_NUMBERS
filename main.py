import random

#Integer
random_integer = random.randint(1, 10)
print(random_integer)

#Float numbers
random_float  = random.random()
print(random_float)

#Float from 0.00000 to 5.00000
print(random_float * 5)

states_of_america = ["Delaware", "Pennsylvania","New Jersey"]

states_of_america.append("New York")
states_of_america.extend(["California","Oregon"])
print(states_of_america)

