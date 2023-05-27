# -*- coding: utf-8 -*-

from landowner.entities.base import AbstractEntity

class Post(AbstractEntity):
    """A Post object representing a single entry from the export data.
    """

    def __init__(self, title="", timestamp=""):
        self.title = title
        self.timestamp = timestamp
        self.media = []

    def add_media(self, media):
        self.media.append(media)


class Media(AbstractEntity):
    """A Media object, typically representing a photo or video
    """

    def __init__(self, uri="", timestamp="", exif_data=""):
        self.uri = uri
        self.timestamp = timestamp
        self.exif_data = exif_data


class ExifData(AbstractEntity):
    """An ExifData object, used for capturing any relevant metadata about Media objects
    """
    def __init__(
            self,
            latitude="",
            longitude="",
            iso="",
            focal_length="",
            lens_model="",
            scene_capture_type="",
            software="",
            device_id="",
            scene_type="",
            camera_position="",
            lens_make="",
            date_time_digitized="",
            date_time_original="",
            source_type="",
            aperture="",
            shutter_speed="",
            metering_mode="",
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.iso = iso
        self.focal_length = focal_length
        self.lens_model = lens_model
        self.scene_capture_type = scene_capture_type
        self.software = software
        self.device_id = device_id
        self.scene_type = scene_type
        self.camera_position = camera_position
        self.lens_make = lens_make
        self.date_time_digitized = date_time_digitized
        self.date_time_original = date_time_original
        self.source_type = source_type
        self.aperture = aperture
        self.shutter_speed = shutter_speed
        self.metering_mode = metering_mode