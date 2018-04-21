# NuaaMoneyGone
通过南航校园卡消费充值查询接口生成个人账单记录与数据分析

## Step1:完善核心SDK-查询指定时间段内校园卡的消费情况与充值情况
### 使用方法：
1. **Clone代码，或者直接拷贝（反正代码很短）**
2.  **在原来的程序的main函数上修改，或者 import client.py这个文件，这取决于你的使用方式。**

_提醒：日期格式为 年份-月份-日期 例如：2018-04-03 且查询的间隔需要大于等于一个月_
_需要安装 requests库_

```python
    test = client(username='你的学号', password='身份证后六位')
    print(test.search(begin_data='起始日期', end_data='终止日期'))
```

 返回结果包含消费记录和充值距离 形式为JSON数组

### 20180421 update
1. 首先将JSON数据以可读形式输出，调用`getIn(data)`函数，可以输出在`data`所选日期范围内所有消费与充值记录，显示内容包括**地点、金额、消费类型**。
2. 其次输出所选日期范围内的消费与支出金额，分别调用`getSpendMonthly(data)`函数与`getChargeMonthly(data)`函数。
3. 为了之后使用Echart进行可视化，前期完成了根据不同年份，输入该年每月的消费与支出金额并保留一位小数。
4. 优化代码，修改`begin_data`与`end_data`为`begin_date`与`end_date`;防止在一个py文件中多次请求出现错误的问题，设置了`isLogin`变量。

## Step 2：清洗数据，挖掘有效信息
## Step 3：搭建Web服务，用Echart做前端对数据进行可视化优化


