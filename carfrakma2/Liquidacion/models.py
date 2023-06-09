from django.db import models

# #Datos Liquidacion
class EstadoL(models.Model):
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return ' {} '.format(self.descripcion)
    

class Liquidacion(models.Model):
    description = models.TextField(max_length=100)
    date = models.DateField()
    amount = models.FloatField()
    estadoL = models.ForeignKey(EstadoL, null=True, blank=True, on_delete=models.CASCADE)
    # conductor = models.ForeignKey(Conductor, null=True, blank=True, on_delete=models.CASCADE)
    # administrador = models.ForeignKey(Administrador, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return ' {} '.format(self.description)


#Datos Usuario
# class Usuario(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=128)

# #-------------------------------------------------------------
# #Datos Administrador
# class Administrador(models.Model):
#     name = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)

# #-------------------------------------------------------------
# #Datos Vehiculo
# class EstadoV(models.Model):
#     descripcion = models.TextField(max_length=100)

# class Vehiculo(models.Model):
#     placa = models.CharField(max_length=20)
#     marca = models.CharField(max_length=50)
#     modelo = models.CharField(max_length=50)
#     estadoV = models.OneToOneField(EstadoV, null=True, blank=True, on_delete=models.CASCADE)

# #-------------------------------------------------------------
# #Datos Conductor
# class EstadoC(models.Model):
#     descripcion = models.TextField(max_length=100)

# class Conductor(models.Model):
#     name = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     birthdate = models.DateField()
#     estadoC = models.OneToOneField(EstadoC, null=True, blank=True, on_delete=models.CASCADE)
#     vehiculo = models.OneToOneField(Vehiculo, null=True, blank=True, on_delete=models.CASCADE)

# #-------------------------------------------------------------