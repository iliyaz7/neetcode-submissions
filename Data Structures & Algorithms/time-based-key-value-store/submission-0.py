class TimeMap:

    def __init__(self):
        self.store = {}  # key -> list of [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        result = ""
        for ts, val in self.store[key]:
            if ts <= timestamp:
                result = val
            else:
                break  # timestamps are increasing, so no point checking further

        return result


# ---- sample run ----
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))   # "bar"
print(timeMap.get("foo", 3))   # "bar"

timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))   # "bar2"
print(timeMap.get("foo", 5))   # "bar2"