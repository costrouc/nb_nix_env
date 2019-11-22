'''
%%javascript
// only have to run once
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
    spec: {display_name: kernel_name, language: "python"},
    resources: {}
};
IPython.kernelselector.set_kernel(kernel_name);
'''

import base64
import shlex

from jupyter_client.kernelspec import KernelSpecManager
from jupyter_client.kernelspec import KernelSpec


DEFAULT_NIX = shlex.split('nix-shell -p python3Packages.ipykernel --run "python3 -m ipykernel -f {connection_file}"')


class NixKernelSpecManager(KernelSpecManager):
    def get_kernel_spec(self, kernel_name):
        try:
            cmd = base64.b64decode(kernel_name.replace('_', '=')).decode('utf-8')
            return KernelSpec(argv=shlex.split(cmd), language='python', display_name=kernel_name)
        except Exception:
            pass
        return KernelSpec(argv=DEFAULT_NIX, language='python', display_name=kernel_name)
