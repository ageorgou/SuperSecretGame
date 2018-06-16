#!/bin/bash

# This needs pdfjam which comes as part of texlive
# pacman -S texlive-core
# brew install mactex (??)

if [[ $1 = '--shuf' ]]; then
    pdfjam $(ls ??.pdf | shuf)  --nup 2x4 --outfile output_random.pdf

else
    pdfjam ??.pdf  --nup 2x4 --outfile output.pdf
fi
