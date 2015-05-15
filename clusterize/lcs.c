#include <Python.h>
#include <string.h>

void* create_table(int r, int c) {
    int i;
    int **arr = (int **)calloc(r, sizeof(int *));
    for (i=0; i<r; i++)
         arr[i] = (int *)calloc(c, sizeof(int));
    return arr;
}

void print_table(int** table, int r, int c) {
    int i,j;
    for (i = 0; i <  r; i++)
    {
        for (j = 0; j < c; j++)
        {
            printf("%d ", table[i][j]);
        }
        printf("\n");
    }
}

static PyObject *
lcs(PyObject *self, PyObject *args)
{
    const char *str1;
    const char *str2;
    int **mem;

    int max_len = 0;
    int s1_end = 0;
    int s2_end = 0;
    int s1_len = 0;
    int s2_len = 0;
    int x, y;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;
    s1_len = strlen(str1);
    s2_len = strlen(str2);

    mem = create_table(s1_len+1, s2_len+1);
    for(x=1; x<=s1_len; x++)
    {
        for(y=1; y<=s2_len; y++)
        {
            if(str1[x-1] == str2[y-1])
            {
                mem[x][y] = mem[x-1][y-1] + 1;
                if(mem[x][y] > max_len) {
                    max_len = mem[x][y];
                    s1_end = x;
                    s2_end = y;
                }
            }
            else
            {
                mem[x][y] = 0;
            }
        }
    }
    free(mem);
    return Py_BuildValue("(iii)", s1_end-max_len, s2_end-max_len, max_len);
}

static PyMethodDef lcsModule_methods[] = {
    {"lcs",  lcs, METH_VARARGS,
     "Calculates the Longest Common Substring."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

void initlcs(void)
{
    // Init module.
    (void) Py_InitModule("lcs", lcsModule_methods);
}
