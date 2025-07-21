#!/bin/bash
set -e
c++ -O3 -Wall -shared -std=c++11 -fPIC \
    $(python3 -m pybind11 --includes) \
    cpp/tokenizer.cpp \
    -o cpp_build/tokenizer$(python3-config --extension-suffix)
echo "✅ C++ module built in cpp_build/"