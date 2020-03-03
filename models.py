# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActionItem(models.Model):
    date_assigned = models.DateField(db_column='Date_Assigned', blank=True, null=True)  # Field name made lowercase.
    date_due = models.DateField(db_column='Date_Due', blank=True, null=True)  # Field name made lowercase.
    date_completed = models.DateField(db_column='Date_Completed', blank=True, null=True)  # Field name made lowercase.
    date_verified = models.DateField(db_column='Date_Verified', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    how_verified = models.CharField(db_column='How_Verified', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=6, blank=True, null=True)  # Field name made lowercase.
    issue = models.ForeignKey('Issue', models.DO_NOTHING, db_column='Issue_id', blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('Members', models.DO_NOTHING, db_column='Member_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Action_Item'


class Actions(models.Model):
    content = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=27, blank=True, null=True)
    issue = models.ForeignKey('Issue', models.DO_NOTHING, db_column='Issue_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actions'


class D5(models.Model):
    corrective_actions = models.CharField(db_column='Corrective_Actions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    verification = models.CharField(db_column='Verification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    issue = models.ForeignKey('Issue', models.DO_NOTHING, db_column='Issue_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'D5'


class Issue(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.CharField(db_column='Customer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(db_column='Project', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='Supplier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    part_num = models.CharField(db_column='Part_num', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ron_num = models.CharField(db_column='RON_num', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    open_date = models.DateField(db_column='Open Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    due_date = models.DateField(db_column='Due Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    closed_date = models.DateField(db_column='Closed Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file = models.TextField(db_column='File', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Issue'


class Members(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dept_field = models.CharField(db_column='Dept.', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    telephone_field = models.IntegerField(db_column='Telephone#', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Members'


class Recognize(models.Model):
    name = models.ForeignKey(Members, models.DO_NOTHING, db_column='Name_id', blank=True, null=True)  # Field name made lowercase.
    issue = models.ForeignKey(Issue, models.DO_NOTHING, db_column='Issue_id', blank=True, null=True)  # Field name made lowercase.
    signature = models.TextField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.
    closure_date = models.DateTimeField(db_column='Closure_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recognize'


class Team(models.Model):
    issue = models.ForeignKey(Issue, models.DO_NOTHING, blank=True, null=True)
    member = models.ForeignKey(Members, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Team'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TableName(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    customer = models.TextField(db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    project = models.TextField(db_column='Project', blank=True, null=True)  # Field name made lowercase.
    supplier = models.TextField(db_column='Supplier', blank=True, null=True)  # Field name made lowercase.
    part_num = models.FloatField(db_column='Part_num', blank=True, null=True)  # Field name made lowercase.
    ron_num = models.FloatField(db_column='RON_num', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    owner = models.FloatField(db_column='Owner', blank=True, null=True)  # Field name made lowercase.
    open_date = models.DateTimeField(db_column='Open Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    due_date = models.FloatField(db_column='Due Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    closed_date = models.DateTimeField(db_column='Closed Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'table_name'
