#!/bin/bash

get_current_file_directory() {
    file_abs_path="$(readlink -f "${BASH_SOURCE[0]}")"
    directory_path="$(dirname "${file_abs_path}")"
    echo "${directory_path}"
}

root=$(dirname "$(get_current_file_directory)")
docs_path="$root"/docs/sphinx

poetry run make --directory="$docs_path" clean &&
    poetry run make --directory="$docs_path" html
