### 封装po

page/ 存放page页 app.py 存放app相关操作，打开，重启，关闭 case/ 存放测试用例

### 流程

1.创建PO 
2.编写测试用例，跑通业务流程，减少调试时间 
3.填充PO 业务内容，将每个页面需要倒入的包导入，把每个页面需要的driver传递过去。

### 封装BasePage的意义

page/ base_page.py base_page.py 可以存分初始化driver，封装find，find and click，find and send

### driver 的复用

每次去执行测试用例，都要初始化一次driver

希望：
- 如果driver存在，不为NONE，就复用这个driver
- 如果driver不存在，就重新创建一个新的driver
- 要在start（）完成