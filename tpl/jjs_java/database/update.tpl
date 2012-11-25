0023:.:0:3:14=48041e4b:16=47d21313:0037:htmlhead_begin.tpl:095A:1:14=4E964555:16=47d21313:<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="application/x-www-form-urlencoded; charset=UTF-8"/>
<base href="<%=basePath%>">
<title>test_page</title>

<link rel="stylesheet" href="themes/smoothness/jquery.ui.all.css">
<link type="text/css" href="css/all.css" rel="stylesheet" />
<link type="text/css" href="css/test01.css" rel="stylesheet" />
 <link type="text/css" href="css/menu.css" rel="stylesheet" />
<script src="jslib/json2.js"></script>
<script src="jslib/jquery-1.4.4.js" type="text/javascript"></script>
<script src="jslib/jquery.form.js" type="text/javascript"></script>

<script src="ui/jquery.ui.core.js"></script>
<script src="ui/jquery.ui.widget.js"></script>
<script src="ui/jquery.ui.mouse.js"></script>
<script src="ui/jquery.ui.button.js"></script>
<script src="ui/jquery.ui.draggable.js"></script>
<script src="ui/jquery.ui.position.js"></script>
<script src="ui/jquery.ui.resizable.js"></script>
<script src="ui/jquery.ui.dialog.js"></script>
<script src="ui/jquery.effects.core.js"></script>
<script src="ui/jquery.ui.slider.js"></script>
<script src="ui/jquery.ui.tabs.js"></script>
<script src="ui/jquery.ui.autocomplete.js"></script>
<script src="ui/jquery.ui.datepicker.js"></script>
<script src="ui/i18n/jquery.ui.datepicker-zh-CN.js"></script>
<script src="jslib/jquery.jqGrid.min.js" type="text/javascript"></script>
<script src="ui/jquery.ui.combobox.js"></script>
<script src="ui/jquery.ui.float.js"></script>
<script src="ui/jquery.ui.int.js"></script>
{{js__init}}
	<style>
	.ui-button-icon-only .ui-button-text { padding: 1px; }
	.ui-autocomplete {
		max-height: 200px;
		overflow-y: auto;
		/* prevent horizontal scrollbar */
		overflow-x: auto;
		/* add padding to account for vertical scrollbar */
		padding-right: 60;
		max-width : 300px;
	}
	/* IE 6 doesn't support max-height
	 * we use height instead, but this forces the menu to always be this tall
	 */
	* html .ui-autocomplete {
		height: 200px;
		width : 300px;
	}
	</style>
</head>
<body id="car_body" class="demo" background="images/bg.gif">
0033:html_head:000000000:2:14=48041e4b:16=47d21313:002E:.svn:000000000:2:14=48041e4b:16=47d21313:002B:entries:0C8:1:14=4F7012D8:16=47d21313:10

dir
1
file:///D:/svnroot/bread_orice/tpl/jjs_java/html_head
file:///D:/svnroot/bread_orice



2012-03-26T06:55:13.625000Z
1
User














78588dc2-8c91-0e4d-a47b-161f8822bfad

stander
dir

0033:prop-base:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:002F:props:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0033:text-base:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:002D:tmp:000000000:2:14=48041e4b:16=47d21313:0033:prop-base:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:002F:props:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0033:text-base:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0031:stander:000000000:2:14=48041e4b:16=47d21313:002E:.svn:000000000:2:14=48041e4b:16=47d21313:002C:entries:030D:1:14=4F7012D8:16=47d21313:10

dir
1
file:///D:/svnroot/bread_orice/tpl/jjs_java/html_head/stander
file:///D:/svnroot/bread_orice



2012-03-26T06:55:13.625000Z
1
User














78588dc2-8c91-0e4d-a47b-161f8822bfad

css_import.tpl
file




2011-09-15T16:01:30.593750Z
736ed7b94a25c0e663d3cb869d9d176e
2012-03-26T06:55:13.625000Z
1
User





















256

html_include.tpl
file




2011-09-15T16:03:05.953125Z
ea96c9c481fff591b10c0889a049b48d
2012-03-26T06:55:13.625000Z
1
User





















231

css_in.tpl
file




2011-09-15T16:02:05.031250Z
9a3b16dbe9dfff84a483980fa9a42505
2012-03-26T06:55:13.625000Z
1
User





















472

js_include.tpl
file




2011-09-18T16:47:43.968750Z
312a8eeb699efd5c7fae5ff6eb9ce3b6
2012-03-26T06:55:13.625000Z
1
User





















1005

0033:prop-base:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:002F:props:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0033:text-base:000000000:2:14=48041e4b:16=47d21313:003C:css_import.tpl.svn-base:0100:1:14=4F7012CE:16=47d21313:<link rel="stylesheet" href="themes/smoothness/jquery.ui.all.css">
<link type="text/css" href="css/all.css" rel="stylesheet" />
<link type="text/css" href="css/test01.css" rel="stylesheet" />
<link type="text/css" href="css/menu.css" rel="stylesheet" />0038:css_in.tpl.svn-base:01D8:1:14=4F7012CC:16=47d21313:<style>
.ui-button-icon-only .ui-button-text { padding: 1px; }
.ui-autocomplete {
	max-height: 200px;
	overflow-y: auto;
	/* prevent horizontal scrollbar */
	overflow-x: auto;
	/* add padding to account for vertical scrollbar */
	padding-right: 60;
	max-width : 300px;
}
/* IE 6 doesn't support max-height
 * we use height instead, but this forces the menu to always be this tall
 */
* html .ui-autocomplete {
	height: 200px;
	width : 300px;
}
</style>
003D:html_include.tpl.svn-base:0E7:1:14=4F7012CE:16=47d21313:<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="application/x-www-form-urlencoded; charset={{html_encoding}}"/>
{{base_path}}
<title>{{html_titls}}</title>003C:js_include.tpl.svn-base:03ED:1:14=4F7012CE:16=47d21313:<script src="jslib/json2.js"></script>
<script src="jslib/jquery-1.4.4.js" type="text/javascript"></script>
<script src="jslib/jquery.form.js" type="text/javascript"></script>
<script src="ui/jquery.ui.core.js"></script>
<script src="ui/jquery.ui.widget.js"></script>
<script src="ui/jquery.ui.mouse.js"></script>
<script src="ui/jquery.ui.draggable.js"></script>
<script src="ui/jquery.ui.position.js"></script>
<script src="ui/jquery.ui.resizable.js"></script>
<script src="ui/jquery.effects.core.js"></script>
<script src="ui/jquery.ui.slider.js"></script>
<script src="ui/jquery.ui.button.js"></script>
<script src="ui/jquery.ui.dialog.js"></script>
<script src="ui/jquery.ui.tabs.js"></script>
<script src="ui/jquery.ui.datepicker.js"></script>
<script src="ui/i18n/jquery.ui.datepicker-zh-CN.js"></script>
<script src="jslib/jquery.jqGrid.min.js" type="text/javascript"></script>
<script src="ui/jquery.ui.combobox.js"></script>
<script src="ui/jquery.ui.autocomplete.js"></script>0023:.:0:3:14=48041e4b:16=47d21313:002D:tmp:000000000:2:14=48041e4b:16=47d21313:0033:prop-base:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:002F:props:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0033:text-base:000000000:2:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0023:.:0:3:14=48041e4b:16=47d21313:0033:css_import.tpl:0100:1:14=4E72215C:16=47d21313:<link rel="stylesheet" href="themes/smoothness/jquery.ui.all.css">
<link type="text/css" href="css/all.css" rel="stylesheet" />
<link type="text/css" href="css/test01.css" rel="stylesheet" />
<link type="text/css" href="css/menu.css" rel="stylesheet" />002F:css_in.tpl:01D8:1:14=4E72217E:16=47d21313:<style>
.ui-button-icon-only .ui-button-text { padding: 1px; }
.ui-autocomplete {
	max-height: 200p