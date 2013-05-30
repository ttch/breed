# logic 系统


##判断表达式


###语法
	
	conditionalOrExpression : ? expression => expression : expression
	| ? expression => expression

对，我们没有if else elseif这样的或者类似的关键字了。

如果你想写一个if ( expression) else ( expression )

现在你可以这样写 ? expression => expression : expression

>好吧，我们不提供switch和case了 你完全可以这样写

	? expression => (
		(? ?$ == "hello1" => ^r 1 )
		(? ?$ == "hello2" => ^r 2 )
		(? ?$ == "hello3" => ^r 3 )
	)


##遍历或者循环

###语法

	loopExpression : ^ expression => statement


如果你想遍历一个元素

	^ expression => (
		print ^$
	)



	break 等价于 ^b

	continue 等价于 ^c

	return 等价于 ^r
	^$取 expression返回值枚举对象的index







