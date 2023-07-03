#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages(ps: [ ps.numpy ])"

import numpy as np


def main():
    a = np.array([1, 2])
    b = np.array([3, 4])
    print(f"The dot product of {a} and {b} is: {np.dot(a, b)}")


if __name__ == "__main__":
    main()
