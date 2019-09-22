#returns the length of the longest prefix of a string which is also the suffix
#e.g. - abcdefgabcd - 4, abcdefgh - 0, abca - 1
#ref - @vinu_sankar
def f(s):
	l = len(s)
	count = 0
	for i in range(int(l/2),l):
	    if s[i]==s[count]:
		count=count+1
	    else:
		count=0
	return count

