# NixOS learning 

## Troubleshooting
If you get weird errors in your flake files saying that it is missing flake.nix ensure that it is a repo and has been pushed.
## Go 
nix flake init -t github:nix-community/gomod2nix#app
go get -d ./... is all that is required to run go programs

## Python
Package management [Poetry](https://python-poetry.org/docs/) and how it does [it](https://toraritte.github.io/poetry-intro/#using-a-hrefhttpspython-poetryorg-titlethe-poetry-websitepoetrya-with-a-hrefhttpsnixosorg-titlethe-website-of-the-nix-cross-platform-system-package-managernixa)

Nix shell [tutorial](https://nixos.org/manual/nixpkgs/stable/#python)
nix flake init -t github:nix-community/poetry2nix#app

## TS/JS
nix flake init -t github:nix-community/dream2nix#simple
nix flake init // (hello world)