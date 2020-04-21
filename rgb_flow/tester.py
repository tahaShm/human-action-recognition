import numpy as np
outfile = TemporaryFile()
x = np.arange(10)
np.save("aaa.npy", x)