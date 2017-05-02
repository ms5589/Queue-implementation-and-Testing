import math

class Queue(object):
      def __init__(self):
            self.queue = None
            if(self.queue is None):
                  self.queue = []
            else:
                  self.queue = list(queue)

      def enqueue(self, v):
            # Check None
            if v is None:
                  raise ValueError("Variable 'v' is None")
                  # Check if float
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
            # return None

      def len(self):
            # return 5
            return len(self.queue)


if __name__ == '__main__':
      qq = Queue()
      # qq.enqueue(None)
      qq.enqueue(1)
      qq.enqueue(2)
      qq.enqueue(3)
      qq.enqueue(4)
      print (qq.dequeue())
      print (qq.dequeue())
      print (qq.dequeue())
      print (qq.dequeue())
      print ('length:XXX ',qq.len())
