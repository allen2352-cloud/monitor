from os import listdir,stat
from os.path import getsize,isdir
from time import time,sleep
class Indexer:
    def __init__(self):
        self.road=''
        self.index=[['C:',0,[]],['D:',0,[]]]#資料夾:[名稱,尺寸,物件夾], 檔案:(名稱,尺寸,上次修改時間)
    def listdir(self,road):
        def find_dir(box,roads):
            if len(roads)==0:return box
            for i in box:
                if i[0]==roads[0] and type(i)==list:
                    return find_dir(i[-1],roads[1:])
            return box
        return find_dir(self.index,road.replace('\\','/').split('/'))
    def explore(self):
        def expand(road):
            size,box=0,[]
            try:
                o=listdir(road)
                for i in o:
                    if isdir(f'{road}{i}'):
                        box+=[[i]+expand(f'{road}{i}/')]
                    else:box+=[(i,getsize(f'{road}{i}'),int(stat(f'{road}{i}').st_mtime))]
                    size+=box[-1][1]
            except:box=[('無法讀取此資料夾.ban',0,0)]
            return [size,box]
        #road,dir_name=road.replace('\\','/')+'/',road.replace('\\','/').split('/')[-1]
        self.index=[['C:']+expand('C:/'),['D:']+expand('D:/')]
        open(f'index.txt','w',encoding='utf-8').write(str(self.index))
c=Indexer()
c.explore()
#get=c.listdir('C:')
#print(get)