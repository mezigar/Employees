from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hired_at = models.DateField(auto_now=True)
    salary = models.DecimalField(max_digits = 9, decimal_places= 2)
    boss = models.ForeignKey('self', null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.pk}> {self.name} - {self.position}'