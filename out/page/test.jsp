<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
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
<script src="jscom/page2_init.js"></script>
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
<body id="car_body" class="demo" background="images/bg.gif"><div class="tab">
	<ul class="ui-widget">
		
			<li ><a href="#local_tab"><span class="span_frame">本地面板</span></a></li>
		
	</ul>
	
		<div id="local_tab" class="demo-config-menu">
			<div class="box"><span class="span_frame">
<label  for="AplName"><font color="">(*)姓名</font></label>
<input id="AplName" name="AplName"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="ID"><font color="">(*)身份证</font></label>
<input id="ID" name="ID"  type="text" maxlength="50" value=""/>
</span><div class="box"><span class="span_frame">
<label  for="AplDate"><font color="">(*)投保日期</font></label>
<input id="AplDate" name="AplDate"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="StartDate"><font color="">(*)起保日期</font></label>
<input id="StartDate" name="StartDate"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="EndDate"><font color="">(*)终止日期</font></label>
<input id="EndDate" name="EndDate"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="SalesOrigin"><font color="">(*)业务来源</font></label>
<select id="SalesOrigin" name="SalesOrigin">
			
</select>
</span><span class="span_frame">
<label  for="PayType"><font color="">(*)付费约定</font></label>
<select id="PayType" name="PayType">
			
</select>
</span><span class="span_frame">
<label  for="ShortRateType"><font color="">(*)计费方式</font></label>
<select id="ShortRateType" name="ShortRateType">
			
</select>
</span></div><div class="box"><span class="span_frame">
<label  for="ShortPercent"><font color="">(*)短期费率</font></label>
<input id="ShortPercent" name="ShortPercent"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="Examinant"><font color="">(*)审批人</font></label>
<select id="Examinant" name="Examinant">
			
</select>
</span><span class="span_frame">
<label  for="SaleOfficeNo"><font color="">(*)销售网点</font></label>
<select id="SaleOfficeNo" name="SaleOfficeNo">
			
</select>
</span></div><div class="box"><span class="span_frame">
<label  for="SalesNo"><font color="">(*)销售员</font></label>
<select id="SalesNo" name="SalesNo">
			
</select>
</span><span class="span_frame">
<label  for="AgentNo"><font color="">(*)代理点</font></label>
<select id="AgentNo" name="AgentNo">
			
</select>
</span><span class="span_frame">
<label  for="SettleType"><font color="">(*)争议处理方式</font></label>
<select id="SettleType" name="SettleType">
			
</select>
</span></div><div class="box"><span class="span_frame">
<label  for="Arbitrator"><font color="">(*)仲裁机关</font></label>
<input id="Arbitrator" name="Arbitrator"  type="text" maxlength="50" value=""/>
</span>
		</div>
	
</div></body>
</html>