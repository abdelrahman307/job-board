# Generated by Django 4.0.5 on 2022-06-09 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_vacancy_job_description_job_experience_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
            preserve_default=False,
        ),
    ]
