import System.IO
import Data.List
import Data.Array

distance [a, b] = abs (a - b)

parseLines :: String -> [[Int]]
parseLines str = transpose $ map read . words <$> lines str

part1 = do
    handle <- openFile "data.csv" ReadMode
    contents <- hGetContents handle
    return $ sum $ map distance $ transpose $ map sort $ parseLines contents

hist :: (Ix a, Num b) => (a,a) -> [a] -> Array a b
hist bnds is = accumArray (+) 0 bnds [(i, 1) | i<-is, inRange bnds i]

part2 = do
    handle <- openFile "data.csv" ReadMode
    contents <- hGetContents handle
    let [a, b] = parseLines contents
    let counts = hist (1, foldl max 0 a) b
    let result = sum $ map (\x -> x * (counts ! x)) a
    return result

