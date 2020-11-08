class Solution:
    def reorganizeString(self, S: str) -> str:
        import collections

        counter = collections.Counter(S)

        if counter.most_common(1)[0][1] > (len(S) + 1) // 2:
            return ""
        else:
            result, previous = [], None

            for _ in range(len(S)):
                head = counter.most_common(2)
                next = head[0][0] if head[0][0] != previous else head[1][0]

                result.append(next)
                previous = next
                counter[next] -= 1

            return "".join(result)
