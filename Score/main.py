from DBConnection import DBConnection
from pandas import DataFrame
import jieba

def segmentation(text):
    seg_list = jieba.cut(text)
    return seg_list

if __name__ == "__main__":

    jieba.set_dictionary('Score\jieba_dict\dict.txt.big')
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


    pass
