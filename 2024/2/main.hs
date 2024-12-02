import System.IO

parseReadings :: String -> [Int]
parseReadings line = map read $ words line

diffs :: [Int] -> [Int]
diffs (x:y:xs) = (y - x) : diffs (y:xs)
diffs _ = []

isSafe :: [Int] -> Bool
isSafe readings = ascending || descending
    where
        ascending = all (\x -> x >= 1 && x <= 3) $ diffs readings
        descending = all (\x -> x<= -1 && x >= -3) $ diffs readings

possible :: [Int] -> [[Int]]
possible xs = [take i xs ++ drop (i+1) xs | i <- take (length xs) [0..]]

isSafeDampened :: [Int] -> Bool
isSafeDampened readings = ascending || descending
    where
        ascending =  any (all (\x -> x >= 1 && x <= 3) . diffs) $ possible readings
        descending = any (all (\x -> x<= -1 && x >= -3) . diffs) $ possible readings

part1 :: IO Int
part1 = do
    handle <- openFile "data.csv" ReadMode
    contents <- hGetContents handle
    return $ length $ filter isSafe $ map parseReadings $ lines contents

part2 :: IO Int
part2 = do
    handle <- openFile "data.csv" ReadMode
    contents <- hGetContents handle
    return $ length $ filter isSafeDampened $ map parseReadings $ lines contents
