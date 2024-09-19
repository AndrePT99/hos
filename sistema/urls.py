from django.contrib import admin
from django.urls import path
from modulos import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inicio/', views.inicio, name='inicio'),  # Inicio del dashboard
    path('catalogo', views.catalogos, name='catalogos'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.mostrar_carrito, name='mostrar_carrito'),
    path('eliminar-del-carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('actualizar-cantidad-carrito/<int:producto_id>/<str:accion>/', views.actualizar_cantidad_carrito, name='actualizar_cantidad_carrito'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('Cliente/registrado', views.clienteregistrado, name='cliente_registrado'),
    path('Ayuda', views.ayuda, name='ayuda'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('actualizar', views.actualizar_datos_cliente, name='actualizar_datos_cliente'),
    path('mis-compras/', views.listar_compras_cliente, name='listar_compras_cliente'),
    path('confirmacion/', views.confirmacion_compra, name='confirmacion_compra'),

    # cambiar contraseña    
    path('cambiar-contrasena/', auth_views.PasswordChangeView.as_view(
        template_name='clientes_pagina/cambiar_clave.html',
        success_url='/cambiar-contrasena-exito/'  # Redirigir después de cambiar la contraseña
    ), name='cambiar_contrasena'),
    path('cambiar-contrasena-exito/', auth_views.PasswordChangeDoneView.as_view(
        template_name='clientes_pagina/exito_clave.html'
    ), name='password_change_done'),

    # Restablecer contraseña 
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='clientes_pagina/password_reset_form.html',
        email_template_name='clientes_pagina/password_reset_email.html',
        subject_template_name='clientes_pagina/password_reset_subject.txt',
        success_url='/password-reset/done/'
    ), name='password_reset'),

    # URL que indica que el correo ha sido enviado
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='clientes_pagina/password_reset_done.html'
    ), name='password_reset_done'),

    # URL para el enlace de restablecimiento de contraseña enviado al correo
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='clientes_pagina/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    # URL que indica que la contraseña ha sido restablecida con éxito
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='clientes_pagina/password_reset_complete.html'
    ), name='password_reset_complete'),




    # Inventario/productos
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/crear_producto/', views.crear_producto, name='crear_producto'),
    path('inventario/editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('inventario/eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('inventario/crear_compraProducto/', views.crear_compraProducto, name='crear_compraProducto'),
    path('inventario/lista_compraProducto/', views.compraProducto, name='lista_compraProducto'),
    path('inventario/editar_compraProducto/<int:id>/', views.editar_compraProducto, name='editar_compraProducto'),
    path('inventario/eliminar_compraProducto/<int:id>/', views.eliminar_compraProducto, name='eliminar_compraProducto'),
    path('descargar_compraproductos/', views.descargar_compraproductos, name='descargar_compraproductos'),
    
    # inventario/insumo
    path('insumo/', views.insumo, name='insumo'),
    path('inventario/crear-insumo/', views.crear_insumo, name='crear_insumo'),
    path('insumo/editar/<int:id>/', views.editar_insumo, name='editar_insumo'),
    path('inventario/eliminar_insumo/<int:id>/', views.eliminar_insumo, name='eliminar_insumo'),
    path('inventario/crear_compraInsumo/', views.crear_compraInsumo, name='crear_compraInsumo'),
    path('inventario/lista_compraInsumo/', views.compraInsumo, name='lista_compraInsumo'),
    path('inventario/editar_compraInsumo/<int:id>/', views.editar_compraInsumo, name='editar_compraInsumo'),
    path('inventario/eliminar_compraInsumo/<int:id>/', views.eliminar_compraInsumo, name='eliminar_compraInsumo'),
    
    


    # Proveedores
    path('proveedor/', views.proveedor, name='proveedor'),
    path('proveedor/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedor/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),


    # Clientes
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/crear/', views.crear_clientes, name='crear_clientes'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_clientes'),
    path('clientes/eliminar/<int:id>/', views.eliminar_clientes, name='eliminar_clientes'),
    path('clientes/enviar_correo', views.enviar_correo, name='enviar_correo'),
    path('exito/', views.exito, name='exito'),

    # Ordenes de produccion
    path('produccion/', views.produccion, name='produccion'),
    path('produccion/crear/', views.crear_produccion, name='crear_produccion'),
    path('produccion/editar/<int:id>/', views.editar_produccion, name='editar_produccion'),
    path('produccion/eliminar/<int:id>/', views.eliminar_produccion, name='eliminar_produccion'),
    path('produccion/lista_gastoInsumo/', views.gastoInsumo, name='lista_gastoInsumo'),
    path('produccion/crear_gastoInsumo/', views.crear_gastoInsumo, name='crear_gastoInsumo'),
    path('produccion/editar_gastoInsumo/<int:id>/', views.editar_gastoInsumo, name='editar_gastoInsumo'),
    path('produccion/eliminar_gastoInsumo/<int:id>/', views.eliminar_gastoInsumo, name='eliminar_gastoInsumo'),

    # Ventas
    path('ventas/', views.ventas, name='ventas'),
    path('ventas/anular/<int:venta_id>/', views.anular_venta, name='anular_venta'),
    path('resumen_ventas/', views.resumen_ventas, name='resumen_ventas'),
    path('ventas/verificar_cliente/', views.verifica_cliente, name='verificar_cliente'),
    path('crear-venta/<int:cliente_id>/', views.crear_venta, name='crear_venta'),
    path('obtener-precio-producto/<int:producto_id>/', views.obtener_precio_producto, name='obtener_precio_producto'),


    # Login
    path('login/', views.log, name='login'),  # este es el login de santiago
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('registro_cliente/', views.registro_cliente, name='registro_cliente'),
    path('registro_cliente/', views.asociar_cuenta_cliente, name='asociar_cuenta_cliente'),

    # Selección de clientes para correos
    path('clientes/seleccionar/', views.seleccionar_clientes_correo, name='seleccionar_clientes_correo'),
    path('clientes/enviar-correo/<str:correos>/', views.formulario_enviar_correo, name='formulario_enviar_correo'),
    path('clientes/enviar-correo/', views.formulario_enviar_correo, name='formulario_enviar_correo_sin_seleccion'),

    # Descargas
    path('exportar_clientes_excel/', views.exportar_clientes_excel, name='exportar_clientes_excel'),
    path('exportar_productos/', views.exportar_productos, name='exportar_productos'),
    path('exportar_insumos/', views.exportar_insumos, name='exportar_insumos'),
    path('exportar_compras_insumos/', views.exportar_compras_insumo, name='exportar_compras_insumos'),
    path('exportar_compras_productos/', views.exportar_compras_productos, name='exportar_compras_productos'),
    path('exportar_produccion/', views.exportar_produccion, name='exportar_produccion'),
    path('exportar_gasto_insumos/', views.exportar_gasto_insumos, name='exportar_gasto_insumos'),
    path('exportar_ventas/', views.exportar_ventas, name='exportar_ventas'),
    path('exportar_proveedores/', views.exportar_proveedores, name='exportar_proveedores'),

    # Graficos

    path('ventas/graficos', views.dashboard_view, name='graficos_ventas'),

    # panel de control / usaurios
    path('panel/lista_usuarios', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('admin-cambiar-contrasena/', auth_views.PasswordChangeView.as_view(
        template_name='panel/cambiar_contrasena.html',
        success_url='/admin-cambiar-contrasena-exito/'  # Redirige después del éxito
    ), name='admin_cambiar_contrasena'),

    path('admin-cambiar-contrasena-exito/', auth_views.PasswordChangeDoneView.as_view(
        template_name='panel/cambiar_contrasena_exito.html'
    ), name='admin_password_change_done'),

    # Dtalle venta de campana
    path('venta/detalle/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),






    


]

# Solo incluir estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)