import random
import matplotlib
# matplotlib.use("Agg") # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from os.path import abspath
from xsort import chooseSF
import fire

# https://ffmpeg.org/
# plt.rcParams["animation.ffmpeg_path"] = abspath("./ffmpeg/bin/ffmpeg.exe")
# plt.rcParams['animation.ffmpeg_path'] = "C:\Program Files\ImageMagick-7.0.7-Q16/ffmpeg.exe"



class ViSort(object):
    def __init__(self):

        self._fig, self._ax = plt.subplots()
        Writer = animation.writers['ffmpeg']
        self._writer = Writer(fps=24, metadata=dict(artist='Me'), bitrate=2000)

    def sortx(self,algo,data=None):
        
        self.sort_func = chooseSF()[algo]
        if not self.sort_func:
            raise NotImplementedError
        if data == None:
            data = self._random_generate(10)

        result = self.sort_func(data)
        self._ani = FuncAnimation(self._fig, self._update,frames=result,interval = 10,fargs=(self.sort_func.__name__,),repeat=False,blit=True)
        # self._ani.save(self.sort_func.__name__+'.mp4', writer=self._writer)
        plt.show()

    def _random_generate(self,size):
        lst = list(range(1,size))
        random.shuffle(lst)
        return lst

    def _update(self,res,*fargs):
        pcols=[]
        plsts=[]
        funcname, = fargs
        for elenum,elecol in res:
            plsts.append(elenum)
            pcols.append(elecol)
        plt.cla()#清除残影
        plt.title(funcname, fontsize=20)
        leftx = list(range(len(plsts)))
        for xy in zip(leftx,plsts):
            plt.annotate("%s" % xy[1], xy=xy, xytext=(-5, 10), textcoords='offset points')
        return plt.bar(leftx,plsts,color=pcols)


if __name__ == '__main__':
    # 命令行模式
    fire.Fire(ViSort())
    #-----------setting area--------------------
    # bubble_sort，insert_sort, select_sort
    #-------------------------------------------
    # myViSort=ViSort()
    # myViSort.sortx('select_sort',[3,2,1,6,5,8,0])
    #-------------------------------------------
        

