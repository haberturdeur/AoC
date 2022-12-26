part1 :: String -> Int
part1 "A X" = 1 + 3
part1 "B X" = 1 + 0
part1 "C X" = 1 + 6

part1 "A Y" = 2 + 6
part1 "B Y" = 2 + 3
part1 "C Y" = 2 + 0

part1 "A Z" = 3 + 0
part1 "B Z" = 3 + 6
part1 "C Z" = 3 + 3

part1 _ = -10000000

part2 :: String -> String
part2 "A X" = "A Z"
part2 "B X" = "B X"
part2 "C X" = "C Y"

part2 "A Y" = "A X"
part2 "B Y" = "B Y"
part2 "C Y" = "C Z"

part2 "A Z" = "A Y"
part2 "B Z" = "B Z"
part2 "C Z" = "C X"

part2 _ = ""

main :: IO ()
main = do
    a <- readFile "data.txt"
    print $ sum $ map part1 $ lines a
    print $ sum $ map (part1 . part2) $ lines a