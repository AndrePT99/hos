from django import forms
from .models import Proveedor, Cliente, Insumo, Producto, Ordendeproduccion, Detalleventa, Usuario, Venta, Detalleventa, Compraproducto, Comprainsumo, Controlgastoinsumo



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Usar el email como username
        if commit:
            user.save()
        return user





# Opciones para el tipo de proveedor
TIPO_PROVEEDOR_CHOICES = [
    ('Producto', 'Producto'),
    ('Insumo', 'Insumo'),
]

# Opciones para el tipo de documento
TIPO_DOCUMENTO_CHOICES = [
    ('CC', 'Cédula de Ciudadanía'),
    ('TI', 'Tarjeta de Identidad'),
    ('CE', 'Cédula de Extranjería'),
]

# Opciones para la unidad de medida
UNIDAD_DE_MEDIDA_CHOICES = [
    ('Ft*2', 'Ft*2'),
    ('Unidad', 'Unidad'),
    ('Metros', 'Metros'),
    ('Centimetros', 'Centímetros'),
    ('Litros', 'Litros'),
    ('Mililitros', 'Mililitros'),
    ('Kilos','Kilos'),
    ('Gramos','Gramos'),
]

# Opciones para la calidad del producto
CALIDAD_CHOICES = [
    ('Bueno', 'Bueno'),
    ('Media', 'Media'),
    ('Baja', 'Baja'),
]

# Opciones para la dimensión del producto
DIMENSION_CHOICES = [
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
]

# Opciones para el género del producto
GENERO_CHOICES = [
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Otro', 'Otro'),
]

# Formulario para Proveedor
class ProveedorForm(forms.ModelForm):
    tipoproveedor = forms.ChoiceField(choices=TIPO_PROVEEDOR_CHOICES)

    class Meta:
        model = Proveedor
        fields = ['tipoproveedor', 'categoriaproveedor', 'direccion', 'sitioweb', 'comentarios',
                  'nombre1', 'nombre2', 'apellido1', 'apellido2', 'nombreempresa',
                  'telefono1', 'telefono2', 'correo1', 'correo2']
    
    def clean_tipoproveedor(self):
        tipo_proveedor = self.cleaned_data.get('tipoproveedor')
        if tipo_proveedor not in dict(TIPO_PROVEEDOR_CHOICES):
            raise forms.ValidationError('Tipo de proveedor inválido.')
        return tipo_proveedor
    
    def clean_telefono1(self):
        telefono1 = self.cleaned_data.get('telefono1')
        if len(telefono1) < 7:
            raise forms.ValidationError('El teléfono 1 debe tener al menos 7 dígitos.')
        return telefono1
    
    def clean_telefono2(self):
        telefono2 = self.cleaned_data.get('telefono2')
        if telefono2 and len(telefono2) < 7:
            raise forms.ValidationError('El teléfono 2 debe tener al menos 7 dígitos.')
        return telefono2
    
    def clean_correo1(self):
        correo1 = self.cleaned_data.get('correo1')
        if not correo1 or '@' not in correo1:
            raise forms.ValidationError('Correo 1 inválido.')
        return correo1
    
    def clean_nombre1(self):
        nombre1 = self.cleaned_data.get('nombre1')
        if not nombre1:
            raise forms.ValidationError('El primer nombre es obligatorio.')
        return nombre1

# Formulario para Cliente
class ClienteForm(forms.ModelForm):
    tipodocumento = forms.ChoiceField(choices=TIPO_DOCUMENTO_CHOICES)
    fechanacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'datetime'}))  # Agregando el calendario
    genero = forms.ChoiceField(choices=GENERO_CHOICES)
    

    class Meta:
        model = Cliente
        fields = ['numerodocumento', 'tipodocumento', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
                  'direccion', 'correo1', 'correo2', 'telefono1', 'telefono2', 'fechanacimiento', 'genero']
    
    def clean_numerodocumento(self):
        numerodocumento = self.cleaned_data.get('numerodocumento')
        if not numerodocumento:
            raise forms.ValidationError('Número de documento es obligatorio.')
        return numerodocumento

    def clean_tipodocumento(self):
        tipodocumento = self.cleaned_data.get('tipodocumento')
        if tipodocumento not in dict(TIPO_DOCUMENTO_CHOICES):
            raise forms.ValidationError('Tipo de documento inválido.')
        return tipodocumento

    def clean_telefono1(self):
        telefono1 = self.cleaned_data.get('telefono1')
        if len(telefono1) < 7:
            raise forms.ValidationError('El teléfono 1 debe tener al menos 7 dígitos.')
        return telefono1

    def clean_correo1(self):
        correo1 = self.cleaned_data.get('correo1')
        if not correo1 or '@' not in correo1:
            raise forms.ValidationError('Correo 1 inválido.')
        return correo1

# Formulario para Insumo
class InsumoForm(forms.ModelForm):
    unidaddemedida = forms.ChoiceField(choices=UNIDAD_DE_MEDIDA_CHOICES)
    imageninsumo = forms.ImageField(required=False)  # Campo opcional para subir imagen

    class Meta:
        model = Insumo
        fields = ['nombreinsumo', 'color', 'unidaddemedida', 'cantidad', 'fecharegistro', 'imageninsumo', 'dimension']
        widgets = {
            'fecharegistro': forms.DateTimeInput(attrs={'type': 'datetime'}),
        }

    def clean_imageninsumo(self):
        imageninsumo = self.cleaned_data.get('imageninsumo')
        if imageninsumo and imageninsumo.size > 5*1024*1024:  # 5MB límite
            raise forms.ValidationError('La imagen debe ser menor de 5MB.')
        return imageninsumo

    def clean_nombreinsumo(self):
        nombreinsumo = self.cleaned_data.get('nombreinsumo')
        if not nombreinsumo:
            raise forms.ValidationError('El nombre del insumo es obligatorio.')
        return nombreinsumo

    def clean_color(self):
        color = self.cleaned_data.get('color')
        if not color:
            raise forms.ValidationError('El color del insumo es obligatorio.')
        return color

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError('La cantidad debe ser mayor a 0.')
        return cantidad

    def clean_dimension(self):
        dimension = self.cleaned_data.get('dimension')
        if dimension not in dict(DIMENSION_CHOICES):
            raise forms.ValidationError('Dimensión debe ser uno de los siguientes valores: xs, s, m, l, xl.')
        return dimension

#Formulario para compra insumo 

class CompraInsumoForm(forms.ModelForm):
    class Meta:
        model = Comprainsumo
        fields = ['fechacompra', 'proveedor_idproveedor', 'idcomprasinsumos', 'preciounitario', 'cantidad', 'preciototal', 'insumo_idinsumos']
        widgets = {
            'fechacompra': forms.DateTimeInput(attrs={'type': 'datetime'}),
            'cantidad': forms.NumberInput(attrs={'step': '0.01'}),
            'preciounitario': forms.NumberInput(attrs={'step': '0.01'}),
            'preciototal': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super(CompraInsumoForm, self).__init__(*args, **kwargs)
        
        # Mostrar el código del insumo en lugar del ID
        self.fields['insumo_idinsumos'].queryset = Insumo.objects.all()  # Usa el nombre correcto del campo
        self.fields['insumo_idinsumos'].label_from_instance = lambda obj: f"{obj.codigo} - {obj.nombreinsumo} - {obj.color}"
        
        # Mostrar detalles del proveedor en lugar del ID
        self.fields['proveedor_idproveedor'].queryset = Proveedor.objects.all()
        self.fields['proveedor_idproveedor'].label_from_instance = lambda obj: f"{obj.tipoproveedor} - {obj.nombre1} - {obj.apellido1}"

# Formulario para Producto
class ProductoForm(forms.ModelForm):
    calidad = forms.ChoiceField(choices=CALIDAD_CHOICES)
    dimension = forms.ChoiceField(choices=DIMENSION_CHOICES)
    genero = forms.ChoiceField(choices=GENERO_CHOICES)
    imagenproducto = forms.ImageField(required=False)  # Campo opcional para subir imagen

    class Meta:
        model = Producto
        fields = ['codigo','nombrecategoria', 'nombreproducto', 'precio', 'calidad', 'dimension', 'color', 'observaciones', 'genero', 'imagenproducto', 'cantidad']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0.')
        return precio

    def clean_calidad(self):
        calidad = self.cleaned_data.get('calidad')
        if calidad not in dict(CALIDAD_CHOICES):
            raise forms.ValidationError('Calidad debe ser uno de los siguientes valores: Alta, Media, Baja.')
        return calidad

    def clean_dimension(self):
        dimension = self.cleaned_data.get('dimension')
        if dimension not in dict(DIMENSION_CHOICES):
            raise forms.ValidationError('Dimensión debe ser uno de los siguientes valores: xs, s, m, l, xl.')
        return dimension

    def clean_color(self):
        color = self.cleaned_data.get('color')
        if not color:
            raise forms.ValidationError('El color es obligatorio.')
        return color

#formulario de compra producto 

class CompraProductoForm(forms.ModelForm):    
    class Meta:
        model = Compraproducto
        fields = ['fechacompra','producto_idproducto', 'proveedor_idproveedor','idcomprasproductos', 'preciounitario', 'cantidad', 'preciototal' ]
        widgets = {
            'fechacompra': forms.DateTimeInput(attrs={'type': 'datetime'}),
            'cantidad': forms.NumberInput(attrs={'step': '0.01'}),
            'preciounitario': forms.NumberInput(attrs={'step': '0.01'}),
            'preciototal': forms.NumberInput(attrs={'step': '0.01'}),
            
        }

    def __init__(self, *args, **kwargs):
        super(CompraProductoForm, self).__init__(*args, **kwargs)
        
        # Mostrar el código del producto en lugar del ID
        self.fields['producto_idproducto'].queryset = Producto.objects.all()
        self.fields['producto_idproducto'].label_from_instance = lambda obj: f"{obj.codigo} - {obj.nombrecategoria} - {obj.nombreproducto}"
        
        # Mostrar detalles del proveedor en lugar del ID
        self.fields['proveedor_idproveedor'].queryset = Proveedor.objects.all()
        self.fields['proveedor_idproveedor'].label_from_instance = lambda obj: f"{obj.tipoproveedor} - {obj.nombre1} - {obj.apellido1}"



    def clean_preciounitario(self):
        preciounitario = self.cleaned_data.get('preciounitario')
        if preciounitario <= 0:
            raise forms.ValidationError('El precio unitario debe ser mayor a 0.')
        return preciounitario

    def clean_preciototal(self):
        preciototal = self.cleaned_data.get('preciototal')
        if preciototal <= 0:
            raise forms.ValidationError('El precio total debe ser mayor a 0.')
        return preciototal

    

# Formulario para Ordendeproduccion

# Opciones para el estado del orden de producción
from django import forms
from .models import Detalleventa, Usuario, Ordendeproduccion

# Opciones para el estado del orden de producción
ESTADO_CHOICES = [
    ('Nuevo', 'Nuevo'),
    ('Finalizado', 'Finalizado'),
    ('Proceso', 'Proceso'),
    ('Atrasado', 'Atrasado'),
]

class OrdendeproduccionForm(forms.ModelForm):
    estado = forms.ChoiceField(choices=ESTADO_CHOICES)
    fechacreacion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime'}))
    fechafinalizacion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime'}))
    detalleventa_iddetalleventa = forms.ModelChoiceField(
        queryset=Detalleventa.objects.all(),
        label="Detalle de Venta"
    )
    usuario_idusurios = forms.ModelChoiceField(queryset=Usuario.objects.all(), label="Usuario")

    class Meta:
        model = Ordendeproduccion
        fields = ['estado', 'fechacreacion', 'fechafinalizacion', 'detalleventa_iddetalleventa', 'usuario_idusurios']
    
    # Modifica la representación del campo 'detalleventa_iddetalleventa'
    def __init__(self, *args, **kwargs):
        super(OrdendeproduccionForm, self).__init__(*args, **kwargs)

        # Personaliza cómo se muestra cada opción del 'detalleventa_iddetalleventa'
        self.fields['detalleventa_iddetalleventa'].label_from_instance = lambda obj: (
            f"{obj.venta_idventas.numeroventa} - "
            f"{obj.producto_idproducto.codigo} - "
            f"{obj.producto_idproducto.nombrecategoria} - "
            f"{obj.producto_idproducto.nombreproducto} - "
            f"{obj.producto_idproducto.color}"
        )

    # Validaciones personalizadas (opcionales)
    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if estado not in dict(ESTADO_CHOICES):
            raise forms.ValidationError('Estado inválido.')
        return estado

    def clean_fechacreacion(self):
        fechacreacion = self.cleaned_data.get('fechacreacion')
        if not fechacreacion:
            raise forms.ValidationError('Fecha de creación es obligatoria.')
        return fechacreacion

    def clean_fechafinalizacion(self):
        fechafinalizacion = self.cleaned_data.get('fechafinalizacion')
        if not fechafinalizacion:
            raise forms.ValidationError('Fecha de finalización es obligatoria.')
        return fechafinalizacion

    def clean_detalleventa_iddetalleventa(self):
        detalleventa_iddetalleventa = self.cleaned_data.get('detalleventa_iddetalleventa')
        if not detalleventa_iddetalleventa:
            raise forms.ValidationError('Detalle de venta es obligatorio.')
        return detalleventa_iddetalleventa

    def clean_usuario_idusurios(self):
        usuario_idusurios = self.cleaned_data.get('usuario_idusurios')
        if not usuario_idusurios:
            raise forms.ValidationError('Usuario es obligatorio.')
        return usuario_idusurios


#Formulario para control gasto insumo
class GastoInsumoForm(forms.ModelForm):
    unidaddemedida = forms.ChoiceField(choices=UNIDAD_DE_MEDIDA_CHOICES)
    numero_venta = forms.CharField(label='Número de Venta', max_length=20, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))  # Campo adicional
    
    class Meta:
        model = Controlgastoinsumo
        fields = ['fechauso', 'insumo_idinsumos', 'ordendeproduccion_idordendeproduccion', 'idcontrolgastoinsumo', 'cantidad', 'unidaddemedida', 'comentarios', 'numero_venta']
        widgets = {
            'fechauso': forms.DateTimeInput(attrs={'type': 'datetime'}),
            'cantidad': forms.NumberInput(attrs={'step': '0.01'}),
        }

    # Corregir el método __init__ con doble guion bajo
    def __init__(self, *args, **kwargs):
        super(GastoInsumoForm, self).__init__(*args, **kwargs)

        # Mostrar el código del insumo en lugar del ID
        self.fields['insumo_idinsumos'].queryset = Insumo.objects.all()
        self.fields['insumo_idinsumos'].label_from_instance = lambda obj: f"{obj.codigo} - {obj.nombreinsumo} - {obj.color}"

        # Mostrar el detalle de la orden de producción en lugar del ID
        self.fields['ordendeproduccion_idordendeproduccion'].queryset = Ordendeproduccion.objects.all()
        self.fields['ordendeproduccion_idordendeproduccion'].label_from_instance = lambda obj: f"Orden #{obj.idordendeproduccion} - Creada el {obj.fechacreacion.strftime('%Y-%m-%d')}"

        # Verificar si existe una instancia para editar, y rellenar el campo número de venta
        if self.instance.pk:
            # Obtener la orden de producción relacionada
            orden_produccion = self.instance.ordendeproduccion_idordendeproduccion
            if orden_produccion:
                # Obtener el detalle de la venta relacionado
                detalle_venta = orden_produccion.detalleventa_iddetalleventa
                if detalle_venta:
                    # Obtener la venta relacionada y el número de venta
                    venta = detalle_venta.venta_idventas
                    if venta:
                        # Asignar el número de venta al campo adicional
                        self.fields['numero_venta'].initial = venta.numeroventa




# Formulario para seleccionar clientes
class ClienteSeleccionadoForm(forms.Form):
    clientes = forms.ModelMultipleChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Selecciona clientes'
    )

# Formulario para enviar correos
class EnviarCorreoForm(forms.Form):
    destinatarios = forms.CharField(
        widget=forms.Textarea(attrs={'readonly': 'readonly'}),
        label='Destinatarios'
    )
    asunto = forms.CharField(label='Asunto')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')





from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from .models import Cliente

class ClienteSignUpForm(UserCreationForm):
    # Opciones para el campo de tipo de documento
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
    ]

    # Opciones para el campo de género
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]

    # Definimos los campos del formulario
    numero_documento = forms.CharField(
        max_length=45,
        validators=[MinLengthValidator(5, "El número de documento debe tener al menos 5 caracteres.")],
        required=True,
        label="Número de Documento"
    )
    tipo_documento = forms.ChoiceField(choices=TIPO_DOCUMENTO_CHOICES, label="Tipo de Documento")
    nombre1 = forms.CharField(
        max_length=45,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'El primer nombre solo debe contener letras.')],
        label="Primer Nombre"
    )
    nombre2 = forms.CharField(max_length=45, required=False, label="Segundo Nombre")
    apellido1 = forms.CharField(
        max_length=45,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'El primer apellido solo debe contener letras.')],
        label="Primer Apellido"
    )
    apellido2 = forms.CharField(max_length=45, required=False, label="Segundo Apellido")
    direccion = forms.CharField(
        max_length=300,
        validators=[MinLengthValidator(10, "La dirección debe tener al menos 10 caracteres.")],
        label="Dirección"
    )
    correo2 = forms.EmailField(max_length=150, required=False, label="Correo Electrónico 2 (Opcional)")
    telefono1 = forms.CharField(
        max_length=13,
        validators=[RegexValidator(r'^\+?\d{7,13}$', "El teléfono debe tener entre 7 y 13 dígitos.")],
        label="Teléfono 1"
    )
    telefono2 = forms.CharField(max_length=13, required=False, label="Teléfono 2 (Opcional)")
    fechanacimiento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")
    genero = forms.ChoiceField(choices=GENERO_CHOICES, label="Género")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Validamos que el correo no esté registrado
    def clean_email(self):
        """Verifica si el correo electrónico ya está registrado en el modelo User"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    # Validamos que el número de documento no cause conflicto
    def clean_numero_documento(self):
        """Permite la asociación del usuario a un cliente existente sin un usuario asociado"""
        numero_documento = self.cleaned_data.get('numero_documento')
        cliente = Cliente.objects.filter(numerodocumento=numero_documento).first()

        if cliente and cliente.user:
            raise ValidationError('Ya existe un cliente registrado con este número de documento y un usuario asociado.')
        
        return numero_documento

    # Método para guardar el cliente y el usuario
    def save(self, commit=True, update_cliente=False):
        # Creamos el usuario pero no lo guardamos todavía
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Sincronizamos email con el correo1 de Cliente
        user.username = self.cleaned_data['username']
        
        if commit:
            user.save()

            numero_documento = self.cleaned_data['numero_documento']
            cliente = Cliente.objects.filter(numerodocumento=numero_documento).first()

            if cliente and update_cliente:
                # Si el cliente ya existe, actualizamos su información
                cliente.user = user
                cliente.tipodocumento = self.cleaned_data['tipo_documento']
                cliente.nombre1 = self.cleaned_data['nombre1']
                cliente.nombre2 = self.cleaned_data['nombre2']
                cliente.apellido1 = self.cleaned_data['apellido1']
                cliente.apellido2 = self.cleaned_data['apellido2']
                cliente.direccion = self.cleaned_data['direccion']
                cliente.correo1 = user.email  # Sincronizamos el correo1 con el email del User
                cliente.correo2 = self.cleaned_data['correo2']
                cliente.telefono1 = self.cleaned_data['telefono1']
                cliente.telefono2 = self.cleaned_data['telefono2']
                cliente.fechanacimiento = self.cleaned_data['fechanacimiento']
                cliente.genero = self.cleaned_data['genero']
                cliente.save()
            else:
                # Si no existe, lo creamos
                Cliente.objects.create(
                    user=user,
                    numerodocumento=self.cleaned_data['numero_documento'],
                    tipodocumento=self.cleaned_data['tipo_documento'],
                    nombre1=self.cleaned_data['nombre1'],
                    nombre2=self.cleaned_data['nombre2'],
                    apellido1=self.cleaned_data['apellido1'],
                    apellido2=self.cleaned_data['apellido2'],
                    direccion=self.cleaned_data['direccion'],
                    correo1=user.email,  # Sincronizamos el correo1 con el email del User
                    correo2=self.cleaned_data['correo2'],
                    telefono1=self.cleaned_data['telefono1'],
                    telefono2=self.cleaned_data['telefono2'],
                    fechanacimiento=self.cleaned_data['fechanacimiento'],
                    genero=self.cleaned_data['genero'],
                )

        return user




from django import forms
from .models import Cliente

class ActualizarClienteForm(forms.ModelForm):
    # Opciones para el campo de género
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]

    genero = forms.ChoiceField(choices=GENERO_CHOICES, label="Género")
    
    class Meta:
        model = Cliente
        fields = [
            'nombre1', 'nombre2', 'apellido1', 'apellido2',
            'direccion', 'correo1', 'correo2', 'telefono1', 'telefono2',
            'fechanacimiento', 'genero'
        ]
        labels = {
            'nombre1': 'Primer Nombre',
            'nombre2': 'Segundo Nombre (Opcional)',
            'apellido1': 'Primer Apellido',
            'apellido2': 'Segundo Apellido (Opcional)',
            'direccion': 'Dirección',
            'correo1': 'Correo Electrónico',
            'correo2': 'Correo Electrónico Secundario (Opcional)',
            'telefono1': 'Teléfono Principal',
            'telefono2': 'Teléfono Secundario (Opcional)',
            'fechanacimiento': 'Fecha de Nacimiento',
            'genero': 'Género',
        }
        widgets = {
            'nombre1': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre2': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido1': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido2': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo1': forms.EmailInput(attrs={'class': 'form-control'}),
            'correo2': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono1': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono2': forms.TextInput(attrs={'class': 'form-control'}),
            'fechanacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }







    
    #venntas Nathalia 



from django import forms
from .models import Venta, Metododepago
from django.utils import timezone

MODALIDAD_VENTA_CHOICES = [
    ('virtual', 'Virtual'),
    ('presencial', 'Presencial'),
]

class VentaForm(forms.ModelForm):
    fechaventa = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime'}),
        initial=timezone.now,  # Fecha y hora actual por defecto
        required=True
    )
    modalidadventa = forms.ChoiceField(
        choices=MODALIDAD_VENTA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Modalidad de Venta"
    )
    

    # Campos para mostrar los datos del cliente (readonly)
    nombre1 = forms.CharField(label="Primer Nombre", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    nombre2 = forms.CharField(label="Segundo Nombre", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    apellido1 = forms.CharField(label="Primer Apellido", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    apellido2 = forms.CharField(label="Segundo Apellido", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    tipodocumento = forms.CharField(label="Tipo de Documento", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    numerodocumento = forms.CharField(label="Número de Documento", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = Venta
        fields = ['metododepago_idmetododepago', 'modalidadventa', 'fechaventa']  # Eliminamos cliente_idclientes

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)  # Recibimos el cliente verificado
        super(VentaForm, self).__init__(*args, **kwargs)

        self.fields['metododepago_idmetododepago'].label_from_instance = lambda obj: f"{obj.metododepago}"
        
        
        if cliente:
            # Prellenar los campos de cliente en el formulario (readonly)
            self.fields['nombre1'].initial = cliente.nombre1
            self.fields['nombre2'].initial = cliente.nombre2
            self.fields['apellido1'].initial = cliente.apellido1
            self.fields['apellido2'].initial = cliente.apellido2
            self.fields['tipodocumento'].initial = cliente.tipodocumento
            self.fields['numerodocumento'].initial = cliente.numerodocumento



class DetalleVentaForm(forms.ModelForm):
    producto_idproducto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'producto-select'})  # Especificamos el id correcto
    )
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'id_cantidad'}))  # Aseguramos el id del campo cantidad

    class Meta:
        model = Detalleventa
        fields = ['producto_idproducto', 'cantidad']

    def __init__(self, *args, **kwargs):
        super(DetalleVentaForm, self).__init__(*args, **kwargs)
        # Personaliza la etiqueta del producto en el desplegable si necesitas algo más complejo
        self.fields['producto_idproducto'].label_from_instance = lambda obj: f"{obj.codigo} - {obj.nombreproducto} "


from django.forms import modelformset_factory
from .models import Detalleventa

# Formset para manejar múltiples DetalleVenta
DetalleVentaFormSet = modelformset_factory(
    Detalleventa,
    form=DetalleVentaForm,
    extra=1,  # Número de formularios adicionales
    can_delete=True  # Permitir eliminar formularios
)





from django.utils import timezone

class VentaClienteForm(forms.ModelForm):
    fechaventa = forms.DateTimeField(
        widget=forms.HiddenInput(),  # Hacer el campo oculto
        required=False  # Ya no es obligatorio desde el formulario
    )

    # Campos del cliente que se mostrarán prellenados y de solo lectura
    nombre1 = forms.CharField(label="Primer Nombre", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    nombre2 = forms.CharField(label="Segundo Nombre", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    apellido1 = forms.CharField(label="Primer Apellido", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    apellido2 = forms.CharField(label="Segundo Apellido", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    tipodocumento = forms.CharField(label="Tipo de Documento", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    numerodocumento = forms.CharField(label="Número de Documento", widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    # Ocultar el campo de modalidad de venta y asignarlo automáticamente
    modalidadventa = forms.CharField(widget=forms.HiddenInput(), initial='virtual')

    class Meta:
        model = Venta
        fields = ['metododepago_idmetododepago', 'modalidadventa', 'fechaventa']

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)
        super(VentaClienteForm, self).__init__(*args, **kwargs)

        # Etiqueta para el método de pago
        self.fields['metododepago_idmetododepago'].label_from_instance = lambda obj: f"{obj.metododepago}"

        if cliente:
            # Prellenar los datos del cliente en el formulario
            self.fields['nombre1'].initial = cliente.nombre1
            self.fields['nombre2'].initial = cliente.nombre2
            self.fields['apellido1'].initial = cliente.apellido1
            self.fields['apellido2'].initial = cliente.apellido2
            self.fields['tipodocumento'].initial = cliente.tipodocumento
            self.fields['numerodocumento'].initial = cliente.numerodocumento

    def save(self, commit=True):
        # Asignar la fecha actual automáticamente
        self.instance.fechaventa = timezone.now()
        # Asegurar que la modalidad de venta sea siempre 'virtual'
        self.instance.modalidadventa = 'virtual'
        
        return super(VentaClienteForm, self).save(commit=commit)





#### panel de control 


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Usuario

class UsuarioSignUpForm(UserCreationForm):
    # Campos adicionales basados en tu modelo Usuario
    numerodocumento = forms.CharField(max_length=20, label="Número de Documento")
    tipodedocumento = forms.CharField(max_length=2, label="Tipo de Documento")
    primernombre = forms.CharField(max_length=45, label="Primer Nombre")
    segundonombre = forms.CharField(max_length=45, required=False, label="Segundo Nombre")
    primeraprellido = forms.CharField(max_length=45, label="Primer Apellido")
    segundoaprellido = forms.CharField(max_length=45, required=False, label="Segundo Apellido")
    correo2 = forms.EmailField(max_length=100, required=False, label="Correo Electrónico 2")
    telefono1 = forms.CharField(max_length=13, label="Teléfono 1")

    # Selección de rol entre Administrador y Jefe de Producción
    ROLES_CHOICES = [
        ('admin', 'Administrador'),
        ('jefe_produccion', 'Jefe de Producción'),
    ]
    rol = forms.ChoiceField(choices=ROLES_CHOICES, label="Rol")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 
                  'numerodocumento', 'tipodedocumento', 'primernombre', 
                  'segundonombre', 'primeraprellido', 'segundoaprellido', 
                  'correo2', 'telefono1', 'rol']

    def save(self, commit=True):
        # Guardar primero el usuario de Django
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()  # Guardar el usuario de Django

            # Crear el registro del modelo personalizado Usuario
            usuario = Usuario.objects.create(
                user=user,
                numerodocumento=self.cleaned_data['numerodocumento'],
                tipodedocumento=self.cleaned_data['tipodedocumento'],
                primernombre=self.cleaned_data['primernombre'],
                segundonombre=self.cleaned_data['segundonombre'],
                primeraprellido=self.cleaned_data['primeraprellido'],
                segundoaprellido=self.cleaned_data['segundoaprellido'],
                correo1=user.email,  # Sincronizar correo1 con el correo del modelo User
                correo2=self.cleaned_data['correo2'],
                telefono1=self.cleaned_data['telefono1']

            )

            # Asignar grupo basado en el rol seleccionado
            rol = self.cleaned_data['rol']
            if rol == 'admin':
                grupo = Group.objects.get(name='Administrador')  # Asegúrate que el grupo existe
            elif rol == 'jefe_produccion':
                grupo = Group.objects.get(name='Jefe de Producción')  # Asegúrate que el grupo existe

            # Agregar el usuario al grupo correspondiente
            user.groups.add(grupo)

        return user
