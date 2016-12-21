# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 13:47
from __future__ import unicode_literals

from django.db import migrations


def create_and_copy_transaction_types(apps, schema_editor):
    TransactionType = apps.get_model('ledger', 'TransactionType')
    Transaction = apps.get_model('ledger', 'Transaction')

    for ttype_name, pretty_name in [
            ('MANUAL', 'Manual'),
            ('AUTOMATIC', 'Automatic'),
            ('RECONCILIATION', 'Reconciliation'),
    ]:
        ttype = TransactionType.objects.get_or_create(
            name=pretty_name,
            description='',
        )[0]

        Transaction.objects.filter(type=ttype_name).update(type2=ttype)


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0014_auto_20160928_1345'),
    ]

    operations = [
        migrations.RunPython(create_and_copy_transaction_types),
    ]