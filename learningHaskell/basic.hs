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
roundDouble =  round myDouble
ceilDouble = ceiling myDouble
floorDouble = floor myDouble

squareRootFive = sqrt numFive'

-- Lists 
numList = [1,2,3,4,5]
rangeList = [1..5] --same as above
alphaList = ['a'..'z']
evenNums = [2,4..20]
oddNums = [1,3..20]
weirdList = [4,9..20]
--also applies to letters
oddAlpha = ['a','e'..'z']
sumNumb = sum [1..5]
sumNbList = sum numList
productNbList = product numList

elemList = elem 5 numList -- part of the list 
elemList' = 5 `elem` numList

fibNumbers = [1,1,2,3,5,8]
moreFibs = [13,21,34,55,89,144]
combineFibs = fibNumbers ++ moreFibs

maxFib = maximum combineFibs
minFib = minimum combineFibs

twoLists = [fibNumbers,moreFibs]

myZip = zipWith (+) [1,2,3,4,5][6,7,8,9,10]
zipFibs = zipWith (+) fibNumbers moreFibs

--infinite
infOdds = [1,3..]
takeODds = take 20 infOdds --first 20
infFives = repeat 5
takeFives = take 20 infFives
replFives = replicate 20 5 -- same as above
cycleFibs = cycle combineFibs
takeCycle = take 50 (cycle [1,2,3,4,5,6,7,8,9,10])
takeCycle' = take 50 $ cycle [1,2,3,4,5,6,7,8,9,10]

dropFibs = drop 5 combineFibs
filterFibs = filter (>5) combineFibs
whileFibs = takeWhile(<=88) combineFibs

mapList = map (*2) [1..10] -- takethis and do the following to everymember of the list

unordList = [545,2,34,87,3,897,56,13]
sortList = sort unordList
{-
usefull commands:
head combineFibs  -- the first item
tails combineFibs -- everything except the first entry
init combineFibs -- shows the list
-}

addList = foldr (+) 1 [2..5] -- the number one will be applied to the right number first (5+1)
multiList = foldr (*) 1 [2..5]
-- foldr takes function (f) applies expression (e) to a list
-- 2*(3*(4*(5*1)))
minusList = foldr (-) 15 [2..5]
-- (((((1)-5)-4)-3)-2)
sumFold = foldl (+) 0 [1..100] -- sum [1..100]
