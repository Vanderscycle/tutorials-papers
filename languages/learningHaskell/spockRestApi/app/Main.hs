{-# LANGUAGE OverloadedStrings #-}

module Main where

-- import Lib
import Web.Spock
import Web.Spock.Config

type Server a = SpockM () () () a

app :: Server ()
-- app = get root (text "hello!")
app = get root (html "<h1>hello!</h1>")

main :: IO ()
main = do
  cfg <- defaultSpockCfg () PCNoDatabase ()
  runSpock 8080 (spock cfg app)
