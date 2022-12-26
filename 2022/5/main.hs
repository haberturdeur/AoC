import Data.List
import qualified Control.Arrow as Data.Bifunctor

parseStackLine :: String -> [Maybe Char]
parseStackLine "" = []
parseStackLine (' ':' ':' ':' ':xs) = Nothing : parseStackLine xs
parseStackLine ('[':l:']':' ':xs) = Just l : parseStackLine xs
parseStackLine [' ', ' ', ' '] = [Nothing]
parseStackLine ['[', l, ']'] = [Just l]
parseStackLine _ =  error "Impossible: internal error, passed wrong string."

addLine :: [Maybe Char] -> [[Char]] -> [[Char]]
addLine [] [] = []
addLine [] (y:ys) = [] : addLine [] ys
addLine (Just x : xs) [] = [x] : addLine xs []
addLine (Nothing : xs)  [] = [] : addLine xs []
addLine (Just x : xs) (y:ys) = (x : y) : addLine xs ys
addLine (Nothing : xs) (y:ys) = y : addLine xs ys

transposeLines :: [[Maybe Char]] -> [[Char]]
transposeLines = foldr addLine []

parseStacks :: [String] -> [[Char]]
parseStacks stacks = map reverse $ transposeLines $ map parseStackLine (tail $ reverse stacks)

moveBlock :: [[Char]] -> (Int, Int, Int) -> [[Char]]
moveBlock stacks (count, src,dst) = addBlocks (removeBlocks stacks count src) dst
    where
        addBlocks :: ([Char], [[Char]]) -> Int -> [[Char]]
        addBlocks (blocks, x:stacks)  0 = (blocks++x):stacks
        addBlocks (blocks, x:stacks)  dst = x:addBlocks (blocks, stacks) (dst-1)
        addBlocks _ _ = error "Impossible: internal error, passed wrong string."

        removeBlocks :: [[Char]] -> Int -> Int -> ([Char], [[Char]])
        removeBlocks (x:stacks) count 0 = (take count x, (reverse . take (length x - count) . reverse) x:stacks)
        removeBlocks (x:stacks) count src = Data.Bifunctor.second (x :) (removeBlocks stacks count (src - 1))
        removeBlocks _ _ _ = error "Impossible: internal error, passed wrong string."

parseInstruction1 :: [String] -> [(Int, Int, Int)]
parseInstruction1 ["move", count, "from", src, "to", dst] = replicate (read count) (1, read src- 1, read dst- 1)
parseInstruction1 _ = error "Impossible: internal error, passed wrong instruction string."

parseInstructions1 :: [String] -> [(Int, Int, Int)]
parseInstructions1 = concatMap (parseInstruction1 . words)

parseInstruction2 :: [String] -> [(Int, Int, Int)]
parseInstruction2 ["move", count, "from", src, "to", dst] = [(read count, read src- 1, read dst- 1)]
parseInstruction2 _ = error "Impossible: internal error, passed wrong instruction string."

parseInstructions2 :: [String] -> [(Int, Int, Int)]
parseInstructions2 = concatMap (parseInstruction2 . words)

moveBlocks :: [[Char]] -> [(Int, Int, Int)] -> [[Char]]
moveBlocks = foldl moveBlock

main :: IO ()
main = do
    a <- readFile "data.txt"
    let b = span (/= "") $ lines a
    let stacks = fst b
    let instructions = tail $ snd b
    print stacks
    print $ parseStacks stacks
    print $ map head $ moveBlocks (parseStacks stacks) $  parseInstructions1 instructions
    print $ map head $ moveBlocks (parseStacks stacks) $  parseInstructions2 instructions