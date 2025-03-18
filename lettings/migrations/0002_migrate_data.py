from django.db import migrations


def copy_lettings_data(apps, schema_editor):
    OldAddress = apps.get_model("lettings", "Address")
    Address = apps.get_model("lettings", "Address")

    OldLetting = apps.get_model("lettings", "Letting")
    Letting = apps.get_model("lettings", "Letting")

    for old_address in OldAddress.objects.all():
        Address.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

    for old_letting in OldLetting.objects.all():
        Letting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address=Address.objects.get(id=old_letting.address.id),
        )


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_lettings_data),
    ]
