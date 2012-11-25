<?xml version="1.0" encoding="UTF-8"?>
<web-app version="2.5" 
	xmlns="http://java.sun.com/xml/ns/javaee" 
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
	http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">

	{% for servlet in servlets %}
		<servlet>
			<description>This is the description of my J2EE component</description>
			<display-name>This is the display name of my J2EE component</display-name>
			<servlet-name>{{servlet.name}}</servlet-name>
			<servlet-class>{{servlet.path}}</servlet-class>
		</servlet>
	{% endfor %}
	{% for servlet in servlets %}
		<servlet-mapping>
			<servlet-name>{{servlet.name}}</servlet-name>
			<url-pattern>{{servlet.urlpath}}</url-pattern>
		</servlet-mapping>
	{% endfor %}

  <welcome-file-list>
    <welcome-file>index.jsp</welcome-file>
  </welcome-file-list>
</web-app>
