# NixOS learning 

## Troubleshooting
If you get weird errors in your flake files saying that it is missing flake.nix ensure that it is a repo and has been pushed.
## Go 

### Locally
go get -d ./... is all that is required to run go programs


### Flakes
[ ] nix flake init -t github:nix-community/gomod2nix#app
[ ] TODO: currently I do not understand the nixway

## Python
Package management [Poetry](https://python-poetry.org/docs/) and how it does [it](https://toraritte.github.io/poetry-intro/#using-a-hrefhttpspython-poetryorg-titlethe-poetry-websitepoetrya-with-a-hrefhttpsnixosorg-titlethe-website-of-the-nix-cross-platform-system-package-managernixa)

### Locally

`poetry new ${NAME}` or `poetry init`
To add a new python package `poetry add ${package_name}`
[ ] TODO: Doesn't run locally if a package is required.


Nix shell [tutorial](https://nixos.org/manual/nixpkgs/stable/#python)

nix flake init -t github:nix-community/poetry2nix#app

## TS/JS

### Locally

If only requiring a single file.
`chmod +x ${file_name}`
```nix
#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages(ps: [ ps.numpy ])"
```

### poetry
`pnpm install ${npm_package}` 
`pnpm run ${script}`

###Nixos
nix flake init -t github:nix-community/dream2nix#simple
nix flake init // (hello world)