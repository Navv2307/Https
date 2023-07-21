# storage_backends.py

from storages.backends.s3boto3 import S3Boto3Storage

# class MediaStorage(S3Boto3Storage):
#     # Define separate folders for each type of image field
#     location = {
#         'poi_building': 'media/poi_building_images',
#         'signboard_image': 'media/signboard_images',
#         'phone_number_image': 'media/phone_number_images',
#         'menu_brochure_image': 'media/menu_brochure_images',
#         'visiting_card_image': 'media/visiting_card_images',
#     }

#     def __init__(self, *args, **kwargs):
#         self.location = self.location.get(kwargs.get('location', 'media'))
#         super().__init__(*args, **kwargs)

#     def _clean_name(self, name):
#         """
#         Modify the filename to include the folder path.
#         """
#         return f"{self.location}/{super()._clean_name(name)}"

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        self.location = kwargs.pop('location', 'media')  # Get the location from keyword arguments, or set to 'media' by default
        super().__init__(*args, **kwargs)

    def _clean_name(self, name):
        """
        Modify the filename to include the folder path.
        """
        return f"{self.location}/{super()._clean_name(name)}"