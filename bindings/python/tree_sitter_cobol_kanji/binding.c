#include <Python.h>

typedef struct TSLanguage TSLanguage;

TSLanguage *tree_sitter_COBOL(void);

static PyObject* _binding_language(PyObject *self, PyObject *args) {
    return PyLong_FromVoidPtr(tree_sitter_COBOL());
}

static PyMethodDef methods[] = {
    {"language", _binding_language, METH_NOARGS,
     "Get the tree-sitter language for this grammar."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_binding",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__binding(void) {
    return PyModule_Create(&module);
}
