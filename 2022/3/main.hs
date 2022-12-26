import Data.List
import Data.Char

priority :: Char -> Int
priority c
    | ord c < ord 'a' = 27 + (ord c - ord 'A')
    | otherwise = 1 + (ord c - ord 'a')


combine :: [Int] -> [Int] -> [Int]
combine [] _ = []
combine _ [] = []
combine a@(ax : al) b@(bx : bl)
    | ax == bx = ax : combine al bl
    | ax < bx = combine al b
    | otherwise = combine a bl


part1 :: String -> Int
part1 str = sum $ combine a b
    where
        half str = length str `div` 2
        prioritized = map priority str
        a = map head . group . sort $ fst $ splitAt (half str) prioritized
        b = map head . group . sort $ snd $ splitAt (half str) prioritized

part2 :: String -> Int
part2 str = head $ part2' $ (group . sort) $ map priority str
    where part2' xs = [a | a:b:c:[] <- xs] 

split :: [String] -> [String]
split [] = []
split (a:b:c:xs) = (a++b++c) : split xs


main :: IO ()
main = do
    a <- readFile "data.txt"
    print $ sum $ map part1 $ lines a
    print $ sum $ map part2 $ split $ map ((map head) . group . sort) $ lines a