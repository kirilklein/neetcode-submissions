from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n]+=1
            else:
                counts[n]=1
        count2values = self.counts_to_values(counts)
        sorted_counts = sorted(count2values.keys(), reverse=True)
        results = []
        print(count2values)
        for c in sorted_counts:
            results = results + count2values[c]
            print(results)
            if len(results)>=k:
                return results
        return results

    @staticmethod
    def counts_to_values(counts : dict) -> Dict[int, List[int]]:
        count2values = defaultdict(list)
        for k, v in counts.items():
            if v in count2values:
                if k in count2values[v]:
                    continue
                count2values[v].append(k)
            else:
                count2values[v] = [k]
        return count2values

            
            