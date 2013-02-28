<div class="tab">
	<ul class="ui-widget">
		{% for item in tabs %}
			<li ><a href="#{{item.tab_id_name}}"><span class="span_frame">{{item.tab_title_name}}</span></a></li>
		{% endfor %}
	</ul>
	{% for item in tabs %}
		<div id="{{item.tab_id_name}}" class="demo-config-menu">
			{{item.tab_contenxt_id}}
		</div>
	{% endfor %}
</div>