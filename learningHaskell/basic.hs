-- This is a single line comment

{-
This is a multi-line comment
-}

-- haskell being a lazy loading language means that an eronous function can be writte yest won't be evaluated (hence not crash)

import Data.List
-- string list of char 
-- Bool, Int, Integer, Float, Double, "char", [Char], Tuples
-- List have to be of the same type while tuples can have any types

-- :: Bool
-- True or False
trueAndFalse = True && False
trueOrFalse = True || False
notFalse = not(False)

-- :: Int
-- WholeNumber -2^63 - 2^63
maxInt = maxBound :: Int

-- :: Integer
-- Unbounded Whole Number
numFive :: Integer -- Haskell compiler infers the type automatically (just use the verbose TS way)
numFive = 5
numFive' = 5.0 :: Float -- single quote at the end being the same var
boolFive = 5 > 4

-- :: Float 
myFloat :: Float -- if not infered already it will be a double
myFloat = 1.0 + 2.5

-- ::Double

myDouble = 1.5555555555 + 0.0000000001

-- ::char
-- Char are single characters and denoted within single quotes

singleChar = 'a'
myName = "Henri" -- :: String
myName' = ['H','e','n','r','i'] -- :: [Char] 

-- Math

addNum = 3 + 6
subNum = 3 - 6
multNum = 3 * 6
divNum = 3 / 6 -- Division is not integer division by default
modNum = mod 9 2 -- integer division (prefix operator)
modNum' = 9 `mod` 2 -- infix (operator)
addNeg = 4 + (-5) --negative numbers have to be in parenthesis

-- pi, exp, log, cos, tan, asin ..

truncDouble = truncate myDouble
