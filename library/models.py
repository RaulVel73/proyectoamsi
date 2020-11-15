from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Categoria')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    

class Inventario(models.Model):
    entrada = models.PositiveIntegerField(verbose_name='Entrada')
    salida = models.PositiveIntegerField(verbose_name='Salida')

    def __str__(self):
        return "{0}".format(self.entrada)


    class Meta:
        verbose_name='Inventario'
        verbose_name_plural='Inventarios'


class Clientes(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre cliente')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    contacto = models.PositiveIntegerField(verbose_name='Contacto')

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'



class Proveedores(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre proveedor')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    contacto = models.PositiveIntegerField(verbose_name='Contacto')

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'


class Ventas(models.Model):
    hora = models.DateTimeField(verbose_name='Fecha y Hora de la venta')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad de productos')
    importe = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Importe de la venta')

    def __str__(self):
        return "{0}".format(self.hora)


    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        
        
class Productos(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre del producto')
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name='Categoria')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

        
