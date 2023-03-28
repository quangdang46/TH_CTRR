Andersen = {"The Emperor's New Clothes", "The Little Mermaid", "The Little Match Girl", "The Snow Queen"}

Shakespeare = {"Romeo and Juliet", "Hamlet", "King Lear", "Macbeth", "A Midsummer Night’s Dream", "A Comedy of Errors"}

Tragedy = {"Medea", "Octavia", "Oedipus", "Ur-Hamlet", "Romeo and Juliet", "Hamlet", "King Lear", "Macbeth"}
Comedy = {"A Midsummer Night's Dream", "A Comedy of Errors", "The Three Musketeer", "The Clouds"}
Uncategory = {"Don Quixote", "Rapunzel", "Cinderella", "The Emperor's New Clothes", "The Little Mermaid", "The Little Match Girl", "The Snow Queen"}

Shakespeare_Tragedy = Shakespeare - Tragedy

# 5
Andersen_Comedy = Andersen.intersection(Comedy)
print(Andersen_Comedy)
# 6
print(Andersen_Comedy.issubset(Andersen))
print(Andersen_Comedy.isdisjoint(Comedy))

print(Shakespeare_Tragedy.issuperset(Comedy))
print(Shakespeare_Tragedy.isdisjoint(Tragedy))

# 7
Work = Andersen.union(Shakespeare, Tragedy, Comedy, Uncategory)

# 8
Author = {'Shakespeare', 'Andersen', 'Unknown'}

# 9
Author_Of = {'Hamlet': 'Shakespeare', 'Romeo and Juliet': 'Shakespeare', 'Macbeth': 'Shakespeare',
             'King Lear': 'Shakespeare', 'A Midsummer Night’s Dream': 'Shakespeare', 'A Comedy of Errors': 'Shakespeare',
             'The Emperor’s New Clothes': 'Andersen', 'The Little Mermaid': 'Andersen', 'The Little Match Girl': 'Andersen',
             'The Snow Queen': 'Andersen', 'Medea': 'Unknown', 'Octavia': 'Unknown', 'Oedipus': 'Unknown',
             'Ur-Hamlet': 'Unknown', 'The Three Musketeer': 'Unknown', 'The Clouds': 'Unknown',
             'Don Quixote': 'Unknown', 'Rapunzel': 'Unknown', 'Cinderella': 'Unknown'}

# 10
Written_By = {}
for work, author in Author_Of.items():
    if author in Written_By:
        Written_By[author].add(work)
    else:
        Written_By[author] = {work}


# 11
Work_Count = {}
for work in Author_Of.values():
    if work in Work_Count:
        Work_Count[work] += 1
    else:
        Work_Count[work] = 1

# 12
def num_of_works(content):
    return len(content.split())

# 13
import string

def count_words(content):
    words = content.split()
    words = [word.strip(string.punctuation) for word in words]
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
