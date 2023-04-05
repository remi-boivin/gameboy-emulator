#/usr/bin/env python3
import argparse
import os

def installPythonHooks():
    print("Installing python hooks...")
    print("Done")

def installCppHooks():
    print("Installing C++ hooks...")
    with open('.git/hooks/pre-commit', 'w') as file:
        file.write("#!/bin/sh\n\nexec < /dev/tty\n\necho \"Running pre-commit hook\"\n\ncmake -B build -G \"Unix Makefiles\" && cd build/ && make && ctest --output-on-failure --rerun-failed\n\n");
    print("Done")

def main():
    print("Installing hooks...")
    parser = argparse.ArgumentParser(
                    prog = 'SetupTools',
                    description = 'Setup tools for the project',
                    epilog = 'Text at the bottom of help')
    parser.add_argument('-l', '--lang', help='Langage used to the project', required=True)
    args = parser.parse_args()

    os.system('git clone git@github.com:remi-boivin/hooks.git')
    os.system('rm -rf .git/hooks')
    os.system('mv hooks .git/')

    if args.lang == "python":
        installPythonHooks()
    elif args.lang == "c++":
        installCppHooks()
    else:
        print("Langage not supported")
        exit(1)

if __name__ == "__main__":
    main()