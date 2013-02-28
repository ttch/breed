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
<script src="jscom/m_init.js"></script>
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
		
			<li ><a href="#remote_return_tab"><span class="span_frame">平台返回</span></a></li>
		
	</ul>
	
		<div id="local_tab" class="demo-config-menu">
			<div class="box">
<input id="Test_Button" name="Test_Button" color=""  type="button" value="测试切换Button"/><div class="box"><span class="span_frame">
<label  for="CarMark"><font color="">(*)车牌号</font></label>
<input id="CarMark" name="CarMark"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="VIN"><font color="">(*)VIN码/车辆识别码</font></label>
<input id="VIN" name="VIN"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="EngineNo"><font color="">(*)发动机号</font></label>
<input id="EngineNo" name="EngineNo"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="Model"><font color="">(*)车辆型号</font></label>
<input id="Model" name="Model"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="VehicleType"><font color="">(*)号牌种类</font></label>
<select id="VehicleType" name="VehicleType">
			
</select>
</span><span class="span_frame">
<label  for="NoLicenseFlag"><font color="">(*)未上牌车辆标志</font></label>
<select id="NoLicenseFlag" name="NoLicenseFlag">
			
</select>
</span></div><div class="box"><span class="span_frame">
<label  for="NewVehicleFlag"><font color="">(*)新车标志</font></label>
<select id="NewVehicleFlag" name="NewVehicleFlag">
			
</select>
</span><span class="span_frame">
<label  for="ChgOwnerFlag"><font color="">(*)过户车辆标志</font></label>
<select id="ChgOwnerFlag" name="ChgOwnerFlag">
			
</select>
</span><span class="span_frame">
<label  for="EcdemicVehicleFlag"><font color="">(*)外地车标志</font></label>
<select id="EcdemicVehicleFlag" name="EcdemicVehicleFlag">
			
</select>
</span></div><div class="box"><span class="span_frame">
<label  for="LoanVehicleFlag"><font color="">(*)是否车贷投保多年标志</font></label>
<select id="LoanVehicleFlag" name="LoanVehicleFlag">
			
</select>
</span><span class="span_frame">
<label  for="FleetFlag"><font color="">(*)车队标志</font></label>
<select id="FleetFlag" name="FleetFlag">
			
</select>
</span><span class="span_frame">
<label  for="PrtBrand"><font color="">(*)打印车型名称</font></label>
<input id="PrtBrand" name="PrtBrand"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="AreaFlag"><font color="">(*)地区标识</font></label>
<select id="AreaFlag" name="AreaFlag">
			
</select>
</span><span class="span_frame">
<label  for="ProducerCode"><font color="">(*)销售渠道代码</font></label>
<select id="ProducerCode" name="ProducerCode">
			
</select>
</span><span class="span_frame">
<label  for="VehicleOwnerName"><font color="">(*)车主名称</font></label>
<input id="VehicleOwnerName" name="VehicleOwnerName"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="BaseCarValue"><font color="red">(*)实际价值</font></label>
<input id="BaseCarValue" name="BaseCarValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="NewCarValue"><font color="red">(*)新车购置价格</font></label>
<input id="NewCarValue" name="NewCarValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="AplName"><font color="">(*)投保人姓名</font></label>
<input id="AplName" name="AplName"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="IsdName"><font color="">(*)被保人姓名</font></label>
<input id="IsdName" name="IsdName"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="GlassFlag"><font color="">玻璃属性</font></label>
<select id="GlassFlag" name="GlassFlag">
			
</select>
</span><div class="box"><span class="span_frame">
<label  for="ClaimAdjustValue"><font color="red">(*)无赔优调整系数</font></label>
<input id="ClaimAdjustValue" name="ClaimAdjustValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="ClaimAdjustReason"><font color="red">(*)无赔优浮动原因代码</font></label>
<select id="ClaimAdjustReason" name="ClaimAdjustReason">
			
</select>
</span><span class="span_frame">
<label  for="NoClaimAdjustReason"><font color="red">无赔优不浮动原因代码</font></label>
<select id="NoClaimAdjustReason" name="NoClaimAdjustReason">
			
</select>
</span></div><div class="box"><span class="span_frame">
<label  for="IsContinuousPolicy"><font color="red">续保标志</font></label>
<select id="IsContinuousPolicy" name="IsContinuousPolicy">
			
</select>
</span><span class="span_frame">
<label  for="LoyaltyAdjustValue"><font color="red">(*)客户忠诚度调整系数</font></label>
<input id="LoyaltyAdjustValue" name="LoyaltyAdjustValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="LoyaltyAdjustReason"><font color="red">客户忠诚度浮动原因代码</font></label>
<select id="LoyaltyAdjustReason" name="LoyaltyAdjustReason">
			
</select>
</span></div><div class="box"><span class="span_frame">
<label  for="NoLoyaltyAdjustReason"><font color="red">客户忠诚度不浮动原因代码</font></label>
<select id="NoLoyaltyAdjustReason" name="NoLoyaltyAdjustReason">
			
</select>
</span><span class="span_frame">
<label  for="MileageAdjustValue"><font color="">行驶里程调整系数</font></label>
<input id="MileageAdjustValue" name="MileageAdjustValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="MileageAdjustReason"><font color="">行驶里程浮动原因</font></label>
<input id="MileageAdjustReason" name="MileageAdjustReason"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="PeccancyAdjustValue"><font color="">违法调整系数</font></label>
<input id="PeccancyAdjustValue" name="PeccancyAdjustValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="PeccancyAdjustReason"><font color="">违法浮动原因</font></label>
<input id="PeccancyAdjustReason" name="PeccancyAdjustReason"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="TravelAdjustValue"><font color="">约定行驶区调整系数</font></label>
<input id="TravelAdjustValue" name="TravelAdjustValue"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="TravelAdjustReason"><font color="">约定行驶区浮动原因</font></label>
<input id="TravelAdjustReason" name="TravelAdjustReason"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="DriverAdjustValue"><font color="">指定驾驶人调整系数</font></label>
<input id="DriverAdjustValue" name="DriverAdjustValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="DriverAdjustReason"><font color="">指定驾驶人浮动原因</font></label>
<input id="DriverAdjustReason" name="DriverAdjustReason"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="LossAdjustValue"><font color="">车辆损失险车型系数</font></label>
<input id="LossAdjustValue" name="LossAdjustValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="TheftAdjustValue"><font color="">盗抢险车型系数</font></label>
<input id="TheftAdjustValue" name="TheftAdjustValue"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="FleetAdjustValue"><font color="">车队调整系数</font></label>
<input id="FleetAdjustValue" name="FleetAdjustValue"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="AdjustValueReason"><font color="">车队浮动原因</font></label>
<input id="AdjustValueReason" name="AdjustValueReason"  type="text" maxlength="50" value=""/>
</span><div class="box"><span class="span_frame">
<label  for="RePolicyNo"><font color="red">重复投保保单号</font></label>
<input id="RePolicyNo" name="RePolicyNo"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="InsurerCode"><font color="red">保险公司代码</font></label>
<select id="InsurerCode" name="InsurerCode">
			
</select>
</span><span class="span_frame">
<label  for="LicensePlateNo"><font color="red">号牌号码</font></label>
<input id="LicensePlateNo" name="LicensePlateNo"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="LicensePlateType"><font color="red">号牌种类代码</font></label>
<select id="LicensePlateType" name="LicensePlateType">
			
</select>
</span><span class="span_frame">
<label  for="LicensePlateColorCode"><font color="red">号牌底色</font></label>
<select id="LicensePlateColorCode" name="LicensePlateColorCode">
			
</select>
</span><span class="span_frame">
<label  for="ReturnVIN"><font color="red">车辆识别代号</font></label>
<input id="ReturnVIN" name="ReturnVIN"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="ReturnEngineNo"><font color="red">发动机号</font></label>
<input id="ReturnEngineNo" name="ReturnEngineNo"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="EffectiveDate"><font color="red">起保日期</font></label>
<input id="EffectiveDate" name="EffectiveDate"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="ExpireDate"><font color="red">终保日期</font></label>
<input id="ExpireDate" name="ExpireDate"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="BillDate"><font color="red">签单日期</font></label>
<input id="BillDate" name="BillDate"  type="text" maxlength="50" value=""/>
</span><div class="box"><span class="span_frame">
<label  for="ThreeAmount"><font color="">三者保额</font></label>
<select id="ThreeAmount" name="ThreeAmount">
			
</select>
</span><span class="span_frame">
<label  for="DHA0004_Amount"><font color="">新增设备损失险保额</font></label>
<input id="DHA0004_Amount" name="DHA0004_Amount"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="DHA0005_DAY"><font color="">营运车辆停驶损失险最高赔偿天数</font></label>
<input id="DHA0005_DAY" name="DHA0005_DAY"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="DHA0005_Amount"><font color="">营运车辆停驶损失险日赔偿金额</font></label>
<input id="DHA0005_Amount" name="DHA0005_Amount"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="DHA0022_DAY"><font color="">机动车全损代步费用险最高赔偿天数</font></label>
<input id="DHA0022_DAY" name="DHA0022_DAY"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="DHA0022_Amount"><font color="">机动车全损代步费用险日赔偿金额</font></label>
<input id="DHA0022_Amount" name="DHA0022_Amount"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="DHA0032_Amount"><font color="">车身划痕损失险保额</font></label>
<select id="DHA0032_Amount" name="DHA0032_Amount">
			
</select>
</span><span class="span_frame">
<label  for="DHA0040_Amount"><font color="">车上人员责任险（驾驶员）每座限额</font></label>
<input id="DHA0040_Amount" name="DHA0040_Amount"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="DHA0041_Amount"><font color="">车上人员责任险（乘客）每座限额</font></label>
<input id="DHA0041_Amount" name="DHA0041_Amount"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="DHA0012_Amount"><font color="">车上货物责任险保额</font></label>
<input id="DHA0012_Amount" name="DHA0012_Amount"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="FreeCharge"><font color="">车损免赔额</font></label>
<select id="FreeCharge" name="FreeCharge">
			
</select>
</span><span class="span_frame">
<label  for="RatedPassengerCapacity"><font color="">核定载客人数</font></label>
<input id="RatedPassengerCapacity" name="RatedPassengerCapacity"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="DHA0014_Amount"><font color="">精神损害责任赔偿责任特约险保额</font></label>
<input id="DHA0014_Amount" name="DHA0014_Amount"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="CarCountry"><font color="">车辆类型</font></label>
<select id="CarCountry" name="CarCountry">
			
</select>
</span><span class="span_frame">
<label  for="DHA0035_DriftProportion"><font color="">专修厂特约条款浮动率</font></label>
<input id="DHA0035_DriftProportion" name="DHA0035_DriftProportion"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="Total_Prm"><font color="red">总保费</font></label>
<input id="Total_Prm" name="Total_Prm"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="Total_Amount"><font color="red">总保额</font></label>
<input id="Total_Amount" name="Total_Amount"  type="text" maxlength="50" value=""/>
</span>
		</div>
	
		<div id="remote_return_tab" class="demo-config-menu">
			<div class="box"><span class="span_frame">
<label  for="QuerySequenceNo"><font color="red">投保查询码</font></label>
<input id="QuerySequenceNo" name="QuerySequenceNo"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="QueryPastDate"><font color="red">查询码有效止期</font></label>
<input id="QueryPastDate" name="QueryPastDate"  type="text" maxlength="50" value=""/>
</span><span class="span_frame">
<label  for="LastProducerCode"><font color="red">销售渠道代码</font></label>
<input id="LastProducerCode" name="LastProducerCode"  type="text" maxlength="50" value=""/>
</span></div><div class="box"><span class="span_frame">
<label  for="RiskWarningType"><font color="red">风险警示类型</font></label>
<select id="RiskWarningType" name="RiskWarningType">
			
</select>
</span>
		</div>
	
</div></body>
</html>