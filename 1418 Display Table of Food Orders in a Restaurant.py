class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        def get_def_dict():
            return defaultdict(int)

        counter = defaultdict(get_def_dict)

        for order in orders:
            counter[order[1]][order[2]] += 1

        dishes = set()
        for table in counter:
            dishes |= counter[table].keys()

        header = ["Table"] + sorted(dishes)
        results = []
        for table in counter:
            results.append([table] + [str(counter[table][dish]) for dish in sorted(dishes)])

        return [header] + sorted(results, key=lambda x: int(x[0]))
