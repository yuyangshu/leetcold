class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def check(target, collection):
            for item in collection:
                if target != item and target in item:
                    return True
            else:
                return False

        return [item for item in words if check(item, words)]
