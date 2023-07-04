
{ 
pkgs ? import <nixpkgs> {},
poetry2nix ? import <poetry2nix> {}
} :

poetry2nix.mkPoetryEnv {
    projectDir = ./.;
}