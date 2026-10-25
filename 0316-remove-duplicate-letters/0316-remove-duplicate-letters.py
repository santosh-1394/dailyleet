
class Solution(object):
    def removeDuplicateLetters(self, s):
        last_seen = {ch: i for i, ch in enumerate(s)}
        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and ch < stack[-1] and last_seen[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)
