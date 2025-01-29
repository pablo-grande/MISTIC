<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<html>
  <head>
      <meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <title>Home Page</title>
  </head>
<body>
<div id="content">
<h1>Sistema de Gestion</h1>

<p>Hola <%=request.getUserPrincipal().toString()%>; este es el menu de la aplicacion:</p>

<h3>Modulo Ventas</h3></td>
<p>
<% if (request.isUserInRole("GCFP")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="ventas/gestion_clientes.jsp">Operacion: gestionar clientes</a></p>

<p>
<% if (request.isUserInRole("GCFP") || request.isUserInRole("A")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="ventas/gestion_presupuestos.jsp">Operacion: gestionar presupuestos</a></p>

<p>
<% if (request.isUserInRole("GCFP")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="ventas/gestion_facturas.jsp">Operacion: gestionar facturas</a></p>

<h3>Modulo Compras</h3></td>
<p>
<% if (request.isUserInRole("GCP") || request.isUserInRole("A")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="compras/gestion_proveedores.jsp">Operacion: gestionar proveedores</a></p>

<p>
<% if (request.isUserInRole("GCP")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="compras/gestion_compras.jsp">Operacion: gestionar compras</a></p>

<p>
<% if (request.isUserInRole("AC")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="compras/autorizar_compras.jsp">Operacion: autorizar compras</a></p>


<h3>Modulo Nominas</h3></td>
<p>
<% if (request.isUserInRole("GNT") || request.isUserInRole("A")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="nominas/gestion_trabajadores.jsp">Operacion: gestionar trabajadores</a></p>
<p>
<% if (request.isUserInRole("GNT")){ %>
<img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
<% } else { %>
<img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
<% } %>
<a href="nominas/gestion_nominas.jsp">Operacion: gestionar nominas</a></p>

<a href='<%= response.encodeURL("../index.jsp?logoff=true") %>'>Logout</a>.

</body>
</html>
