import random

friends = ["Alice", "James", "Robin", "Angela"]
print(random.choice(friends))

# nested list
school_friends = ["Ron", "Rey", "Ryley"]
college_friends = ["Jim", "Harry", "Simon", "Jinny"]

all_friends = [school_friends, college_friends]
print(all_friends[0][1])