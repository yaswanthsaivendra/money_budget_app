# Generated by Django 4.1.4 on 2023-01-03 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('splitter', '0009_alter_personal_expense_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simple_transaction',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_reciever', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='simple_transaction',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SplitRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('amount', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_splitroom', to=settings.AUTH_USER_MODEL)),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer_splitroom', to=settings.AUTH_USER_MODEL)),
                ('splitters', models.ManyToManyField(related_name='member_splitrooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
