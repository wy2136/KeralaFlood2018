#!/usr/bin/env python
import numpy as np
import xarray as xr
import os

ifiles = '/tigress/wenchang/MODEL_OUT/cesm1_2_1/B1850CN_f05g16_tigercpu_intelmpi18_512PE/atm/hist/B1850CN_f05g16_tigercpu_intelmpi18_512PE.cam.h1.????-01-01-00000.nc'
data_name = "PRECT"
ofile = f'B1850CN_f05g16_tigercpu_intelmpi18_512PE.cam.h1.{data_name}.nc'
xname = 'lon'
xlim = (70, 80)
yname = 'lat'
ylim = (5, 15)

x = xr.open_mfdataset(ifiles)[xname].values
ix = x.argsort()
L = (x>=xlim[0]) & (x<=xlim[1])
ixlim = ix[L][0], ix[L][-1]
print(f'xlim: {xlim}; ixlim: {ixlim}')

y = xr.open_mfdataset(ifiles)[yname].values
iy = y.argsort()
L = (y>=ylim[0]) & (y<=ylim[1])
iylim = iy[L][0], iy[L][-1]
print(f'ylim: {ylim}; iylim: {iylim}')

cmd = f'ncrcat -v {data_name} -d {xname},{ixlim[0]},{ixlim[1]} -d {yname},{iylim[0]},{iylim[1]} {ifiles} {ofile}'
print(cmd, '...')
s = os.system(cmd)
if s==0:
    print('[OK]:', cmd)
