drop table {{tbl_name}}
create table {{tbl_name}}(
			{% for item in options %}
				{{item.value}}
			{% endfor %}
);