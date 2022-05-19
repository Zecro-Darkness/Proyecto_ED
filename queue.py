class Node(object):
  def __init__(self, item = None):
    self.item = item
    self.next = None
    self.previous = None


class Queue(object):
  def __init__(self):
    """post: creates an empty FIFO queue"""
    self.length = 0
    self.head = None
    self.tail = None

  def enqueue(self, x):
    """post: adds x at back of queue"""
    newNode = Node(x)
    newNode.next = None
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      newNode.previous = self.tail
      self.tail = newNode

  def dequeue (self):
    """pre: self.size() > 0
        post: removes and returns the front item"""
    item = self.head.item
    self.head = self.head.next 
    self.length = self.length - 1
    if self.length == 0:
      self.last = None
    return item

  def front(self):
    """pre: self.size() > 0
        post: returns first item in queue"""
    return item[0]

  def size(self):
    """post: returns the number of itemes in queue"""