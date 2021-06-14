import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def top(x, cham):
    if x <= -109.5 and cham ==2:
        return -x-220
    elif x<= -104:
        return -110.5
    else:
        return x-6.5

def bottom(x, cham):
    if x <= -109.5 and cham ==2:
        return x-6
    elif x<= -104:
        return -115.5
    else:
        return -x-219.5

#expected txt file: ion number, tof, x, y, z, kinetic energy
n,t,x,y,z,k = np.genfromtxt( "splats1cham_new.txt", unpack=True, skip_header=87, skip_footer=1, autostrip=True)

cham = 1  #number of chamfers


#compute the positions of splats that don't reach the end
lostx = []
losty = []
lostz = []
for i in range(len(z)):
    if z[i] > -450:
        lostx.append(x[i])
        losty.append(y[i])
        lostz.append(z[i])

#draw the aperture cross-section        
xtop = []
xbot = []
ytop = []
ybot = []
zplot = np.arange(-112,-101.51, 0.01)

for i in range(len(zplot)):
    xtop.append(top(zplot[i], cham)+113)
    xbot.append(bottom(zplot[i], cham)+113)

    ytop.append(top(zplot[i], cham))
    ybot.append(bottom(zplot[i], cham))

radius = 2.5
big    = 4.5
angle  = np.linspace(0, 2*np.pi, 500)

eleccol = 'k'
pointcol = 'C0'

plt.rcParams.update({'font.size': 16})
fig, axes = plt.subplots(1,3, figsize=(16,9), gridspec_kw={'width_ratios': [1, 1, 0.869]})
ax = axes[1]
ay = axes[0]
az = axes[2]

ax.plot(zplot, xtop, color = eleccol)
ax.plot(zplot, xbot, color = eleccol)
if cham == 1:
    ax.axvline(x=min(zplot),ymin=min(xtop),ymax=max(xtop), color=eleccol)
    ax.axvline(x=min(zplot),ymin=min(xbot),ymax=max(xbot), color=eleccol)
ax.plot(lostz, lostx, 'o', color = pointcol)
ax.set_title("Y Slice")  
ax.set_xlabel("z [mm]")
ax.set_ylabel("x [mm]")
ax.set_ylim(-5,5)

ay.plot(zplot, ytop, color = eleccol)
ay.plot(zplot, ybot, color = eleccol)
if cham == 1:
    ay.axvline(x=min(zplot),ymin=min(ytop),ymax=max(ytop), color=eleccol)
    ay.axvline(x=min(zplot),ymin=min(ybot),ymax=max(ybot), color=eleccol)
ay.plot(lostz, losty, 'o', color = pointcol)
ay.set_title("X Slice")  
ay.set_xlabel("z [mm]")
ay.set_ylabel("y [mm]")
ay.set_ylim(-118,-108)

az.plot(radius*np.cos(angle), radius*np.sin(angle)-113 , color = eleccol)
#az.plot(big*np.cos(angle), big*np.sin(angle)-113 , color = 'none')
az.plot(lostx,losty, 'o', color = pointcol)
az.set_title("Z Slice")  
az.set_xlabel("x [mm]")
az.set_ylabel("y [mm]")

for i in range(0,3):
    axes[i].set_aspect('equal','box')
    axes[i].tick_params(axis="x",direction="in", top="on",labelbottom="on")
    axes[i].tick_params(axis="y",direction="in", right="on",labelleft="on")

fig.tight_layout()
fig.savefig("splats"+str(cham)+"cham_new.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)
fig.savefig("splats"+str(cham)+"cham_new.png", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)