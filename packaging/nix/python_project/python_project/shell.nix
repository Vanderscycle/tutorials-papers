with import <nixpkgs> {};
let
  pythonEnv = python311.withPackages (ps: with ps; [
    numpy
  ]);
in mkShell {
  packages = [
    pythonEnv

    black
    mypy

  ];
}