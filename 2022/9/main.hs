import Data.Set (Set)
import qualified Data.Set as Set

type Coord = (Int, Int)
type Direction = Char
type Instruction = (Direction, Int)

type Rope = (Coord, Coord)

emptyRope :: Rope
emptyRope = ((0, 0), (0, 0))

positions :: Rope -> [Instruction] -> [(Int, Int)]
positions (h, t) [] = [t]
positions rope (x : xs) = move (0, 0) x ++ positions 
  where
    move :: Rope -> Instruction -> [Rope]
    move _ (_, 0) = []
    move r@(h, t) (i, c) = r : move newRope (i, c - 1) 
        where
            distance a b = ((fst a - fst b), (snd a - snd b)) 
            newHead = movePos h i
            newTail = (0,0)
            newRope = (newHead, newTail)
            movePos :: Coord -> Direction -> Coord 
            movePos (x, y) 'U' = (x, y+1) 
            movePos (x, y) 'D' = (x, y-1) 
            movePos (x, y) 'R' = (x+1, y) 
            movePos (x, y) 'L' = (x-1, y)
            movePos _ _ = error "Wrong direction"

part1 :: [Instruction] -> Int
part1 xs = length (Set.fromList (positions emptyRope xs))

test :: IO String
test = readFile "test.txt"

prod :: IO String
prod = readFile "data.txt"

main :: IO ()
main = do
  a <- test
  let b = map ((\(x, y) -> (head x, read y)) . words) $ lines a
  print $ part1 b