# Generated by Django 4.1.6 on 2023-02-19 17:33

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('default_image', models.CharField(max_length=200, null=True)),
                ('current_date', models.DateField(auto_now_add=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='inputTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_year', models.CharField(default=2023, max_length=20)),
                ('input_month', models.CharField(default=2, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('family', '가족'), ('couple', '연인'), ('club', '동아리'), ('friend', '친구'), ('school', '학교'), ('company', '회사'), ('etc', '기타')], max_length=20)),
                ('invitation_code', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='team_profile')),
                ('default_image', models.CharField(max_length=200, null=True)),
                ('owner', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meetings', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='user_meetings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrivatePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('location', models.CharField(blank=True, max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='private_plan', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublicComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_share', models.CharField(choices=[('open', '공개'), ('close', '비공개'), ('untitled', '비밀일정')], max_length=20)),
                ('meeting', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_shares', to='wapl.meeting')),
                ('plan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plan_shares', to='wapl.privateplan')),
            ],
        ),
        migrations.CreateModel(
            name='replyPublicComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_comment', to='wapl.publiccomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='replyPrivateComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_comment', to='wapl.privatecomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublicPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('location', models.CharField(blank=True, max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True)),
                ('meetings', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='wapl.meeting')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='public_plan', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='publiccomment',
            name='plan_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_plan', to='wapl.publicplan'),
        ),
        migrations.AddField(
            model_name='publiccomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='privatecomment',
            name='plan_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_plan', to='wapl.privateplan'),
        ),
        migrations.AddField(
            model_name='privatecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attend', models.CharField(choices=[('attend', '참석'), ('absence', '불참'), ('standby', '대기상태')], max_length=10)),
                ('plan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plan_attend', to='wapl.publicplan')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_attend', to=settings.AUTH_USER_MODEL)),

            ],
        ),
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attend', models.CharField(choices=[('attend', '참석'), ('absence', '불참'), ('standby', '대기상태')], max_length=10)),
                ('plan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plan_attend', to='wapl.publicplan')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_attend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
