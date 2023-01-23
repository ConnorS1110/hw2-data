import testfile as test
from testfile import getCliArgs, printCLIvalues

the = {}

# args = None
# Seed = 937162211

def main(the, funs):
    fails = 0
    getCliArgs()
    if (test.args.help):
        print(test.help)
    else:
        for what, fun in funs.items():
            if test.args.go == "all" or what == test.args.go:
                Seed = test.args.seed
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:",what)
                else: print("✅ pass:",what)
    printCLIvalues()
    if (fails == 0): return 0
    else: return 1


main(the, test.egs)
