import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array = array * 2
print(array)

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

word = array[0, 0, 0] + array[1, 1, 0] + array[0, 1, 1] + array[1, 0, 2] + array[0, 2, 2] + array[0, 0, 0]
print(word)

# Bro code 12:55
