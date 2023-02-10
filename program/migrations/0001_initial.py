from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('idProgram', models.AutoField(primary_key=True, serialize=False)),
                ('validityDate', models.DateTimeField(blank=True, default=django.utils.timezone.n$
            ],
            options={
                'db_table': 'tblProgram',
            },
        ),
    ]