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
    """
    Function:
        eg
    Description:
        Creates an example test case and adds it to the dictionary of test cases. Appends the key/value to the actions of the help string
    Input:
        key - key of argument
        string - value of argument as a string
        fun - callback function to use for test case
    Output:
        None
    """
    global egs
    global help
    egs[key] = fun
    help += f"  -g {key}    {string}"

def oo():
    pass

def kap(t, fun):
    u = {}
    for k, v in t.items():
        v, k = fun(k, v)
        u[k or len(u)+1] = v
    return u

def rand(low, high):
    """
    Function:
        rand
    Description:
        Creates a random number
    Input:
        low - low value
        high - high value
    Output:
        Random number
    """
    global Seed
    low, high = low or 0, high or 1
    Seed = (16807 * Seed) % 2147483647
    return low + (high - low) * Seed / 2147483647

def randFunc():
    """
    Function:
        randFunc
    Description:
        Callback function to test the rand function
    Input:
        None
    Output:
        checks if m1 equals m2 and that they round to 0.5 as a boolean
    """
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
    """
    Function:
        symFunc
    Description:
        Callback function to test SYM class
    Input:
        None
    Output:
        'a' is the median value in the array and that the div to 3 decimal points equals 1.379 as a boolean
    """
    sym = SYM()
    for i in ["a","a","a","a","b","b","c"]:
        sym.add(i)
    return "a" == sym.mid() and 1.379 == round(sym.div(), ndigits=3)

def numFunc():
    """
    Function:
        numFunc
    Description:
        Callback function to test the NUM class
    Input:
        None
    Output:
        The mean equals 11/7 and the div equals 0.787 as a boolean
    """
    num = NUM()
    for element in [1,1,1,1,2,2,3]:
        num.add(element)
    return 11/7 == num.mid() and 0.787 == round(num.div(), ndigits=3)

def crashFunc():
    num = NUM()
    return not hasattr(num, 'some.missing.nested.field')

def getCliArgs():
    """
    Function:
        getCliArgs
    Description:
        Parses out the arguments entered or returns an error if incorrect syntax is used
    Input:
        None
    Output:
        None
    """
    global args
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-d", "--dump", type=bool, default=False, required=False, help="on crash, dump stack")
    parser.add_argument("-g", "--go", type=str, default="data", required=False, help="start-up action")
    parser.add_argument("-h", "--help", action='store_true', help="show help")
    parser.add_argument("-s", "--seed", type=int, default=937162211, required=False, help="random number seed")
    parser.add_argument("-f", "--file", type=str, default="../etc/data/auto93.csv", required=False, help="name of file")
    args = parser.parse_args()

def printCLIvalues():
    """
    Function:
        printCLIvalues
    Description:
        Prints the arguments
    Input:
        None
    Output:
        None
    """
    cli_args = {}
    cli_args["dump"] = args.dump
    cli_args["go"] = args.go
    cli_args["help"] = args.help
    cli_args["seed"] = args.seed
    cli_args["file"] = args.file
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
    for k, cols in {'y': data.cols.y, 'x': data.cols.x}.items():
        print(k, "\tmid", (data.stats("mid", cols, 2)))
        print("", "\tdiv", (data.stats("div", cols, 2)))

def kap(listOfCols, fun): # t is 
    u = {}
    for k, v in enumerate(listOfCols):
        v, k = fun(v)
        u[k or len(u)+1] = v
    return u