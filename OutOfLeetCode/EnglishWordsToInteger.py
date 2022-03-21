
# https://www.1point3acres.com/bbs/thread-870598-1-1.html

# https://leetcode.com/discuss/interview-question/633508/amazon-onsite-english-words-to-integer

# Meta Phone

s= word.split()

smallNums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
	"eleventh":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17,
	"eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, 
	"seventy":70, "eighty":80, "ninety":90}

bigNums = {"thousand":1000, "million":1000000, "billion":1000000000}

tempNum = 0
finalNum =0
print(s)
for i in s:
	print(finalNum)
	if i in smallNums:
		tempNum += smallNums[i]
	elif i == "hundred":
		tempNum *= 100
	elif i in bigNums:
		tempNum *= bigNums[i]
		finalNum += tempNum
		tempNum = 0

finalNum+=tempNum
print(finalNum)
