# bilibili_comment

该脚本能实现买房。

只需输入cookie(模拟登录）、up主的uid和评论即可。

因为直接登录比较麻烦，本来就是个简易脚本，因此采用cookie登录

获取cookie的方法：

先用浏览器登录一遍b站

再用浏览器打开：https://api.bilibili.com/x/v2/reply/add

然后调出开发者工具，chrome的快捷键是F12，其他浏览器度娘去。

然后刷新一下，找到名为add的，在里面找到Cookie，Cookie的内容就是所需要的。

如图所示： ![image](https://github.com/junhao69535/bilibili_comment/blob/master/cookie.png)
