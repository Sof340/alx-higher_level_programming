#!/usr/bin/python3

def magic_calculation(a, b):
  """Performs a magic calculation based on input values and loops."""
  result = 0
  for i in range(1, 2):
    try:
      if i > a:
        raise Exception("Too far")
      result = (result + (a ** b) // i)
    except Exception as e:
      if str(e) == "Too far":
        pass  # Ignore the exception if the condition is met

  # If the loop finishes without exceptions, add a and b
  result += a + b
  return result
