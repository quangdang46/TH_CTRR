def formalConvertPQ(S):
    mappings = {
        "people": ("people", "is blond", "is westerner"),
        "students": ("students", "study correctly", "have high score"),
        "mammals": ("mammals", "live in the sea", "are either dolphins or whales"),
        "birds don't have wings and can swim": ("birds", "don't have wings and can swim", "are penguins"),
        "birds have wing but can't fly": ("birds", "have wings but can't fly", "")
    }
    words = S.split()
    key = " ".join(words[2:])
    if key not in mappings:
        print("Error: Invalid input string")
        return "", "", "", "Error: Invalid input string"
    D, P, Q = mappings[key]

    if Q:
        F = f"For all {D}, if they {P}, then they {Q}."
    else:
        F = f"Exist a {D} that {P}."

    return D, P, Q, F
D, P, Q, F = formalConvertPQ("Exist a person, whose hair is black but is a westerner")
print("D:", D)
print("P:", P)
print("Q:", Q)
print("Formal statement:", F)