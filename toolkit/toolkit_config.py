import os
PRJDIR = "D:\\python\\toolkit"
DATADIR = os.path.join(PRJDIR, 'data')

if __name__ == "__main__":
    fobj = open("../qan_stk_prc.csv", mode ='rt')
    print(type(fobj))