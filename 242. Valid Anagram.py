def isAnagram(s, t):

    if len(s) != len(t):
        return False

    freq = [0] * 26

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1

    for count in freq:
        if count != 0:
            return False

    return True


# ---------------- Main Program ----------------

s = input("Enter first string: ")
t = input("Enter second string: ")

if isAnagram(s, t):
    print("Anagram")
else:
    print("Not Anagram")
