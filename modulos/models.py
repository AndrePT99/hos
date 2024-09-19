# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Cliente(models.Model):
    idclientes = models.AutoField(db_column='idClientes', primary_key=True)  # Field name made lowercase.
    numerodocumento = models.CharField(db_column='numeroDocumento', max_length=45)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=2)  # Field name made lowercase.
    nombre1 = models.CharField(max_length=45)
    nombre2 = models.CharField(max_length=45, blank=True, null=True)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=300)
    correo1 = models.CharField(max_length=150)
    correo2 = models.CharField(max_length=150, blank=True, null=True)
    telefono1 = models.CharField(max_length=13)
    telefono2 = models.CharField(max_length=13, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    genero = models.CharField(max_length=9)
    password = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', null=True, blank=True)


    class Meta:
        db_table = 'cliente'


class Comprainsumo(models.Model):
    idcomprasinsumos = models.AutoField(db_column='idComprasInsumos', primary_key=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=10, decimal_places=0)  # Field name made lowercase.
    preciototal = models.DecimalField(db_column='precioTotal', max_digits=10, decimal_places=0)  # Field name made lowercase.
    fechacompra = models.DateTimeField(db_column='fechaCompra')  # Field name made lowercase.
    cantidad = models.IntegerField()
    insumo_idinsumos = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='insumo_idInsumos')  # Field name made lowercase.
    proveedor_idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_idProveedor')  # Field name made lowercase.

    class Meta:
        db_table = 'comprainsumo'


class Compraproducto(models.Model):
    idcomprasproductos = models.AutoField(db_column='idComprasproductos', primary_key=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=10, decimal_places=0)  # Field name made lowercase.
    preciototal = models.DecimalField(db_column='precioTotal', max_digits=10, decimal_places=0)  # Field name made lowercase.
    fechacompra = models.DateTimeField(db_column='fechaCompra')  # Field name made lowercase.
    cantidad = models.IntegerField()
    producto_idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_idProducto')  # Field name made lowercase.
    proveedor_idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_idProveedor')  # Field name made lowercase.

    class Meta:
        db_table = 'compraproducto'


class Controlgastoinsumo(models.Model):
    idcontrolgastoinsumo = models.AutoField(db_column='idControlGastoInsumo', primary_key=True)  # Field name made lowercase.
    fechauso = models.DateTimeField(db_column='fechaUso')  # Field name made lowercase.
    unidaddemedida = models.CharField(db_column='unidadDeMedida', max_length=11)  # Field name made lowercase.
    cantidad = models.IntegerField()
    comentarios = models.TextField()
    insumo_idinsumos = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='insumo_idInsumos')  # Field name made lowercase.
    ordendeproduccion_idordendeproduccion = models.ForeignKey('Ordendeproduccion', models.DO_NOTHING, db_column='ordenDeProduccion_idOrdenDeProduccion')  # Field name made lowercase.

    class Meta:
        db_table = 'controlgastoinsumo'




class Detalleventa(models.Model):
    iddetalleventa = models.AutoField(db_column='idDetalleVenta', primary_key=True)
    cantidad = models.IntegerField()
    producto_idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_idProducto')
    venta_idventas = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_idVentas')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Nuevo campo para el subtotal

    class Meta:
        db_table = 'detalleventa'
    
    def save(self, *args, **kwargs):
        # Calcular el subtotal cuando se guarda el detalle de la venta
        self.subtotal = self.cantidad * self.producto_idproducto.precio
        super().save(*args, **kwargs)





class Insumo(models.Model):
    idinsumos = models.AutoField(db_column='idInsumos', primary_key=True)
    codigo = models.CharField(max_length=10)
    nombreinsumo = models.CharField(db_column='nombreInsumo', max_length=150)  # Field name made lowercase.
    color = models.CharField(max_length=45)
    unidaddemedida = models.CharField(db_column='unidadDeMedida', max_length=11)  # Field name made lowercase.
    cantidad = models.DecimalField(max_digits=10, decimal_places=0)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro')  # Field name made lowercase.
    imageninsumo = models.ImageField(upload_to='imagenes_insumos/', db_column='imagenInsumo', blank=True, null=True)  # Field name made lowercase.
    dimension = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'insumo'


class Metododepago(models.Model):
    idmetododepago = models.AutoField(db_column='idMetodoDePago', primary_key=True)  # Field name made lowercase.
    metododepago = models.CharField(db_column='metodoDePago', max_length=15)  # Field name made lowercase.

    class Meta:
        db_table = 'metododepago'


class Ordendeproduccion(models.Model):
    idordendeproduccion = models.AutoField(db_column='idOrdenDeProduccion', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(max_length=11)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechafinalizacion = models.DateTimeField(db_column='fechaFinalizacion')  # Field name made lowercase.
    detalleventa_iddetalleventa = models.ForeignKey(Detalleventa, models.DO_NOTHING, db_column='detalleVenta_idDetalleVenta')  # Field name made lowercase.
    usuario_idusurios = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_idUsurios')  # Field name made lowercase.

    class Meta:
        db_table = 'ordendeproduccion'


class Privilegio(models.Model):
    idprivilegio = models.AutoField(db_column='idPrivilegio', primary_key=True)  # Field name made lowercase.
    nombreprivilegio = models.CharField(db_column='nombrePrivilegio', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'privilegio'


class Privilegiocliente(models.Model):
    idprilegiocliente = models.AutoField(db_column='idprilegioCliente', primary_key=True)  # Field name made lowercase.
    fechaasignacion = models.DateTimeField(db_column='fechaAsignacion')  # Field name made lowercase.
    cliente_idclientes = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_idClientes')  # Field name made lowercase.
    privilegio_idprivilegio = models.ForeignKey(Privilegio, models.DO_NOTHING, db_column='privilegio_idPrivilegio')  # Field name made lowercase.

    class Meta:
        db_table = 'privilegiocliente'


class Privilegiousuario(models.Model):
    idprivilegiosusuarios = models.AutoField(db_column='idPrivilegiosUsuarios', primary_key=True)  # Field name made lowercase.
    fechaasignacion = models.DateTimeField(db_column='fechaAsignacion')  # Field name made lowercase.
    usuario_idusurios = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_idUsurios')  # Field name made lowercase.
    privilegio_idprivilegio = models.ForeignKey(Privilegio, models.DO_NOTHING, db_column='privilegio_idPrivilegio')  # Field name made lowercase.

    class Meta:
        db_table = 'privilegiousuario'


from django.contrib.auth.models import User

class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)
    codigo = models.CharField(max_length=10)
    nombrecategoria = models.CharField(db_column='nombreCategoria', max_length=100)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='nombreProducto', max_length=100)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    calidad = models.CharField(max_length=7)
    dimension = models.CharField(max_length=2)
    color = models.CharField(max_length=45)
    observaciones = models.TextField()
    imagenproducto = models.ImageField(upload_to='imagenes_productos/', db_column='imagenProducto', blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(max_length=9)
    cantidad = models.IntegerField(default=0)
    usuario_idusurios = models.ForeignKey(User, on_delete=models.CASCADE, db_column='usuario_idUsurios')  # Field name made lowercase.

    class Meta:
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    tipoproveedor = models.CharField(db_column='tipoProveedor', max_length=8)  # Field name made lowercase.
    categoriaproveedor = models.CharField(db_column='categoriaProveedor', max_length=10)  # Field name made lowercase.
    direccion = models.CharField(max_length=500)
    sitioweb = models.CharField(db_column='sitioWeb', max_length=500, blank=True, null=True)  # Field name made lowercase.
    comentarios = models.TextField(blank=True, null=True)
    nombre1 = models.CharField(max_length=45)
    nombre2 = models.CharField(max_length=45, blank=True, null=True)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    nombreempresa = models.CharField(db_column='nombreEmpresa', max_length=100)  # Field name made lowercase.
    telefono1 = models.CharField(max_length=13)
    telefono2 = models.CharField(max_length=13, blank=True, null=True)
    correo1 = models.CharField(max_length=150)
    correo2 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'proveedor'


class Rol(models.Model):
    idrol = models.AutoField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    nombrerol = models.CharField(db_column='nombreRol', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'rol'


class Usuario(models.Model):
    idusurios = models.AutoField(db_column='idUsurios', primary_key=True)  # Field name made lowercase.
    numerodocumento = models.CharField(db_column='numeroDocumento', max_length=20)  # Field name made lowercase.
    tipodedocumento = models.CharField(db_column='tipodeDocumento', max_length=2)  # Field name made lowercase.
    primernombre = models.CharField(db_column='primerNombre', max_length=45)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    primeraprellido = models.CharField(db_column='primerAprellido', max_length=45)  # Field name made lowercase.
    segundoaprellido = models.CharField(db_column='segundoAprellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correo1 = models.CharField(max_length=100)
    correo2 = models.CharField(max_length=100, blank=True, null=True)
    telefono1 = models.CharField(max_length=13)
    rol_idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_idRol', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = 'usuario'





from django.db import models
import datetime

class Venta(models.Model):
    idventas = models.AutoField(db_column='idVentas', primary_key=True)  # Campo AutoField como clave primaria.
    valortotal = models.DecimalField(db_column='valorTotal', max_digits=10, decimal_places=0)  # Campo Decimal para el valor total.
    fechaventa = models.DateTimeField(db_column='fechaVenta')  # Fecha de la venta.
    modalidadventa = models.CharField(db_column='modalidadVenta', max_length=10)  # Modalidad de venta.
    cliente_idclientes = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_idClientes')  # Relación con el cliente.
    metododepago_idmetododepago = models.ForeignKey('Metododepago', models.DO_NOTHING, db_column='metodoDePago_idMetodoDePago')  # Relación con el método de pago.
    estado = models.CharField(max_length=10, default='activa')  # Estado de la venta, con valor por defecto 'activa'.
    numeroventa = models.CharField(max_length=20, unique=True, blank=True)  # Número de venta, generado automáticamente.

    # Sobrescribimos el método save para generar el número de venta automáticamente si no existe.
    def save(self, *args, **kwargs):
        if not self.numeroventa:  # Solo generamos el número de venta si no existe.
            self.numeroventa = self.generar_numero_venta()
        super().save(*args, **kwargs)

    # Método para generar el número de venta.
    def generar_numero_venta(self):
        current_year = datetime.datetime.now().year
        # Obtenemos la última venta del año actual para incrementar el número.
        ultimo_numero = Venta.objects.filter(numeroventa__startswith=f'VENTA-{current_year}').order_by('numeroventa').last()
        
        if ultimo_numero:
            # Extraemos el número de la venta anterior y lo incrementamos.
            ultimo_numero = int(ultimo_numero.numeroventa.split('-')[-1])
            nuevo_numero = ultimo_numero + 1
        else:
            nuevo_numero = 1  # Si no hay ventas previas en el año, comenzamos desde 1.
        
        # Retornamos el número de venta en el formato 'VENTA-AAAA-XXXX'.
        return f'VENTA-{current_year}-{str(nuevo_numero).zfill(4)}'

    class Meta:
        db_table = 'venta'  # Nombre de la tabla en la base de datos.

