# Classical Solutions

## Haskell
This approach in functional programming defines a function with overloads to count subsets, then returns `0` if the number is even or `1` if it's odd. <br>

In the way the function is implemented, it is already able to solve similar problems for an input of size `n`.

```haskell
countSubsets :: [Int] -> Int
countSubsets [] = 0
countSubsets xs =
    if odd count then 1 else 0 where
        count = countSubsets' xs 0 
        countSubsets' :: [Int] -> Int -> Int
        countSubsets' [] count = count
        countSubsets' (1 : rest) count = 
            countSubsets' (dropWhile (== 1) rest) (count + 1)
        countSubsets' (_ : rest) count = 
            countSubsets' rest count
```
