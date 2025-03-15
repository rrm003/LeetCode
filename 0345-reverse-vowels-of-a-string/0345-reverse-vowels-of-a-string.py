class Solution:
	def isVowel(self, char: str) -> bool:
		vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
		if char in vowels: return True
		return False

	def reverseVowels(self, s: str) -> str:
		start = 0 
		end = len(s)-1

		s_list = list(s)
		#print(s_list)
		while start < end :
			l = self.isVowel(s_list[start])
			r = self.isVowel(s_list[end])
			#print(s[start], l , s[end], r)
			if l and r: 
				s_list[start], s_list[end] = s_list[end], s_list[start]
				start+=1
				end -= 1
			elif not r: end -= 1
			elif not l: start += 1
	 	
		#print(s_list)
		rslt = "".join(s_list)
		return rslt