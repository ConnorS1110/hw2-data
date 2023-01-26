import argparse
import csv
import os
from num import NUM
from sym import SYM
from data import DATA

help = """
data.lua : an example csv reader script
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2
USAGE:   data.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -f  --file  name of file         = ../etc/data/auto93.csv
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
"""

args = None
Seed = 937162211
egs = {}
n = 0

def eg(key, string, fun):
    global egs
    global help
    egs[key] = fun
    help += f"  -g {key}    {string}"

def oo():
    pass

def rand(low, high):
    global Seed
    low, high = low or 0, high or 1
    Seed = (16807 * Seed) % 2147483647
    return low + (high - low) * Seed / 2147483647

def randFunc():
    global args
    global Seed
    num1, num2 = NUM(), NUM()
    Seed = args.seed
    for i in range(10**3):
        num1.add(rand(0, 1))
    Seed = args.seed
    for i in range(10**3):
        num2.add(rand(0, 1))
    m1, m2 = round(num1.mid(), 10), round(num2.mid(), 10)
    return m1 == m2 and 0.5 == round(m1, 1)

def symFunc():
    sym = SYM()
    for i in ["a","a","a","a","b","b","c"]:
        sym.add(i)
    return "a" == sym.mid() and 1.379 == round(sym.div(), ndigits=3)

def numFunc():
    num = NUM()
    for element in [1,1,1,1,2,2,3]:
        num.add(element)
    return 11/7 == num.mid() and 0.787 == round(num.div(), ndigits=3)

def crashFunc():
    num = NUM()
    return not hasattr(num, 'some.missing.nested.field')

def getCliArgs():
    global args
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-d", "--dump", type=bool, default=False, required=False, help="on crash, dump stack")
    parser.add_argument("-g", "--go", type=str, default="data", required=False, help="start-up action")
    parser.add_argument("-h", "--help", action='store_true', help="show help")
    parser.add_argument("-s", "--seed", type=int, default=937162211, required=False, help="random number seed")
    parser.add_argument("-f", "--file", type=str, default="../etc/data/auto93.csv", required=False, help="name of file")
    args = parser.parse_args()

def printCLIvalues():
    cli_args = {}
    cli_args["dump"] = args.dump
    cli_args["go"] = args.go
    cli_args["help"] = args.help
    cli_args["seed"] = args.seed
    print(cli_args)

def csvFunc():
    global n
    def fun(t):
        global n
        n += len(t)
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, args.file)
    readCSV(full_path, fun)
    return n == 8 * 399

def readCSV(sFilename, fun):
    n = 0
    with open(sFilename, mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            n += len(line)
            fun(line)

def dataFunc():
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, args.file)
    data = DATA(full_path)
    return (len(data.rows) == 398 and
    data.cols.y[1].w == -1 and
    data.cols.x[1].at == 1 and
    len(data.cols.x) == 4
    )

def statsFunc():
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, args.file)
    data = DATA(full_path)
    for k, cols in zip(data.cols.y, data.cols.x):
        print(data.stats(cols, 2))
