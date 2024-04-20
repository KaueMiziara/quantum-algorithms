# Classical Solutions

## Haskell
This approach in functional programming defines a function with overloads to count subsets, then returns `0` if the number is even or `1` if it's odd. <br>

In the way the function is implemented, it is already able to solve similar problems for an input of size `n`.

```haskell
eightTrees :: [Int] -> Int
eightTrees [] = 0
eightTrees xs =
    if odd count then 1 else 0 where
        count = countSets xs 0 
        countSets :: [Int] -> Int -> Int
        countSets [] count = count
        countSets (1 : rest) count = 
            countSets (dropWhile (== 1) rest) (count + 1)
        countSets (_ : rest) count = 
            countSets rest count
```
