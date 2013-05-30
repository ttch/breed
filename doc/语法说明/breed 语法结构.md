
# breed Rational Application Develop V0.1

@ author by zhao_nf(ttchgm@gmail.com)

## 1 系统说明

###1.1 系统开发环境

系统采用 python 开发,模版规则引擎采用 jinja2,文档生成器采用自定义开发。


##1.2 系统定位

这版的系统代号为 breed,意喻繁殖,属于 Rational Application Develop 工具类型,这 个开发工具没有 IDE,为了减少开发难度而没有做 IDE 和控件拖拽,从某种意义上 IDE 是会 降低开发效率,增加开发友好度。但为了这个豪华的表现层付出了非常昂贵的代价不是非 常值当。
暂时 0.1 版本只支持java的转换工作。


##1.3 系统的运作方式

系统采用流水线方式工作。

首先使用javaparser转换代码，javaparser v0.2提供了一份文法解析。

> todo : 提供一套灵活的解析的结构
> 
> 支持定义与breed语言结构相同的部分的转换。

## 1.4 系统层级结构

系统主要功能实现:
`转换程序(translate)`:支持部分 java 的 SSH 框架中部分业务定义和业务逻辑代码到breed 语言的语法。`分析程序(Parser)`:分析 breed 程序,生一个 breed 词法集合文件。`生成程序(Make)`:根据词法集合文件,分析出要生成的源格式(注意这个格式不是源代码) 

`模板库(template)`:可以让用户根据源格式自定义一套自己的工作环境的对应的生产模版库,以便生成最终代码。
系统分为两种模式运作:
`机器转换` : java 代码 ->Translate -> Parser ->Make ->template ->target code。`用户编写`  Breed 源代码 →Parser ->Make ->template ->target code。
## 1.5 java部分


### MVC模式

这种模式下，可以定义转换类到
# 2 系统架构
## 2.1 支持层面
数据结构(DataStruct)
	例子代码
		@define
		struct Person (){
			String CustomID;
			String CustomName;
			String Sex;
			Date Birthday;
			String PersonType;
			String PaperType;
			String PaperNo;
			String Tel;
			String Mobile;
			String Fax;
			String ZipCode;
			String Addr;
			String PostAddr;
			String UnitName;
			String UnitAddr;
			String UnitTel;
			String UnitZipCode;
		}
		@end	
页面(Page)
	@define
		field MainTable( extends : InputText)[
			fieldname : 'MainTable1';
			fieldTitle : '主table';
		];	@end
业务逻辑(Logic)
	logic{
		Person p;
		p.CustomID = "hello";
		p.Sex = "男";	}	关联(Assioc)
	@assioc	
	@end
检测(Check)

	check TypeInstance
持久化(Persistence)

>暂时未设计	
算法(Algorithm)
以上每个层都有可能是一个独立的语法集合。
## 2.2 通用语法
以下语法可能出现在数据结构，页面，关联
段定义	@define
		typeStatments	@end
---函数定义
	@function
		functionStatements	@end---


## 2.3 java 转换框架


转换成struct，首先定义一个


针对类型我们设定一个转换表

class interface enum 都可以转换成struct

其中的属性，如果是基础类型的直接声明。

如果类型是对象类型的，且不是业务model类型不做转换。
如果是业务model类型，可以进行转换


Persistence 可以根据指定



