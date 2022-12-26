import Data.List

parse :: String -> (Int, Int, Int, Int)
parse str = (fst a, snd a, fst b, snd b)
    where
        split' :: (String, String)
        split' = span (\x -> x /= ',') str
        split :: (String, String)
        split = (fst split', tail $ snd split')
        a = range $ fst $ split 
        b = range $ snd $ split
        range' x = span (\y -> y /= '-') x 
        range x = (read $ fst $ range' x,read $ tail $ snd $ range' x)

part1 :: Int -> (Int,Int, Int,Int) -> Int
part1 acc (la, ra, lb, rb)
    | la <= lb && ra >= rb = acc + 1
    | la >= lb && ra <= rb = acc + 1
    | otherwise = acc

part2 :: Int -> (Int,Int, Int,Int) -> Int
part2 acc (la, ra, lb, rb)
    | la > rb = acc
    | lb > ra = acc
    | otherwise = acc + 1

main :: IO ()
main = do
    a <- readFile "data.txt"
    print $ foldl part1 0 $ map parse $ lines a
    print $ foldl part2 0 $ map parse $ lines a