# Python3 program to find
# a missing number in a
# string of consecutive
# numbers without any
# separator.
import math

MAX_DIGITS = 6


# gets the integer at position
# i with length m, returns it
# or -1, if none
def getValue(Str, i, m):
    if (i + m > len(Str)):
        return -1

    # Find value at index
    # i and length m.
    value = 0

    for j in range(m):
        c = (ord(Str[i + j]) -
             ord('0'))
        if (c < 0 or c > 9):
            return -1
        value = value * 10 + c
    return value


# Returns value of missing
# number
def findMissingNumber(Str):
    # Try all lengths for
    # first number
    for m in range(1, MAX_DIGITS + 1):

        # Get value of first
        # number with current
        # length
        n = getValue(Str, 0, m)
        if (n == -1):
            break

        # To store missing number
        # of current length
        missingNo = -1

        # To indicate whether
        # the sequence failed
        # anywhere for current
        # length.
        fail = False

        # Find subsequent numbers
        # with previous number as n
        i = m
        while (i != len(Str)):

            # If we haven't yet found
            # the missing number for
            # current length. Next
            # number is n+2. Note
            # that we use Log10 as
            # (n+2) may have more
            # length than n.
            if ((missingNo == -1) and
                    (getValue(Str, i, 1 +
                                      int(math.log10(n + 2))) ==
                     n + 2)):
                missingNo = n + 1
                n += 2

            # If next value is (n+1)
            elif ((getValue(Str, i, 1 +
                                    int(math.log10(n + 1))) ==
                   n + 1)):
                n += 1
            else:
                fail = True
                break
            i += 1 + int(math.log10(n))

        if (not fail):
            return missingNo

    # not found or no
    # missing number
    return -1


# Driver code
print(findMissingNumber("9101112141516"))

# This code is contributed by avanitrachhadiya2155