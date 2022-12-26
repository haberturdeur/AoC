import Data.List

parseFile :: String -> [[Int]]
parseFile str = parse $ lines str
    where
        parse :: [String] -> [[Int]]
        parse [] = [[]]
        parse ("":xs) = [] : parse xs
        parse (x:xs) = ((read x): (head $ parse xs)) : (tail $ parse xs)

part1 :: [[Int]] -> Int
part1 xs = maximum $ map sum xs

part2 :: [[Int]] -> Int
part2 xs = sum $ fst $ splitAt 3 (reverse $ sort $ map sum xs)

main :: IO ()
main = do
    a <- readFile "data.txt"
    print $  part1 $ parseFile a
    print $  part2 $ parseFile a