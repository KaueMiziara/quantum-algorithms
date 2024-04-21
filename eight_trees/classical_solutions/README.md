# Classical Solutions

## Haskell
[Medium post explaining the solution](https://medium.com/@kauemiziara/eight-trees-problem-1-46a74c27b81a)

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
