<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <title>Home Page</title>
  </head>
  <body>
    <div id="content">
      <h1>Sistema de Gestión</h1>

      <p>Hola <%=request.getUserPrincipal().getName()%> <span>[
      <% if (request.isUserInRole("ROLE_GCFP")){%>
      GCFP
      <% } %>

      <% if (request.isUserInRole("ROLE_GCP")){%>
      GC
      <% } %>

      <% if (request.isUserInRole("ROLE_A")){%>
      A
      <% } %>

      <% if (request.isUserInRole("ROLE_AC")){%>
      AC
      <% } %>

      <% if (request.isUserInRole("ROLE_GNT")){%>
      GNT
      <% } %>
      ]</span>; este es el menu de la aplicación:
    </p>

    <h3>Módulo Ventas</h3></td>
    <p>
      <% if (request.isUserInRole("ROLE_GCFP")){ %>
      <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
      <% } else { %>
      <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
      <% } %>
      <a href="ventas/gestion_clientes.jsp">Operación: gestionar clientes</a></p>

      <p>
        <% if (request.isUserInRole("ROLE_GCFP") || request.isUserInRole("ROLE_A")){ %>
        <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
        <% } else { %>
        <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
        <% } %>
        <a href="ventas/gestion_presupuestos.jsp">Operación: gestionar presupuestos</a></p>

        <p>
          <% if (request.isUserInRole("ROLE_GCFP")){ %>
          <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
          <% } else { %>
          <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
          <% } %>
          <a href="ventas/gestion_facturas.jsp">Operación: gestionar facturas</a>
        </p>

        <h3>Módulo Compras</h3></td>
        <p>
          <% if (request.isUserInRole("ROLE_GCP") || request.isUserInRole("ROLE_A")){ %>
          <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
          <% } else { %>
          <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
          <% } %>
          <a href="compras/gestion_proveedores.jsp">Operación: gestionar proveedores</a>
        </p>

        <p>
          <% if (request.isUserInRole("ROLE_GCP")){ %>
          <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
          <% } else { %>
          <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
          <% } %>
          <a href="compras/gestion_compras.jsp">Operación: gestionar compras</a>
        </p>

        <p>
          <% if (request.isUserInRole("ROLE_AC")){ %>
          <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
          <% } else { %>
          <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
          <% } %>
          <a href="compras/autorizar_compras.jsp">Operación: autorizar compras</a>
        </p>


        <h3>Módulo Nóminas</h3></td>
        <p>
          <% if (request.isUserInRole("ROLE_GNT") || request.isUserInRole("ROLE_A")){ %>
          <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
          <% } else { %>
          <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
          <% } %>
          <a href="nominas/gestion_trabajadores.jsp">Operación: gestionar trabajadores</a>
        </p>
        <p>
          <% if (request.isUserInRole("ROLE_GNT")){ %>
          <img src='<%=response.encodeURL("../img/check.svg") %>' alt="granted" style="width:25px;height:25px">
          <% } else { %>
          <img src='<%=response.encodeURL("../img/times.svg") %>' alt="restricted" style="width:25px;height:25px">
          <% } %>
          <a href="nominas/gestion_nominas.jsp">Operación: gestionar nóminas</a>
        </p>

        <p><a href="../j_spring_security_logout">Logout</a></p>
      </div>
    </body>
  </html>
