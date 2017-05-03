import math

class Queue(object):
      def __init__(self):
            self.queue = None
            if(self.queue is None):
                  self.queue = []
            else:
                  self.queue = list(queue)

      def enqueue(self, v):
            if v is None:
                  raise ValueError("Variable 'v' is None")
            if isinstance(v, float):
                  if math.isnan(v):
                        raise ValueError("Variable 'v' is NaN")
                  if math.isinf(v):
                        raise ValueError("Variable 'v' is Infinity")
            self.queue.append(v)

      def dequeue(self):
            if self.queue == []:
                  return None
            else:
                  return self.queue.pop(0)

      def len(self):
            return len(self.queue)