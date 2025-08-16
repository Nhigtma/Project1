from django.db import models

class people(models.Model):
    cc = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    weight = models.DecimalField(max_digits=3, decimal_places=1)
    height = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=50)
    imc = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    state = models.CharField(default=" ")
    class Meta:
        app_label = 'app'
    def __str__(self):
        return (f"{self.cc} - {self.first_name} {self.last_name} | "
            f"Age: {self.age} | W: {self.weight}kg | "
            f"H: {self.height}cm | Gender: {self.gender} |"
            f"IMC: {self.imc} | State: {self.state}")