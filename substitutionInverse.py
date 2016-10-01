sub = "THEQUICKSLVRFOXJMPDAZYBWNG"

# Convert letters A, ..., Z to indices 0, ..., 25.
# Also handle a, ..., z, just because we can.
def indexFromLetter(char):
	if "A" <= char <= "Z":
		return ord(char) - ord("A")
	elif "a" <= char <= "z":
		return ord(char) - ord("a")
	else:
		return None

# Convert indices back to upper-case letters.
def letterFromIndex(index):
	if index < 0 or index > 25:
		return None
	else:
		return chr(index + ord("A"))

l = [""]*26
for i in range(len(sub)):
    print(indexFromLetter(sub[i]))
    l[indexFromLetter(sub[i])]=letterFromIndex(i)
print("".join(l))
