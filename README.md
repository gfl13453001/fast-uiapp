
# uiapp

**轻量级Android APP自动化测试框架、解决Android APP自动化测试环境配置及搭建复杂的问题、开箱即用的测试框架**


## 示例代码-1
```python

from uiapp import start

app = start()
app.run('com.example.jideailicense', 'com.example.jideailicense.MainActivity')

```
上述代码就是启动一个app的操作、首先启动start方法进行启动adb、run方法用于启动一个指定的APP。

后续考虑研究IOS自动化测试


