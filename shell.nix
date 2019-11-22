{ pkgs ? import <nixpkgs> { }, pythonPackages ? pkgs.python3Packages }:

let nb_nix_kernels = pythonPackages.buildPythonPackage {
      pname = "nb_nix_kernels";
      version = "1.0.0";

      src = ./.;

      propagatedBuildInputs = [ pythonPackages.jupyter_client ];
    };
in
pkgs.mkShell {
  buildInputs = [ pythonPackages.jupyterlab nb_nix_kernels];

  shellHook = ''
    # jupyter notebook
  '';
}
