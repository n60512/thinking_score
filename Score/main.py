from DBConnection import DBConnection
from pandas import DataFrame
import jieba


def Console(text, flag):
    if flag:
        print(text)
    pass

def segmentation(text):
    seg_list = jieba.cut(text)
    return seg_list

def EvaluateScore(df, targetStu):
    console_flag = False
    similarCount = 0
    for index, row in df.loc[df.StuNun == targetStu].iterrows():
        seg = segmentation(row['text'])

        ## 每一個斷詞結果 (本次作答)
        for val in seg:
            similarflag = False

            for index_j, row_j in df.loc[df.StuNun == targetStu].iterrows():
                if index_j > index:
                    seg_j = segmentation(row_j['text'])
                    ## 每一個斷詞結果 (其他答案)
                    for val_j in seg_j:
                        # print(val, val_j) # show all result
                        if (val == val_j):
                            Console(('Same -> [%s,%s]' % (val, val_j)),console_flag)
                            similarflag = True
                            break
            pass

        if (not similarflag):
            Console(('[%s] get point' % row['text']),console_flag)
            similarCount += 1
        pass

    return similarCount
    

if __name__ == "__main__":

    jieba.set_dictionary('jieba_dict\dict.txt.big')
    DBconn = DBConnection()

    DBconn.SetCmd(
        'select StuNun,text from oneimagetest_research where text is not null order by StuNun;')
    res = DBconn.select()
    df = DataFrame(res)

    DBconn.SetCmd(
        'select StuNun,count(StuNun) as counter from oneimagetest_research where text is not null group by StuNun;')
    countRes = DBconn.select()
    count_df = DataFrame(countRes)


    # StuNun into list
    # StuNun = df.StuNun.unique()


    for index, row in count_df.iterrows():
        #print(row['StuNun'], row['counter'])
        print('[%s]: %s , %s' % (row['StuNun'], EvaluateScore(
            df, row['StuNun']), row['counter']))
        pass

    """
    for val in segmentation('高線'):
        print(val)
    for val in segmentation('等高線'):
        print(val)
    """

    pass
