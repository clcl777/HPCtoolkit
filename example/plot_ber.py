import os
import matplotlib.pyplot as plt


def save_file_name(default_file_name):
    k = 1
    while True:
        if os.path.isfile(default_file_name + str(k) + '.png'):
            k = k + 1
        else:
            file_name = default_file_name + str(k) + '.png'
            return file_name


def plot_ber(SIM):
    LW = 2
    FS = 16
    FN = 'Times New Roman'
    MS = 12

    plt.figure(0)
    plt.title('')
    plt.grid(True)
    plt.xlabel(r'$E_s/N_0$[dB]')
    plt.ylabel('BER')
    plt.plot(SIM.EsN0, SIM.BER, 'o-', ms=MS, markerfacecolor='#ffffff', lw=LW)
    ax = plt.gca()
    ax.set_yscale('log')
    plt.savefig('BER_' + str(SIM.Kd) + 'bit' + '.png')
    # plt.show()
