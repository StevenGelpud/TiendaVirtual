from django.db import models

class Administrador(models.Model):
    idAdmin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def registrar(self):
        # Implementar lógica de registro
        pass

    def iniciarSesion(self):
        # Implementar lógica de inicio de sesión
        pass

    def gestionarProductos(self):
        # Implementar lógica de gestión de productos
        pass

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def registrar(self):
        # Implementar lógica de registro
        pass

    def iniciarSesion(self):
        # Implementar lógica de inicio de sesión
        pass

    def actualizarPerfil(self):
        # Implementar lógica de actualización de perfil
        pass

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def actualizar(self):
        # Implementar lógica de actualización del producto
        pass

    def obtenerDetalles(self):
        # Implementar lógica para obtener detalles del producto
        pass

class CarritoDeCompras(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    listaProductos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def agregarProducto(self, producto):
        # Implementar lógica para agregar producto al carrito
        pass

    def eliminarProducto(self, producto):
        # Implementar lógica para eliminar producto del carrito
        pass

    def calcularTotal(self):
        # Implementar lógica para calcular el total
        pass

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def confirmarPedido(self):
        # Implementar lógica para confirmar el pedido
        pass

    def cancelarPedido(self):
        # Implementar lógica para cancelar el pedido
        pass

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    metodoPago = models.CharField(max_length=50)
    totalPago = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPago = models.DateTimeField(auto_now_add=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def procesarPago(self):
        # Implementar lógica para procesar el pago
        pass

    def generarFactura(self):
        # Implementar lógica para generar factura
        pass
