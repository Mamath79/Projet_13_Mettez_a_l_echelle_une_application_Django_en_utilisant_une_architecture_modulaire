from django.db import migrations


def copy_profiles_data(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    Profile = apps.get_model("profiles", "Profile")

    for old_profile in OldProfile.objects.all():
        Profile.objects.create(
            id=old_profile.id,
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_profiles_data),
    ]
