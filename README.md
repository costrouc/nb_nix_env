# nb_nix_kernels

The nix way

```shell
nix-shell
jupyter notebook
```

or the other way (maybe works)

```shell
pip install . --user
jupyter notebook
```

Add to `~/.jupyter/jupyter_notebook_config.py` 

```python
c.NotebookApp.kernel_spec_manager_class = 'nb_nix_kernels.NixKernelSpecManager'
```

# put this inside of your notebook anywhere 

Currently does not support jupyterlab (only notebook). This command
will embed the environment in the notebook
`metadata.kernel_info.kernel_name`. And it only has to be run once.

```javascript
%%javascript
// only have to run once and the kernel should auto load
var kernel_name = btoa(`
nix-shell -p python3Packages.ipykernel
             python3Packages.numpy
             python3Packages.scipy
             python3Packages.flask
             nodejs
            --run "python3 -m ipykernel -f {connection_file}"
`).replace('=', '_');

IPython.kernelselector.kernelspecs[kernel_name] = {
    name: kernel_name,
    spec: {display_name: "nix-env", language: "python"},
    resources: {}
};
IPython.kernelselector.set_kernel(kernel_name);
```

# Motivation

nix-shell shebang magic where dependencies are embeded in the script.

```python
#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 python37Packages.pytorch nodejs firefox

import torch
import subprocess
print(torch.randn(10))
print(subprocess.check_output('node -e "console.log(\'asdf\')"', shell=True))
subprocess.check_output('firefox', shell=True)
```
