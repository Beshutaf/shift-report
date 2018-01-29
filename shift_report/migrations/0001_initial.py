# Generated by Django 2.0.1 on 2018-01-29 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shift_report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_from_shares', models.IntegerField(default=0)),
                ('money_from_cheques', models.IntegerField(default=0)),
                ('money_from_cash', models.IntegerField(default=0)),
                ('envelope_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_number', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_report.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('date', models.DateField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('cache', models.ForeignKey(default=shift_report.models.Cache.empty, on_delete=django.db.models.deletion.CASCADE, to='shift_report.Cache')),
                ('leaving_members', models.ManyToManyField(related_name='leaving', to='shift_report.Member')),
                ('members', models.ManyToManyField(through='shift_report.MemberShift', to='shift_report.Member')),
                ('missing_products', models.ManyToManyField(related_name='almost_missing', to='shift_report.Product')),
                ('new_members', models.ManyToManyField(related_name='new', to='shift_report.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Conclusions',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shift_report.Item')),
                ('assigned_team', models.CharField(max_length=128)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_report.Shift')),
            ],
            bases=('shift_report.item',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shift_report.Item')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_report.Shift')),
            ],
            bases=('shift_report.item',),
        ),
        migrations.AddField(
            model_name='membershift',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_report.Role'),
        ),
        migrations.AddField(
            model_name='membershift',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_report.Shift'),
        ),
        migrations.AddField(
            model_name='cache',
            name='money_at_shift_end',
            field=models.ManyToManyField(related_name='shift_end', to='shift_report.Money'),
        ),
        migrations.AddField(
            model_name='cache',
            name='money_at_shift_start',
            field=models.ManyToManyField(related_name='shift_start', to='shift_report.Money'),
        ),
    ]
