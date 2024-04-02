import argparse

p = argparse.ArgumentParser()
p.add_argument("args", nargs="+")
args = p.parse_args()

print("your args: " + " ".join(args.args))