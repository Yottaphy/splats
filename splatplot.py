import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def top(x):
    if x <= -109.5:
        return -x-220
    elif x<= -104:
        return -110.5
    else:
        return x-6.5

def bottom(x):
    if x <= -109.5:
        return x-6
    elif x<= -104:
        return -115.5
    else:
        return -x-219.5

n,t,x,y,z,k = np.genfromtxt( "splats.txt", unpack=True, skip_header=87, skip_footer=1, autostrip=True)

lostx = []
losty = []
lostz = []
for i in range(len(z)):
    if z[i] > -450:
        lostx.append(x[i])
        losty.append(y[i])
        lostz.append(z[i])
        
xtop = []
xbot = []
ytop = []
ybot = []
zplot = np.arange(-112,-101.51, 0.01)

for i in range(len(zplot)):
    xtop.append(top(zplot[i])+113)
    xbot.append(bottom(zplot[i])+113)

    ytop.append(top(zplot[i]))
    ybot.append(bottom(zplot[i]))

radius = 2.5
big    = 4.5
angle  = np.linspace(0, 2*np.pi, 500)

eleccol = 'k'
pointcol = 'C0'

fig, axes = plt.subplots(1,3, figsize = (13, 13))
ax = axes[1]
ay = axes[0]
az = axes[2]

ax.plot(zplot, xtop, color = eleccol)
ax.plot(zplot, xbot, color = eleccol)
ax.plot(lostz, lostx, 'o', color = pointcol)
ax.set_title("Y Slice")  
ax.set_xlabel("z [mm]")
ax.set_ylabel("x [mm]")

ay.plot(zplot, ytop, color = eleccol)
ay.plot(zplot, ybot, color = eleccol)
ay.plot(lostz, losty, 'o', color = pointcol)
ay.set_title("X Slice")  
ay.set_xlabel("z [mm]")
ay.set_ylabel("y [mm]")

az.plot(radius*np.cos(angle), radius*np.sin(angle)-113 , color = eleccol)
#az.plot(big*np.cos(angle), big*np.sin(angle)-113 , color = 'none')
az.plot(lostx,losty, 'o', color = pointcol)
#az.set_ylim(-118.5,-107.5)
az.set_title("Z Slice")  
az.set_xlabel("x [mm]")
az.set_ylabel("y [mm]")

for i in range(0,3):
    axes[i].set_aspect('equal', 'box')

fig.tight_layout()
fig.savefig("splats.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)
fig.savefig("splats.png", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)