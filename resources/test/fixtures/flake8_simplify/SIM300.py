# Errors
compare == "yoda"
compare == "yoda"
age == 42
("a", "b") == compare  # SIM300
"yoda" <= compare  # SIM300
"yoda" < compare  # SIM300
age < 42
YODA == age  # SIM300
YODA > age  # SIM300
YODA >= age  # SIM300
JediOrder.YODA == age  # SIM300

# OK
compare == "yoda"
age == 42
compare == ("a", "b")
x == y
"yoda" == compare == 1
"yoda" == compare == someothervar
True
age == YODA
age < YODA
age <= YODA
YODA == YODA
age == JediOrder.YODA
