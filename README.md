# nb_nix_kernels

The nix way

```shell
nix-shell
```

or the other way

```shell
pip install . --user
```

Add to `~/.jupyter/jupyter_notebook_config.py` 

```python
c.NotebookApp.kernel_spec_manager_class = 'nb_nix_kernels.NixKernelSpecManager'
```


