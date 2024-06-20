# Make Change Function

This function solves the "make change" problem by calculating the minimum number of coins needed to make a given total amount.

## Function Signature

```python
def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make the total amount.

    :param coins: List of coin denominations
    :param total: Total amount to make
    :return: Minimum number of coins needed
    """
```

# Parameters
 - coins (list): A list of coin denominations. Each coin denomination should be a positive integer.
 - total (int): The total amount to make using the given coins. The total should be a non-negative integer.

# Return Value
The function returns an integer representing the minimum number of coins needed to make the total amount. If it is not possible to make the total amount using the given coins, the function returns 0.

# Example Usage
```python
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output: 3
```
In the example above, the function is called with coins as [1, 2, 5] and total as 11. The minimum number of coins needed to make 11 is 3 (using 3 coins with denominations 5, 5, and 1).
