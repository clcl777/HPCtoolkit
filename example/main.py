import numpy as np
import main_task
import plot_ber
import multiprocessing


class Constant:
    pass


if __name__ == '__main__':
    SIM = Constant()
    SIM.nworker = 8
    SIM.Kd = 32
    SIM.wloop = 5
    SIM.ml = 4
    SIM.EsN0 = np.arange(0, 21, 2)
    SIM.nloop = 10**SIM.wloop
    SIM.Q = 2**SIM.ml
    RES = np.zeros([len(SIM.EsN0), 7])

    # hpctoolkitのための設定
    manager = multiprocessing.Manager()
    SIM.lock = manager.Lock()

    if SIM.nworker == 1:
        RES = main_task.main_task([0, SIM])
    else:
        # 並列処理
        pool = multiprocessing.Pool(processes=SIM.nworker)
        params = []
        for p in range(SIM.nworker):
            params.append([p, SIM])  # wokerの番号を渡す
        RES_ = pool.map(main_task.main_task, params)
        pool.close()
        RES = sum(RES_)

    SIM.BER = RES[:, 0]/RES[:, 3]
    SIM.BLER = RES[:, 1] / RES[:, 4]
    plot_ber.plot_ber(SIM)
