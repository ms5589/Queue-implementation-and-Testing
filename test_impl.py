# Author: Sagar Mehta

import hypothesis.strategies as st 
from hypothesis import given, example
import impl
import pytest
 
class TestQueue:

	vals = (st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False)| st.text() |st.integers() | st.booleans() | st.tuples(st.integers(), st.booleans()) | st.dictionaries(st.integers(), st.text(), min_size=1 ))))
	special_vals = (st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False)) | st.text() | st.integers() | st.booleans() | st.tuples(st.integers(), st.booleans())| st.dictionaries(st.integers(), st.text(), min_size=1 ), min_size=1))
	more_vals = (st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False)) | st.text() | st.integers() | st.booleans() | st.tuples(st.integers(), st.booleans())| st.dictionaries(st.integers(), st.text(), min_size=1 ), min_size=1, max_size=1))
	
	def setup_method(self):
		pass

	# OK: test multiple enqueue/dequeue ..
	@given(vals)
	def test_enqueue_multiple(self, a):
		queue = impl.Queue()
		for x in a:
			# print (x)
			queue.enqueue(x)
		for x in a:
			queue.dequeue()
		assert queue.dequeue() == None
		assert queue.len() == 0

	# OK: test when queue length is increasing by one only ..
	@given(vals)
	def test_enqueue_single_operation(self, a):
		queue = impl.Queue()
		for elem in a:
			# print (elem)
			expected_length = queue.len()+1
			queue.enqueue(elem)
			assert queue.len() == expected_length

	# OK: test when dequeue length is decreasing by one only ..
	@given(vals)
	def test_dequeue_single_operation(self, a):
		queue = impl.Queue()
		for elem in a:
			# print (elem)
			queue.enqueue(elem)
			expected_length = queue.len()-1
			queue.dequeue()
			assert queue.len() == expected_length

	# OK: test to check when queue is empty, dequeue will return None ..
	def test_dequeue_when_queue_empty(self):
		q = impl.Queue()
		result = q.dequeue()
		assert result is None

	# OK: test to check length when queue is not empty ..
	@given(vals)
	def test_len_when_not_empty(self, param):
		queue = impl.Queue()
		for elem in param:
			queue.enqueue(elem)
		# print (param)
		assert queue.len() == len(param)
	
	# OK: test to check when queue is initialized its size is 0 ..
	def test_len_when_initalize(self):
		queue = impl.Queue()
		try:
			assert queue.len() == 0
		except:
			assert False

	# OK: test to check len always returns non negative integers ..
	def test_len_returns_positive_ints(self):
		queue = impl.Queue()
		try:
			# assert (type(queue.len())==int) and (queue.len()>=0)
			assert isinstance(queue.len(), int) and (queue.len()>=0)
		except:
			assert False

	# OK: test to check when queue is not empty, dequeue doesn't return None ..
	@given(special_vals)
	def test_dequeue_when_queue_not_empty(self, param):
		queue = impl.Queue()
		for element in param:
			queue.enqueue(element)
		result = queue.dequeue()
		# print (result)
		assert result is not None

	# OK: test to check valuerror when enqueue values are None, nan, inf and -inf ..
	@given(st.floats(min_value=None, max_value=None, allow_nan=None, allow_infinity=None))
	@example(param = float('inf'))
	@example(param = float('-inf'))
	@example(param = float('nan'))
	@example(param = None)
	def test_value_error(self,param):
		queue = impl.Queue()
		try:
			# print(param)
			queue.enqueue(param)
		except ValueError:
			pass
		except:
			assert False

	# OK: test to check dequeue value is always the first element
	@given(special_vals)
	def test_dequeue_val(self,param):
		queue = impl.Queue()
		try:
			for element in param:
				queue.enqueue(param)
			result = queue.dequeue()
			# print (result[0],'==',param[0])
			assert result[0] == param[0]
		except:
			assert False

	# test to check dequeue doesn't return False
	@given(st.floats(min_value=None, max_value=None, allow_nan=None, allow_infinity=None))
	@example(param=None)
	@example(param=float('inf'))
	@example(param=float('-inf'))
	@example(param=float('nan'))
	def test_dequeue_not_return_inf_nan(self, param):
		queue = impl.Queue()
		try:
			queue.enqueue(param)
		except ValueError:
			try:
				assert queue.dequeue() == None
			except:
				assert False
		except:
			assert False, "Sorry!"

	# to test enqueue inserts correct element
	@given(more_vals)
	def test_correct_enqueue(self,param):
		queue = impl.Queue()
		try:
			for element in param:
				queue.enqueue(element)
			for element in param:
				result = queue.dequeue()
				assert result == element
			for element in param:
				queue.enqueue(element)
			queue.enqueue('random_string')
			assert queue.len() == 2
			for element in param:
				m = queue.dequeue()
				assert m == element
			new_result = queue.dequeue()
			print(new_result)
			assert queue.len() == 0
		except:
			assert False
