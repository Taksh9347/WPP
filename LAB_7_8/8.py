# Decode the message:
# A message containing the letters from A-Z can be encoded into the numbers using the mapping
# A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
# and do the reverse mapping. You are required to display all the possible decoded messages.
# For example: "11106" can be decoded into:
# a. "AAJF" with the grouping (1 1 10 6)
# b. "KJF" with the grouping (11 10 6)
Msg = (input("Enter encoded message : "))
D = list(int(digit) for digit in str(Msg))

pairs = [] # store from 1 to 9
for i in range(len(D)):
    if D[i] != 0:
        pairs.append(D[i])
print(pairs)