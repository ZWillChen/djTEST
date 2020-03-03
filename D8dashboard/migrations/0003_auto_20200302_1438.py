# Generated by Django 3.0.3 on 2020-03-02 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('D8dashboard', '0002_auto_20200224_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableName',
            fields=[
                ('id', models.BigIntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('customer', models.TextField(blank=True, db_column='Customer', null=True)),
                ('project', models.TextField(blank=True, db_column='Project', null=True)),
                ('supplier', models.TextField(blank=True, db_column='Supplier', null=True)),
                ('part_num', models.FloatField(blank=True, db_column='Part_num', null=True)),
                ('ron_num', models.FloatField(blank=True, db_column='RON_num', null=True)),
                ('cost', models.FloatField(blank=True, db_column='Cost', null=True)),
                ('owner', models.FloatField(blank=True, db_column='Owner', null=True)),
                ('open_date', models.DateTimeField(blank=True, db_column='Open Date', null=True)),
                ('due_date', models.FloatField(blank=True, db_column='Due Date', null=True)),
                ('closed_date', models.DateTimeField(blank=True, db_column='Closed Date', null=True)),
            ],
            options={
                'db_table': 'table_name',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='D8DashboardPost',
        ),
    ]
