# nb_nix_kernels

# Dependencies and Launching Jupyter

The nix way. Make sure you have [nix installed](https://nixos.org/nix/download.html) (linux, darwin, bsd only) 

```shell
nix-shell
jupyter notebook --NotebookApp.kernel_spec_manager_class='nb_nix_kernels.NixKernelSpecManager'
```

or the other way (maybe works?)

```shell
pip install . --user
jupyter notebook --NotebookApp.kernel_spec_manager_class='nb_nix_kernels.NixKernelSpecManager'
```

Or if you would like a shorter command `jupyter notebook` add the following to
your jupyter config `~/.jupyter/jupyter_notebook_config.py`.

```python
c.NotebookApp.kernel_spec_manager_class = 'nb_nix_kernels.NixKernelSpecManager'
```

# Custom jupyter environments in your notebook anywhere 

Currently does not support jupyterlab (only notebook). This command
will embed the environment in the notebook
`metadata.kernel_info.kernel_name`. And it only has to be run once (or
as many times as you like to have multiple environments). This can
work with `conda env ... run ...` as well but I have plans to make
this more nix specific. Here is the javascript you need to
execute/edit. If there was someone who was great with widgets I'm sure
this could be made prettier and work well with jupyterlab!

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

I was motivated by nix-shell shebang magic where dependencies are
embeded in the script. I **REALLY** wanted this is jupyter notebooks.

`example/example.py`

```python
#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 python37Packages.numba nodejs firefox

import numba
import subprocess
print(torch.randn(10))
print(subprocess.check_output('node -e "console.log(\'asdf\')"', shell=True))
subprocess.check_output('firefox', shell=True)
```
