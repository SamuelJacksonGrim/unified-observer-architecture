#include <pybind11/pybind11.h>
#include "coherence_engine.h"

namespace py = pybind11;

PYBIND11_MODULE(coherence_engine, m) {
    m.doc() = "High-performance coherence engine";
    m.def("compute_coherence", &compute_coherence, "Compute coherence score");
}
