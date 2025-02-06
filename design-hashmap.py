# Implemented using LinkedList
class ListNode:
  def __init__(self, key = -1, val = -1, next = None):
    self.key = key
    self.val = val
    self.next = next

class MyHashMap:

  def __init__(self):
    self.map = [ListNode() for _ in range(1000)]

  def hash(self, key: int) -> int:
    return key % len(self.map)

  def put(self, key: int, value: int) -> None:
    cur = self.map[self.hash(key)]
    while cur.next:
      if cur.next.key == key:
        cur.next.val = value
        return
      cur = cur.next
    cur.next = ListNode(key, value)

  def get(self, key: int) -> int:
    cur = self.map[self.hash(key)].next # Don't need the dummy node as it is not used or checked
    while cur:
      if cur.key == key:
        return cur.val
      cur = cur.next
    return -1

  def remove(self, key: int) -> None:
    cur = self.map[self.hash(key)]
    while cur and cur.next:
      if cur.next.key == key:
        cur.next = cur.next.next
        return
      cur = cur.next


obj = MyHashMap()
obj.put(1,5)
obj.put(2,10)
print(obj.get(1))
obj.remove(2)
print(obj.get(2))