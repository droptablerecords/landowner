# -*- coding: utf-8 -*-
# Objects representing exported data
import json
from landowner.entities.base import AbstractEntity

class Post(AbstractEntity):   
    def __init__(self, title="", timestamp=""):
        self.title = title
        self.timestamp = timestamp
        self.data = PostData()
        self.tags = []
        self.attachments = []

class Tag(AbstractEntity):   
    def __init__(self, name=""):
        self.name = name

    def __str__(self) -> str:
        return self.name


class PostData(AbstractEntity):
    def __init__(self, text="", update_timestamp=""):
        self.text = text
        self.update_timestamp = update_timestamp

    def __repr__(self):
        return self.toJSON()

class TextAttachment(AbstractEntity):
    def __init__(self, text=""):
        self.text = text


class Media(AbstractEntity):
    """A Media object, typically representing a photo or video
    """
    def __init__(self="", uri="", title="", description="", timestamp="", exif_data=""):
        self.uri = uri
        self.title = title
        self.description = description
        self.timestamp = timestamp
        self.exif_data = exif_data


class Place(AbstractEntity):
    def __init__(self, latitude="", longitude="", name="", address="", url=""):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.address = address
        self.url = url


class Event(AbstractEntity):
    def __init__(
            self,
            name="",
            start_timestamp="",
            end_timestamp="",
            description="",
            create_timestamp="",
            place=""
            ):
        self.name = name
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.description = description
        self.create_timestamp = create_timestamp
        self.place = place


class ExternalContext(AbstractEntity):
    def __init__(self, name="", source="", url=""):
        self.name = name
        self.source = source
        self.url = url


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
            upload_ip="",
            taken_timestamp="",
            orientation="",
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
        self.upload_ip = upload_ip
        self.taken_timestamp = taken_timestamp
        self.orientation = orientation