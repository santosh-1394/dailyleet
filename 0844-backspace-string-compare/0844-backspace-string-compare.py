
class Solution(object):
    def backspaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1

        def next_valid(string, index):
            backspaces = 0

            while index >= 0:
                if string[index] == '#':
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    return index

                index -= 1

            return -1

        while i >= 0 or j >= 0:
            i = next_valid(s, i)
            j = next_valid(t, j)

            if i < 0 or j < 0:
                return i == j

            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True
