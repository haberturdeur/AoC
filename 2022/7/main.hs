import Data.List
import Debug.Trace (trace)

data Tree = File String Int | Dir String [Tree] deriving (Show, Read, Eq)

debug = flip trace

sortOutput :: [String] -> [String]
sortOutput [] = []
sortOutput (x@('$' : _) : xs) = x : sortOutput xs
sortOutput xs = sort a ++ sortOutput b
  where
    (a, b) = span (\y -> not ("$" `isPrefixOf` y)) xs

buildChildren :: [String] -> ([Tree], [String])
buildChildren str
  | null str = ([], [])
  | "$" `isPrefixOf` x = ([], xs)
  | "dir" `isPrefixOf` x = buildChildren xs
  | otherwise = (File name size : children, remaining)
  where
    x = head str
    xs = tail str
    size :: Int
    size = read $ head $ words x
    name = words x !! 1
    (children, remaining) = buildChildren xs

build :: [String] -> ([Tree], [String])
build str
  | null str = ([], [])
  | x == "$ cd .." = ([], xs)
  | "$ cd " `isPrefixOf` x = (Dir dirName children : neighbors, zs)
  | "$ ls" == x = build xs
  | "dir" `isPrefixOf` x = build xs
  | otherwise = (File name size : _neighbors, _zs)
  where
    x = head str
    xs = tail str
    Just dirName = stripPrefix "$ cd " x
    (children, ys) = build xs
    (neighbors, zs) = build ys
    (_neighbors, _zs) = build xs
    size :: Int
    size = read $ head $ words x
    name = words x !! 1

buildTree :: [String] -> Tree
buildTree xs = head $ fst $ build xs

calculateSize :: Tree -> Int
calculateSize t = calculateSize' [t]
  where
    calculateSize' [] = 0
    calculateSize' ((File name size) : xs) = size + calculateSize' xs
    calculateSize' ((Dir name children) : xs) = calculateSize' children + calculateSize' xs

part1 :: Tree -> Int -> Int
part1 tree maxSize = snd $ part1' [tree] maxSize 0
  where
    part1' :: [Tree] -> Int -> Int -> (Int, Int)
    part1' [] _ acc = (0, acc)
    part1' ((File name size) : xs) _ acc = (size + nSize, nAcc)
      where
        (nSize, nAcc) = part1' xs maxSize acc

    part1' ((Dir name children) : xs) maxSize acc = (cSize, nAcc + if cSize <= maxSize then cSize else 0)
      where
        (cSize, cAcc) = part1' children maxSize acc
        (nSize, nAcc) = part1' xs maxSize cAcc

totalSize :: Int
totalSize = 70000000

neededSpace :: Int
neededSpace = 30000000

part2 :: Tree -> Int
part2 tree = minimum $ filter (\y -> y > (neededSpace - (totalSize - calculateSize tree))) (part2' tree)
  where
    part2' :: Tree-> [Int]
    part2' (File name size) = []

    part2' x@(Dir name children) = calculateSize x : concatMap part2' children

main :: IO ()
main = do
  a <- readFile "data.txt"
  let b = lines a
  let tree = buildTree b
  print $ part1 tree 100000
  print $ neededSpace - (totalSize - calculateSize tree)
  print $ part2 tree