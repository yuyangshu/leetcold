class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        from collections import defaultdict
        
        def update(prev, current):
            if prev:
                pending[prev] -= 1
            if current:
                pending[current] += 1
            
            return False if prev and pending[prev] < 0 else True

        counter, memory = 0, 0
        pending = defaultdict(int)

        for c in croakOfFrogs:
            if c == 'c':
                counter += 1
                is_valid = update('', 'r')
            elif c =='r':
                is_valid = update('r', 'o')
            elif c == 'o':
                is_valid = update('o', 'a')
            elif c == 'a':
                is_valid = update('a', 'k')
            elif c == 'k':
                counter -= 1
                is_valid = update('k', '')

            if not is_valid:
                return -1
            if counter > memory:
                memory = counter

        return memory if set(pending.values()) == {0} else -1
