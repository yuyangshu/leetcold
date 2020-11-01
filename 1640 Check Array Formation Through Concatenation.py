class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            try:
                start = arr.index(piece[0])
            except:
                return False

            if arr[start: start + len(piece)] == piece:
                arr = arr[:start] + arr[start + len(piece):]
            else:
                return False

        return True
