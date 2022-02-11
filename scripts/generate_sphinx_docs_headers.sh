#!/bin/bash

get_current_file_directory() {
    file_abs_path="$(readlink -f "${BASH_SOURCE[0]}")"
    directory_path="$(dirname "${file_abs_path}")"
    echo "${directory_path}"
}

root=$(dirname "$(get_current_file_directory)")
src=$root/src

poetry run sphinx-apidoc \
    -d 2 \
    -H "Python Project Templates" \
    --separate \
    --follow-links \
    --full \
    -o docs \
    -s rst \
    "$src" \
    "$src"/**/*_test.py \
    "$src"/**/tests/ \
    "$src"/**/test_*.py \
    "$src"/**/_test_*.py \
    "$src"/scripts/

# full options
# https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
