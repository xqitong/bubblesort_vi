import random
import matplotlib
# matplotlib.use("Agg") # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from os.path import abspath

# plt.rcParams["animation.ffmpeg_path"] = abspath("./ffmpeg/bin/ffmpeg.exe")
# 
# plt.rcParams['animation.ffmpeg_path'] = "C:\Program Files\ImageMagick-7.0.7-Q16/ffmpeg.exe"

def setcolor(i_idx,m_idx,lst):
    res=[]
    for i, ele in enumerate(lst):
        lev = '#95a5a6'#设置颜色
        if i == i_idx:
            lev = '#e74c3c' #当前对象
        elif i == m_idx:
            lev = '#2ecc71' #比较对象
        res.append((ele,lev))
    return res


def bubs(lst):
    res=[]
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            res.append(setcolor(j,j+1,lst))
            if lst[j+1] < lst[j]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            res.append(setcolor(j,j+1,lst))
    res.append(setcolor(-1,-1,lst))
    return res

lst = list(range(1,10))
random.shuffle(lst)
result=bubs(lst)


fig, ax = plt.subplots()

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=24, metadata=dict(artist='Me'), bitrate=2000)

def update(res):
    pcols=[]
    plsts=[]
    for elenum,elecol in res:
        plsts.append(elenum)
        pcols.append(elecol)
    plt.cla()#清除残影
    return plt.bar(list(range(len(plsts))),plsts,color=pcols)
    

ani = FuncAnimation(fig, update,frames=result,interval = 100,repeat=False,blit=True)
# ani.save('bobs.mp4', writer=writer)
plt.show()
