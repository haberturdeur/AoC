import Data.Char (digitToInt)
import Data.List (transpose)
import Data.Matrix (fromLists, mapPos, toLists, Matrix, getRow, getCol)
import Data.Vector (toList)
import Debug.Trace (trace)
import Data.List (findIndex)
import Data.Text (Text)
import qualified Data.Text as T (lines, unpack, pack)
import Data.List (tails)

import Control.Monad ((<=<), when)
import Data.Maybe (mapMaybe)
import Data.Text (Text)
import qualified Data.Text.IO as TIO (putStrLn, readFile)
import System.Environment (getArgs)
import Text.Read (readMaybe)


debug = flip trace

type Tree = (Int, Bool)
type TreeHouse = (Int, (Int, Int, Int, Int))

type Grid = [[Int]]

visible :: Grid -> Int
visible m = sum $ map sum (visibleMask m)

visibleMask :: Grid -> Grid
visibleMask m = map (map (\(_, v) -> if v then 1 else 0)) visibleMask'
  where
    visibleMask' :: [[Tree]]
    visibleMask' = cast 3 (map (map (\x -> (x, False))) m)
    cast :: Int -> [[Tree]] -> [[Tree]]
    cast (-1) t = t
    cast d t = trans $ rev $ map (line (-1)) (rev $ trans $ next t)
      where
        next c = cast (d -1) c
        trans b = if even d then transpose b else b
        rev a = if d < 2 then a else map reverse a

    line :: Int -> [Tree] -> [Tree]
    line height [] = []
    line height (x@(9, _) : xs) = (9, True) : xs
    line height (x@(h, v) : xs) = (h, v || h > height) : line (max h height) xs

score :: Matrix Int -> (Int, Int) -> Int -> Int
score m c@(x, y) height = product scores -- `debug` (show c ++ " " ++ show height ++ " " ++ show (product scores) ++ " " ++ show scores)
    where
        row = getRow y m
        column = getCol x m
        (ha, hb) = splitAt (x-1) $ toList row
        (va, vb) = splitAt (y-1) $ toList column
        directions = [reverse ha, if null hb then [] else  tail hb, reverse va, if null vb then [] else tail vb]
        scores = map (scoreLine height) directions
        scoreLine :: Int -> [Int] -> Int
        scoreLine h xs = maybe (length xs) succ $ findIndex (>= h) xs

scoreGrid :: Grid -> Grid
scoreGrid m = toLists $ mapPos (score $ fromLists m) $ fromLists m

part1 :: Grid -> Int
part1 = visible

part2 :: Grid -> Int -- doesn't work
part2 m = maximum $ map maximum $ scoreGrid m -- `debug` show (fromLists $ scoreGrid m)

test :: IO String
test = readFile "test.txt"

prod :: IO String
prod = readFile "data.txt"

main :: IO ()
main = do
  a <- prod
  let b = map (map digitToInt) (lines a)
  let m = b
  print $ part1 m