

def negation(statement):
  D, P, Q = statement.split(',')
  return f"There exists {D} such that {P} and not {Q}."

def contrapositive(statement):
  D, P, Q = statement.split(',')
  return f"For all {D}, if not {Q}, then not {P}."

def converse(statement):
  D, P, Q = statement.split(',')
  return f"For all {D}, if {Q}, then {P}."

def inverse(statement):
  D, P, Q = statement.split(',')
  return f"For all {D}, if not {P}, then not {Q}."

print(inverse("fish, they need water, they swim"))
print(contrapositive("fish, they need water, they swim"))
print(negation("fish, they need water, they swim"))
print(converse("fish, they need water, they swim"))
