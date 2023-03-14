'''
. Finally, after many contests, the last contest given the following algorithm
and ask what the result is with n = 10, 20, 5:
Input: Integer n
Output: List O
Step0: if n<2: return [] else: proceed to step 1
Step1: Initiate O=[2]
Step2: i = 3
Step3: Flag = True
Step4: j = 0
Step5: if i%O[j]=0: Flag=False go to step 8
Step6: if j+1<length(O): j+=1;go to step 5
Step7: if Flag=True: O.append[i]
Step8: if i+2<n: i+=2; go to step 3; else: return O
Implement the algorithm to help Odyssey get back to his throne
'''
def solve(n):
	if n < 2:
		return []
	O=[2]
	i = 3
	while i < n:
		Flag = True
		j = 0
		while j < len(O):
			if i % O[j] == 0:
				Flag = False
				break
			j += 1
		if Flag:
			O.append(i)
		i += 2
	return O

print(solve(10))

