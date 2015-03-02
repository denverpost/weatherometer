def median(numbers):
   "Return the median of the list of numbers."
   # Sort the list and take the middle element.
   n = len(number)
   copy = numbers[:] # So that "numbers" keeps its original order
   copy.sort()
   if n & 1:         # There is an odd number of elements
      return copy[n // 2]
   else:
      return (copy[n // 2 - 1] + copy[n // 2]) / 2