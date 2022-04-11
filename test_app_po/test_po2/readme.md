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
- 要在start（）方法中实现driver的复用
- 首先：要在base_page.py里面给driver一个初始值为none

### 打印日志
1、首先创建 conftest.py定义日志的文件名和级别
2、pytest.ini
### 多设备并发执行
- Android1 --- appium server 4723 
- Android2 --- appium server 4725 间隔一个端口，一台设备需要两个端口

### 设置udid

- udid 是测试多台设备的唯一标识
- 代码为 udid = os.getenv('udid')
        port = os.getenv('port')
- 执行（命令行执行）
  mac/linux
   udid = "192.168.57.103:5555" port=4723 pytest test_contact.py
   udid = "emulator-5554" port=4725 pytest test_contact.py
  windows
  第一台设备：
   set udid = "192.168.57.103:5555" port=4723 回车
   pytest test_contact.py
  第二台设备：
   set udid = "emulator-5554" port=4725 回车
   pytest test_contact.py

