from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
# Create your models here.
from phoenix.storage_backends import MediaStorage

# Define the upload_to functions with the `photo_id`
def upload_to1(instance, filename):
    return f"poi_building/{instance.photo_id}/{filename}"

def upload_to2(instance, filename):
    return f"signboard_images/{instance.photo_id}/{filename}"

def upload_to3(instance, filename):
    return f"phone_number_images/{instance.photo_id}/{filename}"

def upload_to4(instance, filename):
    return f"menu_brochure_images/{instance.photo_id}/{filename}"

def upload_to5(instance, filename):
    return f"visiting_card_images/{instance.photo_id}/{filename}"

def generate_unique_identifier():
    # Generate a random integer portion of the identifier
    unique_integer = uuid.uuid4().int & ((1 << 31) - 1)
    # Combine the prefix and integer portion
    unique_identifier = f"{unique_integer:06}"
    return unique_identifier
def generate_unique_identifier_pohotoid():
    # Generate a random integer portion of the identifier
    unique_integer = uuid.uuid4().int & ((1 << 31) - 1)
    # Combine the prefix and integer portion
    unique_identifier = f"BLR_BFP_{unique_integer:06}"
    return unique_identifier

class IdentifierCounter(models.Model):
    counter = models.IntegerField(default=1)

    def increment_counter(self):
        self.counter += 1
        self.save()
        
def generate_unique_identifier_sequence():
    # Retrieve the IdentifierCounter instance (assuming there's only one row)
    identifier_counter = IdentifierCounter.objects.first()

    if identifier_counter is None:
        # If there's no existing row, create a new one with the default counter value (1)
        identifier_counter = IdentifierCounter()
        identifier_counter.save()

    # Increment the counter to get the next value
    next_counter = identifier_counter.counter
    identifier_counter.increment_counter()

    # Format the next counter value as a string with the desired prefix
    unique_identifier = f"100000{next_counter:02}"
    return unique_identifier
# class BangalorePoiData(models.Model):
#     gid = models.AutoField(primary_key=True)
#     photo_id = models.CharField(max_length=254, blank=True, null=True)
#     poi_id = models.CharField(max_length=254, blank=True, null=True)
#     poi_name = models.CharField(max_length=254, blank=True, null=True)
#     category = models.CharField(max_length=254, blank=True, null=True)
#     sub_cat = models.CharField(max_length=254, blank=True, null=True)
#     contact = models.CharField(max_length=15, blank=True, null=True)
#     mobile = models.CharField(max_length=15, blank=True, null=True)
#     toll_free = models.CharField(max_length=20, blank=True, null=True)
#     poi_email = models.CharField(max_length=254, blank=True, null=True)
#     website = models.CharField(max_length=254, blank=True, null=True)
#     service_ty = models.CharField(max_length=254, blank=True, null=True)
#     is_exist = models.CharField(max_length=254, blank=True, null=True)
#     days_of_wo = models.CharField(max_length=254, blank=True, null=True)
#     parent_chi = models.CharField(max_length=254, blank=True, null=True)
#     parent_id = models.CharField(max_length=254, blank=True, null=True)
#     point_addr = models.CharField(max_length=254, blank=True, null=True)
#     street_roa = models.CharField(max_length=254, blank=True, null=True)
#     secon_sree = models.CharField(max_length=254, blank=True, null=True)
#     locality = models.CharField(max_length=254, blank=True, null=True)
#     sub_locali = models.CharField(max_length=254, blank=True, null=True)
#     landmark = models.CharField(max_length=254, blank=True, null=True)
#     city = models.CharField(max_length=254, blank=True, null=True)
#     postcode = models.FloatField(blank=True, null=True)
#     build_late = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     build_lone = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     collect_on = models.CharField(max_length=254, blank=True, null=True)
#     collect_dt = models.CharField(max_length=254, blank=True, null=True)
#     qil_dmk = models.CharField(max_length=50, blank=True, null=True)
#     remarks = models.CharField(max_length=254, blank=True, null=True)
#     number_1st_open = models.CharField(db_column='1st_open', max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_1st_close = models.CharField(db_column='1st_close', max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_2nd_open = models.CharField(db_column='2nd_open', max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_2nd_close = models.CharField(db_column='2nd_close', max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     frame_1 = models.CharField(max_length=10, blank=True, null=True)
#     frame_2 = models.CharField(max_length=10, blank=True, null=True)
#     frame_3 = models.CharField(max_length=10, blank=True, null=True)
#     POI_Building_Overview = models.ImageField(blank=True, null=True)
#     Signboard = models.ImageField(blank=True, null=True)
#     Phone_Number = models.ImageField(blank=True, null=True)
#     Visiting_Card = models.ImageField(blank=True, null=True)
#     Menu_Brochure = models.ImageField(blank=True, null=True)
#     pro_resour = models.CharField(max_length=25, blank=True, null=True)
#     qc_resourc = models.CharField(max_length=25, blank=True, null=True)
#     type_coll = models.CharField(max_length=25, blank=True, null=True)
#     geom = models.PointField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bangalore_poi_data'


class Bangalore_POI_Updated(models.Model):
    gid = models.AutoField(primary_key=True)
    photo_id = models.CharField(max_length=30, editable=False, null=True)
    poi_id = models.CharField(max_length=30, editable=False, default=generate_unique_identifier_sequence, unique=True)
    poi_name = models.CharField(max_length=254, null=False, blank=False)
    category = models.CharField(max_length=254, blank=True, null=True)
    sub_cat = models.CharField(max_length=254, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    toll_free = models.CharField(max_length=20, blank=True, null=True)
    poi_email = models.CharField(max_length=254, blank=True, null=True) 
    website = models.CharField(max_length=254, blank=True, null=True)
    service_ty = models.CharField(max_length=254, blank=True, null=True)
    is_exist = models.CharField(max_length=254, blank=True, null=True)
    days_of_wo = models.CharField(max_length=254, blank=True, null=True)
    parent_chi = models.CharField(max_length=254, blank=True, null=True)
    parent_id = models.CharField(max_length=254, blank=True, null=True)
    point_addr = models.CharField(max_length=254, blank=True, null=True)
    street_roa = models.CharField(max_length=254, blank=True, null=True)
    secon_sree = models.CharField(max_length=254, blank=True, null=True)
    locality = models.CharField(max_length=254, blank=True, null=True,)
    sub_locali = models.CharField(max_length=254, blank=True, null=True)
    landmark = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    postcode = models.FloatField(blank=True, null=True)
    build_late = models.DecimalField(max_digits=50, decimal_places=14, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    build_lone = models.DecimalField(max_digits=50, decimal_places=14, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    build_late_centroid = models.DecimalField(max_digits=50, decimal_places=14, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    build_lone_centroid = models.DecimalField(max_digits=50, decimal_places=14, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    collect_on = models.DateField(auto_now_add=True, blank=True, null=True)
    collect_dt = models.DateTimeField(default=timezone.now)
    qil_dmk = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=254, blank=True, null=True)
    number_1st_open = models.CharField(max_length=20, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1st_close = models.CharField(max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2nd_open = models.CharField(max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2nd_close = models.CharField(max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    frame_1 = models.CharField(max_length=10, blank=True, null=True)
    frame_2 = models.CharField(max_length=10, blank=True, null=True)
    frame_3 = models.CharField(max_length=10, blank=True, null=True)
    poi_building = models.ImageField(upload_to=upload_to1, storage=MediaStorage(location='poi_building_images'), blank=True, null=True)
    signboard_image = models.ImageField(upload_to=upload_to2, storage=MediaStorage(location='signboard_images'), blank=True, null=True)
    phone_number_image = models.ImageField(upload_to=upload_to3, storage=MediaStorage(location='phone_number_images'), blank=True, null=True)
    menu_brochure_image = models.ImageField(upload_to=upload_to4, storage=MediaStorage(location='menu_brochure_images'), blank=True, null=True)
    visiting_card_image = models.ImageField(upload_to=upload_to5, storage=MediaStorage(location='visiting_card_images'), blank=True, null=True)
    # pro_resour = models.CharField(max_length=25, blank=True, null=True)
    # pro_resour = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING)
    pro_resour = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    qc_resourc = models.CharField(max_length=25, blank=True, null=True)
    type_coll = models.CharField(max_length=25, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    # Override the save method to generate and set the `photo_id` before saving
    def save(self, *args, **kwargs):
        if not self.photo_id:
            # Generate the unique `photo_id` based on some logic (e.g., UUID, timestamp)
            self.photo_id = generate_unique_identifier_sequence()  # Implement this function as required
        super().save(*args, **kwargs)

