from DBConnection import DBConnection
from pandas import DataFrame
import jieba

"""
class segmentation(object):
    
    def __init__(self):
        super(segmentation, self).__init__()
        # jieba custom setting.
        jieba.set_dictionary('jieba_dict/dict.txt.big')
        pass
        
    
    def testing(self,val):
        # 默認是精確模式
        seg_list = jieba.cut(val)
        print("默認是精確模式: ")
        for i in seg_list:
            print(i)
        pass
"""    


def segmentation(text):
    seg_list = jieba.cut(text)
    return seg_list

if __name__ == "__main__":

    jieba.set_dictionary('jieba_dict/dict.txt.big')
    DBconn = DBConnection()


    DBconn.SetCmd(
        'select StuNun,text from oneimagetest_research where text is not null;')
    res = DBconn.select()
    df = DataFrame(res)

    # StuNun into list
    StuNun = df.StuNun.unique()
    
    #print(df.StuNun)
    #print(df.loc[df.StuNun == 'ds01'])

    for index, row in df.iterrows():
        seg = segmentation(row['text'])
        print(row['StuNun'], row['text'], end='seg:')

        for val in seg:
            print(val,end=',')
        print('')
        pass
    
    stop = 0
    
    for index, row in df.loc[df.StuNun == 'ds01'].iterrows():
        seg = segmentation(row['text'])
        print(row['StuNun'], row['text'], end='seg:')

        for val in seg:
            print(val,end=',')
        print('')

        pass

    #seg = segmentation('台北天氣真好')


    



    pass
