#  ** Problem Statement
# Naive algorithm for Pattern Searching
# Given a text txt[0..n-1] and a pattern pat[0..m-1]
# write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
# You may assume that n > m.

def check_matched_pattern(pattern, text):
	pattern_lenght = len(pattern)
	txt_lenght = len(text)

	for i in range(txt_lenght - pattern_lenght + 1):
		j = 0

		for j in range(0, pattern_lenght):
			if(text[i + j] != pattern[j]):
				break

		if(j == pattern_lenght - 1):
			print("pattern found at: ", i)





# Driver Code 
if __name__ == '__main__': 
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    check_matched_pattern(pat, txt)