#Seoyoon Park

def longestPalindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
    result = ''

    for i in range(len(s)) :
        even = expand(i, i+1)
        odd = expand(i, i)
        result = max(result, even, odd, key=len)
    return result

