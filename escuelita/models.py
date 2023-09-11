from django.db import models

# Create your models here.
# Son elementos que se van a reflejar en la base de datos como tablas

#ORM Object-Relational-Mapping
class Tira(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)

    def __str__(self):
        txt = f"{self.nombre}"
        return txt

class Jugador(models.Model):
    dni = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    vigencia = models.BooleanField(default=True)
    

    class Meta:
        verbose_name_plural = "Jugadores"
    def __str__(self):
        txt = f"{self.nombre} {self.apellido}"
        return txt

    def nombreCompleto(self):
        txt = "{0} {1}"
        return txt.format(self.nombre, self.apellido)

class Categoria(models.Model):
    codigo = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=35)

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    jugador = models.ForeignKey(Jugador,null=False,blank=False,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,null=False,blank=False,on_delete=models.CASCADE)
    tira = models.ForeignKey(Tira,null=False,blank=False,on_delete=models.CASCADE)


