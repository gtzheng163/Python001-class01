学习笔记

pandas数据的导入 read_excel read_csv read_table read_sql 
读取文件
读取csv: read_csv() 引
读取excel: read_excel()
读取制表符分割的table： read_table()
参数
encoding 设置文件编码
header 设置表头
sep 设置分割符,sep可以是正则表达式
names 设置列名
index_col 设置行索引,可以是多个列组成的复合索引
skip_rows 跳过的某些行
na_values 将指定的值替换为NaN,还可以指定列索引,只替换指定的列的值
空值na函数
sheet_name指定的sheet页 head() shape info() describe() 

缺失值处理 填补 hansnans fillna ifnull().sum() ffill() ffill(axis=1) dropna
重复值处理 drop_duplicates

写入文件
写入csv: to_csv()
写入excel: to_excel()
写入pickle文件： to_pickle()

基础的数据定位操作
获取所有列名 df.colunm
获取指定的列名 df.column[]
获取行索引 df.index
获取指定的列的数据 df[‘列名’]
获取指定的多个列的数据 df[[‘列名1’,’列名2’]]
获取指定的行 df.loc[‘行索引’]
获取指定行号的数据 df.iloc[行号] ,支持切片操作
获取指定行号的数据的值(返回的是array) df.loc[‘行索引’].values

聚合操作
sum()
mean()
avg()
count()
std()
groupby() 指定列名,返回根据该列进行分组的结果的迭代器。


这周学习pandas的用法，老师用买菜和做菜的例子来类比pandas处理数据的流程很形象；
pandas处理数据涉及到的方法有很多，需要课下参考官方的文档，多加练习这些方法。