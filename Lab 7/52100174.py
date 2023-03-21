
def thieves(day):
    if day == 1:
        return 1
    else:
        return day + thieves(day-1)
    
def days(thieves):
    day = 1
    while thieves(day) <= thieves:
        day += 1
    return day


def riches(xn, previous_richest):
	if xn > previous_richest:
		return xn
	else:
		return previous_richest

def richest(x):
	if len(x) == 1:
		return x[0]
	else:
		return riches(x[0], richest(x[1:]))
    


men = [10, 5, 15, 20, 7]


def waytochoose(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return waytochoose(n-1, k) + waytochoose(n-1, k-1)

def closest(n, k):
    if waytochoose(n, k) == 1000:
        return k
    elif waytochoose(n, k) > 1000:
        return closest(n, k-1)
    else:
        return closest(n, k+1)



def waytochooseP(n,k):
	if k == 0 or k == n:
		return 1
	else:
		return waytochooseP(n-1, k-1)*n
        

def closestP(n, k):
	if waytochooseP(n, k) == 10000:
		return k
	elif waytochooseP(n, k) > 10000:
		return closestP(n, k-1)
	else:
		return closestP(n, k+1)



def total_characters(story_num):
    if story_num == 1:
        return 1
    else:
        return (2 ** (story_num - 1)) + total_characters(story_num - 1)

def total_stories(characters):

	if total_characters(1) > characters:
		return 0
	else:
		return 1 + total_stories(characters - total_characters(1))

def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	

def towerOfHanoi(n, A, B, C):
    if n == 1:
        C.append(A.pop())
    else:
        towerOfHanoi(n - 1, A, C, B)
        C.append(A.pop())
        towerOfHanoi(n - 1, B, A, C)




A = [['A'], [1, 2, 3]]
B = [['B'], []]
C = [['C'], []]

towerOfHanoi(3, A[1], B[1], C[1])

print(C)


