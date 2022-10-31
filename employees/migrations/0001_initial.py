# Generated by Django 4.1.2 on 2022-10-31 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('hired_at', models.DateField(auto_now=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9)),
                ('boss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]