from employee import Manager

manager = Manager(
    "E101",
    "Abhirag Verma", 
    "Free Use",
    5000,
    1000
)

boss = Manager(
    "E100",
    "Ananya Rastogi",
    "CEO",
    20000000000,
    100000000
)

print(boss.display_details())
print(manager.display_details())