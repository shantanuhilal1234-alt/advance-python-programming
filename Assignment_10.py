import numpy as np

arr = np.arange(1, 11)

print("Original Array:")
print(arr)


print("\nFirst five elements:")
print(arr[:5])

print("\nElements from index 2 to 6:")
print(arr[2:7])

print("\nLast three elements:")
print(arr[-3:])

print("\nAlternate elements:")
print(arr[::2])


print("\nStatistical Measures:")
print("Sum     :", np.sum(arr))
print("Mean    :", np.mean(arr))
print("Maximum :", np.max(arr))
print("Minimum :", np.min(arr))

arr = arr + 5

print("\nArray after adding 5 using broadcasting:")
print(arr)

arr = arr * 2

print("\nArray after multiplying by 2 using broadcasting:")
print(arr)
