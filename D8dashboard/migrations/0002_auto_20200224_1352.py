# Generated by Django 3.0.3 on 2020-02-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('D8dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(blank=True, db_column='Date_Assigned', null=True)),
                ('date_due', models.DateField(blank=True, db_column='Date_Due', null=True)),
                ('date_completed', models.DateField(blank=True, db_column='Date_Completed', null=True)),
                ('date_verified', models.DateField(blank=True, db_column='Date_Verified', null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('owner', models.CharField(blank=True, db_column='Owner', max_length=255, null=True)),
                ('verification', models.CharField(blank=True, db_column='Verification', max_length=255, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=6, null=True)),
            ],
            options={
                'db_table': 'Action_Item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=27, null=True)),
            ],
            options={
                'db_table': 'Actions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='D5',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('corrective_actions', models.CharField(blank=True, db_column='Corrective_Actions', max_length=255, null=True)),
                ('verification', models.CharField(blank=True, db_column='Verification', max_length=255, null=True)),
            ],
            options={
                'db_table': 'D5',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='D8DashboardPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'D8dashboard_post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('problem', models.CharField(blank=True, db_column='Problem', max_length=255, null=True)),
                ('supplier', models.CharField(blank=True, db_column='Supplier', max_length=255, null=True)),
                ('part_num', models.CharField(blank=True, db_column='Part_num', max_length=255, null=True)),
                ('ron_num', models.CharField(blank=True, db_column='RON_num', max_length=255, null=True)),
                ('cost', models.DecimalField(blank=True, db_column='Cost', decimal_places=2, max_digits=19, null=True)),
                ('owner', models.CharField(blank=True, db_column='Owner', max_length=255, null=True)),
                ('open_date', models.DateField(blank=True, db_column='Open Date', null=True)),
                ('due_date', models.DateField(blank=True, db_column='Due Date', null=True)),
                ('closed_date', models.DateField(blank=True, db_column='Closed Date', null=True)),
            ],
            options={
                'db_table': 'Issue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True, unique=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=50, null=True)),
                ('dept_field', models.CharField(blank=True, db_column='Dept.', max_length=8, null=True)),
                ('telephone_field', models.IntegerField(blank=True, db_column='Telephone#', null=True)),
            ],
            options={
                'db_table': 'Members',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recognize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.TextField(blank=True, db_column='Signature', null=True)),
                ('closure_date', models.DateTimeField(blank=True, db_column='Closure_Date', null=True)),
            ],
            options={
                'db_table': 'Recognize',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Team',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
