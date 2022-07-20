# Python之pandas中Series对象下的str方法汇总

1. cat（和指定字符进行拼接）
2. split（按照指定字符串分隔）
3. rsplit（和split用法一致，只不过默认是从右往左分隔）
4. partition（也是按照指定字符串分隔，和python内置的partition一样）
5. rpartition（和partition类似，不过是默认是从右往左找到第一个分隔符）
6. get（获取指定位置的字符，只能获取1个）
7. slice（和python内置的slice一样。get相当于是[n],slice相当于是[m: n]）
8. slice_replace（从名字也能看出来，slice筛选出来之后替换）
9. join（将每个字符之间使用指定字符相连，相当于sep.join(list(value))）
10. contains（判断字符串是否含有指定子串，返回的是bool类型）
11. startswith（是否某个子串开头）
12. endswith（判断是否以某个子串结尾）
13. match（从头开始匹配的。返回布尔型，表示是否匹配给定的模式）
14. replace（替换指定的字符）
15. repeat（重复字符串）
16. pad（将每一个元素都用指定的字符填充，只能是一个字符）
17. zfill（填充，只能是0，从左边填充）
18. encode decode（字符串编码、解码）
19. strip（按照指定内容，从两边去除，和python字符串内置的strip一样）
20. translate（指定部分替换）
21. extract（分组捕获）
22. find（查找指定字符第一次出现的位置）

> 在使用pandas的时候，经常要对DataFrame的某一列进行操作，一般都会使用df[“xx”].str下的方法，但是都有哪些方法呢？
> 我们下面来罗列并演示一下。既然是df[“xx”].str，那么xx这一列必须是字符串类型，当然在pandas里面是object，不能是整型、时间类型等等。如果想对这些类型使用的话，必须先df[“xx”].astype(str)转化一下，才能使用此方法。

例如有如下数据：  
数组名：df

![](https://img-blog.csdnimg.cn/2020081315123236.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzc1MDM3Nw==,size_16,color_FFFFFF,t_70#pic_center)

## 1. cat（和指定字符进行拼接）

```python
print(df["name"].str.cat())
"""
莫伊拉士兵76死神托比昂安娜aaa
"""
# 可以看到如果cat里面不指定参数，是将所有字段拼接在一起了

print(df["name"].str.cat(sep='-'))
"""
莫伊拉-士兵76-死神-托比昂-安娜-aaa
"""
# 可以指定sep分隔符，会自动用sep连接

print(df["name"].str.cat(['xx'] * len(df)))
"""
0     莫伊拉xx
1    士兵76xx
2      死神xx
3     托比昂xx
4      安娜xx
5     aaaxx
Name: name, dtype: object
"""
# 第一个参数要么不传，要么是一个与之等长的序列
# 会按照索引顺序将元素组合起来，得到一个新的Series

print(df["name"].str.cat(['xx'] * len(df), sep="@"))
"""
0     莫伊拉@xx
1    士兵76@xx
2      死神@xx
3     托比昂@xx
4      安娜@xx
5     aaa@xx
Name: name, dtype: object
"""
# 当然此时也是可以指定分隔符的

print(df["attack"].str.cat(['xx'] * len(df), sep="@"))
"""
0     近距离@xx
1     远距离@xx
2     近距离@xx
3    中远距离@xx
4     远距离@xx
5        NaN
Name: attack, dtype: object
"""

print(df["attack"].str.cat(['xx'] * len(df), sep="@", na_rep="-"))
"""
0     近距离@xx
1     远距离@xx
2     近距离@xx
3    中远距离@xx
4     远距离@xx
5       -@xx
Name: attack, dtype: object
"""
# 可以看到如果一方为NaN,name结果也为NaN,因此我们可以指定na_rep,表示将NaN用na_rep替换
```

## 2. split（按照指定字符串分隔）

```python
print(df["attack"].str.split())
"""
0     [近距离]
1     [远距离]
2     [近距离]
3    [中远距离]
4     [远距离]
5      None
Name: attack, dtype: object
"""
# 不指定分隔符，默认就是一个列表

print(df["attack"].str.split("距"))
"""
0     [近, 离]
1     [远, 离]
2     [近, 离]
3    [中远, 离]
4     [远, 离]
5       None
Name: attack, dtype: object
"""
# 和python内置split一样

print(df["attack"].str.split("距", n=-1))
"""
0     [近, 离]
1     [远, 离]
2     [近, 离]
3    [中远, 离]
4     [远, 离]
5       None
Name: attack, dtype: object
"""
# 指定n，表示分隔次数，默认是-1，全部分隔

print(df["attack"].str.split("距", expand=True))
"""
      0     1
0     近     离
1     远     离
2     近     离
3    中远     离
4     远     离
5  None  None
"""
# 注意这个expand，默认是False，得到是一个列表
# 如果指定为True，会将列表打开，变成多列，变成DATAFrame
# 列名则是按照0 1 2 3····的顺序，并且默认None值分隔后还是为None

print(df["attack"].str.split("远", expand=True))
"""
      0     1
0   近距离  None
1          距离
2   近距离  None
3     中    距离
4          距离
5  None  None
"""
# 显然并不是每一个字段分隔之后的数量都是一致的
# 不够就用None值补充。索引为4的地方不是None，是因为原来内容是"远距离"
# 按照"远"分隔之后，为空字符串

print(df["attack"].str.split("蛤", expand=True))
"""
      0
0   近距离
1   远距离
2   近距离
3  中远距离
4   远距离
5  None
"""
# 当分隔符不存在的时候，还是返回DataFrame
```

## 3. rsplit（和split用法一致，只不过默认是从右往左分隔）

## 4. partition（也是按照指定字符串分隔，和python内置的partition一样）

```python
print(df["attack"].str.partition("远"))
"""
      0     1     2
0   近距离            
1           远    距离
2   近距离            
3     中     远    距离
4           远    距离
5  None  None  None
"""
# partition只会分隔一次，会返回一个长度为3的元组
# 第一个元素：第一个分隔符之前的部分
# 第二个元素：分隔符本身
# 第三个元素：第一个分隔符之后的内容
# 对于"近距离":由于没有"远"这个字符，所以第一个元素就是其本身，第二个、第三个均为""
# 如果有多个分隔符，也只会按照第一个分隔符分隔
print("AaAaA".partition("a"))  # ('A', 'a', 'AaA')
# 并且注意到，和split不同，这个方法会自动变成DataFrame
print(df["attack"].str.partition("蛤"))
"""
      0     1     2
0   近距离            
1   远距离            
2   近距离            
3  中远距离            
4   远距离            
5  None  None  None
"""
# 即便当我指定一个不存在的分隔符也是一样，因为返回值就是一个包含三个元素的元组
```

## 5. rpartition（和partition类似，不过是默认是从右往左找到第一个分隔符）

```python
print(df["attack"].str.rpartition("远"))
"""
      0     1     2
0               近距离
1           远    距离
2               近距离
3     中     远    距离
4           远    距离
5  None  None  None
"""
# 可以看到对于存在分隔符的字段来说，或者None来说，是没区别的
# 但是如果没有分隔符的话，那么整体是位于name=2的列上面
# 可对于partition来说，不存在分隔符，则是位于name=0的列上面
```

## 6. get（获取指定位置的字符，只能获取1个）

```python
print(df["attack"].str.get(2))
"""
0       离
1       离
2       离
3       距
4       离
5    None
Name: attack, dtype: object
"""
# 获取指定索引的字符，只能传入int

print(df["attack"].str.get(3))
"""
0     NaN
1     NaN
2     NaN
3       离
4     NaN
5    None
Name: attack, dtype: object
"""
# 索引越界返回NaN

print(df["attack"].str.get(30))
"""
0   NaN
1   NaN
2   NaN
3   NaN
4   NaN
5   NaN
Name: attack, dtype: float64
"""
# 如果全部越界，那么None也为NaN，并且整体是float64类型
# 如果pandas用的时间比较长的话，一定会遇见该问题
# 像数据库、excel、csv等等，原来的类型明明为整型，但是读成DataFrame之后变成浮点型了
# 就是因为含有空值，变成float了。
# 这里多提一嘴
"""
如果是object类型(或者理解为str)，空值可以是None，也可以是NaN,但不可以是NaT
对于整型来说，如果含有空值，那么空值为NaN。
对于时间类型来说，如果含有空值，那么空值为NaT。
即使你想转化也是没用的，如果想把NaN或者NaT变成None，只有先变成object(str)类型，才可以转化
"""
```

## 7. slice（和python内置的slice一样。get相当于是[n],slice相当于是[m: n]）

```python
print(df["ultimate"].str.slice(0))
"""
0    聚合射线
1    战术目镜
2    死亡绽放
3    熔火核心
4    纳米激素
5    None
Name: ultimate, dtype: object
"""
# 指定一个值的话，相当于[m:]


print(df["ultimate"].str.slice(0, 3))
"""
0     聚合射
1     战术目
2     死亡绽
3     熔火核
4     纳米激
5    None
Name: ultimate, dtype: object
"""
# 指定两个值的话，相当于[m: n]

print(df["ultimate"].str.slice(0, 3, 2))
"""
0      聚射
1      战目
2      死绽
3      熔核
4      纳激
5    None
Name: ultimate, dtype: object
"""
# 指定三个值的话，相当于[m: n: step]

print(df["ultimate"].str.slice(5, 9, 2))
"""
0        
1        
2        
3        
4        
5    None
Name: ultimate, dtype: object
"""
# 索引越界，默认为空字符串，None还是None
```

## 8. slice_replace（从名字也能看出来，slice筛选出来之后替换）

```python
print(df["attack"].str.slice_replace(1,3, "distance"))
"""
0     近distance
1     远distance
2     近distance
3    中distance离
4     远distance
5          None
Name: attack, dtype: object
"""
# 将slice为[1:3]的内容换成"distance"，既然替换，所以这里不支持步长。
```

## 9. join（将每个字符之间使用指定字符相连，相当于sep.join(list(value))）

```python
print(df["ultimate"].str.join("a"))
"""
0    聚a合a射a线
1    战a术a目a镜
2    死a亡a绽a放
3    熔a火a核a心
4    纳a米a激a素
5       None
Name: ultimate, dtype: object
"""
```

## 10. contains（判断字符串是否含有指定子串，返回的是bool类型）

```python
print(df["country"].str.contains("国"))
"""
0    False
1     True
2     True
3    False
4    False
5     None
Name: country, dtype: object
"""
# 存在None值的话，整体还是object

print(df["country"].str.contains("国", na=False))
"""
0    False
1     True
2     True
3    False
4    False
5    False
Name: country, dtype: bool
"""
# 指定na=False，那么就会变成False了，当然也可以指定为其他的值，但是类型会变

print(df["country"].str.contains("国", na="嘎嘎"))
"""
0    False
1     True
2     True
3    False
4    False
5       嘎嘎
Name: country, dtype: object
"""
# 一般我们是为了进行删选，所以会指定为False
```

## 11. startswith（是否某个子串开头）

```python
print(df["attack"].str.startswith("近"))
"""
0     True
1    False
2     True
3    False
4    False
5     None
Name: attack, dtype: object
"""
```

## 12. endswith（判断是否以某个子串结尾）

```python
print(df["attack"].str.endswith("离"))
"""
0    True
1    True
2    True
3    True
4    True
5    None
Name: attack, dtype: object
"""
```

## 13. match（从头开始匹配的。返回布尔型，表示是否匹配给定的模式）

```python
print(df["attack"].str.match(".{2}距"))
"""
0    False
1    False
2    False
3     True
4    False
5     None
Name: attack, dtype: object
"""
# 开头两个字符任意，第三个字符为"距"
```

## 14. replace（替换指定的字符）

```python
# 我们来增加一列date
print(df["date"])
"""
0    2011-11-23
1    2011-11-23
2    2011-11-23
3    2011-11-23
4    2011-11-23
5    2011-11-23
Name: date, dtype: object
"""
# 将2011-11-23替换成23/11/2011这种格式

print(df["date"].str.replace("(\d+)-(\d+)-(\d+)", r"\3/\2/\1"))
"""
0    23/11/2011
1    23/11/2011
2    23/11/2011
3    23/11/2011
4    23/11/2011
5    23/11/2011
"""
# 这里面的replace是支持正则的。
# 并且一般我们会加上r表示原生的，这是在正则中
# 对于pandas来说，第一个参数是不需要加的，如match。但是第二个参数是要加上r的
# 尤其是分组替换，但如果只是简单字符串替换就不需要了。
```

## 15. repeat（重复字符串）

```python
print(df["date"].str.repeat(3))
"""
0    2011-11-232011-11-232011-11-23
1    2011-11-232011-11-232011-11-23
2    2011-11-232011-11-232011-11-23
3    2011-11-232011-11-232011-11-23
4    2011-11-232011-11-232011-11-23
5    2011-11-232011-11-232011-11-23
Name: date, dtype: object
"""
```

## 16. pad（将每一个元素都用指定的字符填充，只能是一个字符）

```python
print(df["name"].str.pad(5, fillchar=">"))
"""
0    >>莫伊拉
1    >士兵76
2    >>>死神
3    >>托比昂
4    >>>安娜
5    >>aaa
Name: name, dtype: object
"""
# 表示要占5个长度，用">"填充
# 但是我们发现是填在左边的

print(df["name"].str.pad(5, fillchar="<", side="right"))
"""
0    莫伊拉<<
1    士兵76<
2    死神<<<
3    托比昂<<
4    安娜<<<
5    aaa<<
Name: name, dtype: object
"""
# 指定side为right，会填在右边

print(df["name"].str.pad(5, fillchar="<", side="both"))
"""
0    <莫伊拉<
1    <士兵76
2    <<死神<
3    <托比昂<
4    <<安娜<
5    <aaa<
"""
# 指定side为both，会填在两端
```

## 17. zfill（填充，只能是0，从左边填充）

```python
print(df["name"].str.zfill(10))
"""
0    0000000莫伊拉
1    000000士兵76
2    00000000死神
3    0000000托比昂
4    00000000安娜
5    0000000aaa
Name: name, dtype: object
"""
```

## 18. encode decode（字符串编码、解码）

```python
print(df["attack"].str.encode("utf-8"))
"""
0              b'\xe8\xbf\x91\xe8\xb7\x9d\xe7\xa6\xbb'
1              b'\xe8\xbf\x9c\xe8\xb7\x9d\xe7\xa6\xbb'
2              b'\xe8\xbf\x91\xe8\xb7\x9d\xe7\xa6\xbb'
3    b'\xe4\xb8\xad\xe8\xbf\x9c\xe8\xb7\x9d\xe7\xa6...
4              b'\xe8\xbf\x9c\xe8\xb7\x9d\xe7\xa6\xbb'
5                                                 None
Name: attack, dtype: object
"""

print(df["attack"].str.encode("utf-8").str.decode("utf-8"))
"""
0     近距离
1     远距离
2     近距离
3    中远距离
4     远距离
5    None
Name: attack, dtype: object
"""
```

## 19. strip（按照指定内容，从两边去除，和python字符串内置的strip一样）

```python
print(df["attack"].str.strip("中远近离"))
"""
0       距
1       距
2       距
3       距
4       距
5    None
Name: attack, dtype: object
"""
```

## 20. translate（指定部分替换）

```python
trans = str.maketrans({"距": "ju", "离": "li"})
print(df["attack"].str.translate(trans))
"""
0     近juli
1     远juli
2     近juli
3    中远juli
4     远juli
5      None
Name: attack, dtype: object
"""
```

## 21. extract（分组捕获）

```python
print(df["date"].str.extract("\d{4}-(\d{2})-(\d{2})"))
"""
    0   1
0  11  23
1  11  23
2  11  23
3  11  23
4  11  23
5  11  23
"""
# 必须匹配指定pattern，否则为NaN
# 而且必须要有分组，否则报错，结果是一个DataFrame，每一个分组对应一列

print(df["date"].str.extract("\d{4}-(?P<月>\d{2})-(?P<日>\d{2})"))
"""
    月   日
0  11  23
1  11  23
2  11  23
3  11  23
4  11  23
5  11  23
"""
# 指定分组名，会变成列名
```

## 22. find（查找指定字符第一次出现的位置）

```python
print(df["date"].str.find("-"))
"""
0    4
1    4
2    4
3    4
4    4
5    4
Name: date, dtype: int64
"""

# 当然可以指定范围,包括起始和结束
print(df["date"].str.find("-", 5))
"""
0    7
1    7
2    7
3    7
4    7
5    7
Name: date, dtype: int64
"""

print(df["date"].str.find("蛤"))
"""
0   -1
1   -1
2   -1
3   -1
4   -1
5   -1
Name: date, dtype: int64
"""
# 找不到的话，返回-1
```
