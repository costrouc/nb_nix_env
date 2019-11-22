#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 python37Packages.numba nodejs firefox

import numba
import subprocess
print(subprocess.check_output('node -e "console.log(\'asdf\')"', shell=True))
subprocess.check_output('firefox', shell=True)
print('opened firefox!')
