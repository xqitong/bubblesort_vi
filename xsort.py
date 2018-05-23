

def chooseSF():
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

    def insertSort(lst):
        res = []
        res.append(setcolor(-1,-1,lst))
        for i in range(1,len(lst)): #i控制有序区长度，开始[0,1)已排序
            x = lst[i]
            j = i
            res.append(setcolor(j,-1,lst))
            while j > 0 and lst[j-1] > x:
                res.append(setcolor(j,j-1,lst))
                lst[j] = lst[j-1]
                res.append(setcolor(j,j-1,lst))
                j -= 1
            lst[j] = x
        res.append(setcolor(-1,-1,lst))
        return res

    def bubbleSort(lst):
        res=[]
        for i in range(len(lst)-1): #i控制有序区长度
            for j in range(len(lst)-i-1): # 比较无序区中j 与 j+1的元素，满足条件交换，注意下标
                res.append(setcolor(j,j+1,lst))
                if lst[j+1] < lst[j]:
                    lst[j],lst[j+1] = lst[j+1],lst[j]
                res.append(setcolor(j,j+1,lst))
        res.append(setcolor(-1,-1,lst))
        return res


    def selectSort(lst):
        res = []
        for i in range(len(lst)-1):
            mininx = i
            res.append(setcolor(mininx,-1,lst))
            for j in range(i+1,len(lst)):
                res.append(setcolor(mininx,j,lst))
                if lst[j] < lst[mininx]:
                    mininx = j
            res.append(setcolor(mininx,i,lst))
            lst[i],lst[mininx] = lst[mininx], lst[i]
            res.append(setcolor(mininx,i,lst))
        return res


    sortFunc = {'bubble_sort':bubbleSort,'insert_sort':insertSort,'select_sort':selectSort}
    return sortFunc