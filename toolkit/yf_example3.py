import os
import toolkit_config as cfg
from toolkit import yf_example2


def qan_prc_to_csv(year):
    start = str(year)+"-01-01"
    end = str(year)+"-12-31"
    tic = 'QAN.AX'
    file_name = 'qan_prc_'+str(2020)+'.csv'
    pth = os.path.join(cfg.DATADIR, file_name)
    yf_example2.yf_prc_to_csv(tic, pth, start, end)

if __name__ == "__main__":
    qan_prc_to_csv(2020)

