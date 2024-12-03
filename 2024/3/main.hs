import System.IO
import Text.Parsec
import Data.Functor

data Instruction = Do | Dont | Mul !Int !Int  deriving (Show)

parser1 :: Stream s m Char => ParsecT s u m [Instruction]
parser1 = (eof $> []) <|> (do {
    ; res <- mul <|> dont <|> doIns
    ; rem <- parser1
    ; return (res : rem)
    }) <|> anyChar *> parser1
    where
        mul = try $ do {
            ; string' "mul("
            ; arg1 <- many digit
            ; string' ","
            ; arg2 <- many digit
            ; string' ")"
            ; return $ Mul (read arg1) (read arg2)
        }
        doIns = try $ string "do()" $> Do
        dont = try $ string "don't()" $> Dont

solve :: Instruction -> Int
solve (Mul a b) = a*b
solve _ = 0

process1 :: [Instruction] -> Int
process1 = foldr ((+) . solve) 0

process2 :: [Instruction] -> Int
process2 [] = 0
process2 xs = foldr ((+) . solve) 0 enabled + process2 next
    where
        (enabled, remainder) = break isDont xs
        (_, next) = break isDo remainder
        isDo Do = True
        isDo _ = False
        isDont Dont = True
        isDont _ = False

part1 :: IO ()
part1 = do
    handle <- openFile "data.txt" ReadMode
    contents <- hGetContents handle
    let res = runParser parser1 () "" contents
    case res of
        Left err -> print err
        Right result -> print $ process1 result
    return ()

part2 :: IO ()
part2 = do
    handle <- openFile "data.txt" ReadMode
    contents <- hGetContents handle
    let res = runParser parser1 () "" contents
    case res of
        Left err -> print err
        Right result -> print $ process2 result
    return ()
