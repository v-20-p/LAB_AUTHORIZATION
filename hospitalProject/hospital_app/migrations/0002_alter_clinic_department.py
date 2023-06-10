# Generated by Django 4.2.1 on 2023-06-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='department',
            field=models.CharField(choices=[('Heart Center', 'Heart Center'), ('Neuroscience Center', 'Neuroscience Center'), ('Obesity Center', 'Obesity Center'), ('Eye Center', 'Eye Center'), ('Orthopedic Center', 'Orthopedic Center'), ('Pediatric Center', 'Pediatric Center')], max_length=50),
        ),
    ]
