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

main :: IO ()
main = do
    let inputList = [1, 0, 1, 1, 0, 1, 0, 1]
    putStrLn $ "Input: " ++ show inputList
    putStrLn $ "Result: " ++ show (countSubsets inputList)

