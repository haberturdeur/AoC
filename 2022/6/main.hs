import Data.List
import Debug.Trace (trace)

debug = flip trace

checkUnique :: Int -> Int -> String -> Int
checkUnique count counter xs
  | length xs < count = error "match not found" `debug` xs
  | count == length (group $ sort $ take count xs) = counter
  | otherwise = checkUnique count (counter + 1) (tail xs)

main :: IO ()
main = do
  a <- readFile "data.txt"
  let b = lines a
  print $ map (checkUnique 4 4) b -- part 1
  print $ map (checkUnique 14 14) b -- part 2
