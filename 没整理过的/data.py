# coding=utf-8
import pandas


def chaifenexl():
    path='/Users/td/Desktop/线上数据分析/色情风险/源文件/seqing.json'
    ds=pandas.read_excel(path)
    nrows = ds.shape[0]
    print(nrows)
    begin=0
    end=begin+1000000
    mark=1
    while end < int(nrows):
        peth2='/Users/td/Desktop/线上数据分析/色情风险/源文件/拆分seqing%s.json'%str(mark)
        #end= int(nrows)
        print(begin,end)
        xiao_result=ds.iloc[begin:end]
        print(peth2,xiao_result.shape[0])
        toexl(xiao_result,peth2)
        mark+=1
        begin=end
        end = begin + 1000000

    end=int(nrows)-1
    xiao_result = ds.iloc[begin:end]
    peth2 = '/Users/td/Desktop/线上数据分析/色情风险/源文件/拆分seqing%s.json' % str(mark)
    toexl(xiao_result, peth2)
    print('end')


if __name__ == '__main__':
    chaifenexl()
    print (1)