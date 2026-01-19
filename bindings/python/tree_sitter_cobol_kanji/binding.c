#include <Python.h>

typedef struct TSLanguage TSLanguage;

TSLanguage *tree_sitter_COBOL(void);

static PyObject* _binding_language(PyObject *self, PyObject *args) {
    TSLanguage *language = tree_sitter_COBOL();
    if (language == NULL) {
        Py_RETURN_NONE;
    }
    return PyCapsule_New(language, "tree_sitter.Language", NULL);
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
