import h5py
import numpy as np 
import matplotlib.pyplot as plt 
f = h5py.File("./singlecoil_val/file1000000.h5","r")
print(list(f.keys()))
dset = f['kspace']
print(dset.shape)
print(dset.dtype)
print(dset.name)
print(f.name)
dset1 =f['reconstruction_esc']
print(dset1.shape)
print(dset1.dtype)
ref =dset1[0]
plt.imshow(ref,cmap="gray")