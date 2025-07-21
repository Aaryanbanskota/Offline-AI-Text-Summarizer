#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>

namespace py = pybind11;

std::vector<std::string> fast_tokenize(const std::string& text, int max_length) {
    std::vector<std::string> chunks;
    for (size_t i = 0; i < text.size(); i += max_length) {
        size_t len = std::min((size_t)max_length, text.size() - i);
        chunks.push_back(text.substr(i, len));
    }
    return chunks;
}

PYBIND11_MODULE(tokenizer, m) {
    m.def("fast_tokenize", &fast_tokenize, "Chunk text fast");
}