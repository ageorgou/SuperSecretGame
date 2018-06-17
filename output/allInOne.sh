#!/bin/bash

# This needs pdfjam which comes as part of texlive and pdftk
# pacman -S texlive-core
# brew install pdfjam
# for pdftk... well here you can get some instructions for macos
# https://gist.github.com/jvenator/9672772a631c117da151
# and read the latest comments!

output=(output.pdf output_back.pdf)

if [[ $1 = '--shuf' ]]; then
    input_files=$(ls ??.pdf | shuf)
else
    input_files=$(ls ??.pdf)
fi

for i in ${output[@]}; do
    if [[ $i = *back* ]]; then
        input_files=$(seq $(ls ??.pdf | wc -l) | sed "c back_card.pdf")
    fi
    pdfjam ${input_files} -q --nup 4x2 --landscape --frame true  --outfile ${i}
done

# merge files interleaving page of one with pdftk
pdftk A=${output[0]} B=${output[1]} shuffle A B output allTogether.pdf
rm ${output[@]}
