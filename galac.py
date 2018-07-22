import argparse
import transpile
import parser
import os
import sys
import subprocess

argp = argparse.ArgumentParser()

argp.add_argument("entrypoint", help="file to be compiled")

args = argp.parse_args()

with open(args.entrypoint) as f:
    # Create our parser
    p = parser.Parser()

    # Parse our input
    ast = p.parse(f.read())
    if hasattr(ast, 'line'):
        print('Syntax error')
        print(ast)
        sys.exit(1)

    # Print our AST
    #print(ast)

    if not os.path.exists('.gala'):
        os.mkdir('.gala')

    transpile.transpile(ast, filename=os.path.join('.gala', 'transpiled.c'))

    output_name = os.path.splitext(os.path.basename(args.entrypoint))[0]
    subprocess.call(["clang", ".gala/transpiled.c", "-o", output_name, '-lm'])
