class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def process(log):
            id_, rest = log.split(' ', 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        logs.sort(key=process)

        return logs