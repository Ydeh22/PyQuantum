# --------------------
from math import sqrt
KHz = 10 ** 3  # 1 KГц
MHz = 10 ** 6  # 1 МГц
GHz = 10 ** 9  # 1 ГГц

mks = 1e-6  # 1 мкс
ns = 1e-9  # 1 мкс
# --------------------
# BEGIN----------------------------------------- CAVITY -------------------------------------------
capacity = 2

wc = 6.729 * GHz

wa = wc

g = 1.0 * 1e-1 * wc

n_atoms = 2

n_levels = 3
# END------------------------------------------- CAVITY -------------------------------------------

# -------------------------------------------------------------------------------------------------
# T = 0.05 * mks
# T = 100
# T = 0.1 * mks
# T = 0.25 * mks
# T = 0.5 * mks
# T = 1 * mks
T = 50 * mks
# T = 10 * mks

# dt = T / 500
# dt = T / 1000

# nt = int(T / dt)
# -------------------------------------------------------------------------------------------------
nt = 100

# nt = int(T*nt)
nt = int(T/mks*nt)

dt = T / nt
# -------------------------------------------------------------------------------------------------

# init_state = [1, [0, 1]]
init_state = [0, [0, 2]]
# init_state2 = [0, [1, 1]]
# init_state = [2, [0, 1, 0]]
# certain_state = [1, [0, 1]]

precision = 5

# -------------------------------------------------------------------------------------------------
path = "test_tcl/TC/out/" + str(capacity) + "_" + str(n_atoms) + "/"
H_html = path + "H.html"
H_csv = path + "H.csv"
U_csv = path + "U.csv"
ro_0_csv = path + "ro_0.csv"
U_csv = path + "U.csv"
x_csv = path + "x.csv"
y_csv = path + "t.csv"
z_csv = path + "z.csv"
z_all_csv = path + "z_all.csv"
fid_csv = path + "fid.csv"
fid_small_csv = path + "fid_small.csv"
# -------------------------------------------------------------------------------------------------
