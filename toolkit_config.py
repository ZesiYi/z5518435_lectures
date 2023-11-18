import os
PRJDIR = "D:\\python"
DATADIR = os.path.join(PRJDIR, 'project2\\data')

if __name__ == "__main__":
    fobj = open("../qan_stk_prc.csv", mode ='rt')
    print(type(fobj))