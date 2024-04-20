countSets :: [Int] -> Int
countSets [] = 0
countSets xs =
    if odd count then 1 else 0 where
        count = countSets' xs 0 
        countSets' :: [Int] -> Int -> Int
        countSets' [] count = count
        countSets' (1 : rest) count = 
            countSets' (dropWhile (== 1) rest) (count + 1)
        countSets' (_ : rest) count = 
            countSets' rest count

main :: IO ()
main = do
    let inputList = [1, 0, 1, 1, 0, 1, 0, 1]
    putStrLn $ "Input: " ++ show inputList
    putStrLn $ "Result: " ++ show (countSets inputList)

