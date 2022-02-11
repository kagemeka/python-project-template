#!/bin/bash

poetry run make --directory=docs clean &&
    poetry run make --directory=docs html
