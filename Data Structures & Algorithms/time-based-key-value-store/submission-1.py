class TimeMap:

    def __init__(self):
      self.dict1={}

    def set(self, key: str, value: str, timestamp: int) -> None:
      if key not in self.dict1:
        self.dict1[key]=[[value,timestamp]]
      else:
        self.dict1[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict1:
          return ""
        arr=self.dict1[key]
        left=0
        right=len(arr)-1
        ans=""
        while left<=right:
          mid=left+(right-left)//2
          if arr[mid][1]<=timestamp:
            ans=arr[mid][0]
            left= mid+1
          elif arr[mid][1]>timestamp:
            right=mid-1
        return ans
     
tm=TimeMap()
tm.set("Terror","Madara",2)