#breed工具使用说明


##javatobreed

>简介 ： 

这个工具本身就是帮助你构建一个java的解析框架，他会提供一个基于python ply的bnf语法框架。你可以在这样的框架里对具体的你敢兴趣的结构进行归类整理生成结构，然后解析转换成其他语言，当然你也可以用他做点其他的。比如比CTag更好的深度分析工具，当然有了这个东西实现起来并不难了。


>关于为什么取名叫javatobreed 

我肯定会改。因为这个暂时是我的私有工具，回头我会把他隔离开来，并提供一些数据结构和算法来减少您的工作量，当然不是最好，总比没有好。

> 如何使用?

安装python，装上ply，你可以就可以调用了。

>输入 python main.py --help或者python main.py --version

输出如下：

	java parser v0.0.1
	author by zhao_nf
	command line is main.py -shortoptions args
	example : python main.py --file $HOME/project/xxxx.java

>输入python main.py --file /home/zhao_nf/xxx.java

就分析对应的文件。


good luck ！祝使用愉快

有什么问题随时发送到ttchgm@gmail.com

