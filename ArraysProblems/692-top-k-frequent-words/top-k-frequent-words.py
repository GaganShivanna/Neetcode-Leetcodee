class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        buckets = [[] for i in range(len(words) + 1)]
        for word, freq in count.items():
            buckets[freq].append(word)

        result = []
        for freq in range(len(buckets)-1, 0, -1):
            if buckets[freq]:
                buckets[freq].sort()
                for word in buckets[freq]:
                    result.append(word)
                    if len(result) == k:
                        return result
