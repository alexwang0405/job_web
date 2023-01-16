# Generated by Django 4.1.4 on 2022-12-31 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='web',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jobs.platform'),
        ),
    ]
