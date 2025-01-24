# -*- coding: utf-8 -*-

from .base import SocialMediaExportDeserializer
from ..entities import facebook as Facebook

class FacebookPostExportDeserializer(SocialMediaExportDeserializer):

    def __init__(self):
        super().__init__()

    def _extract_event_attachment(self, event_dict):
        event_object = Facebook.Event()
        for key in event_dict:
            if hasattr(event_object, key):
                if key == "place":
                    place_attribute_object = Facebook.Place()
                    place_attribute_object.name = event_dict[key].get('name')
                    if "coordinate" in event_dict[key]:
                        place_attribute_object.latitude = event_dict[key]['coordinate'].get('latitude')
                        place_attribute_object.longitude = event_dict[key]['coordinate'].get('longitude')
                    else:
                        pass
                    setattr(event_object, key, place_attribute_object)
                else:
                    setattr(event_object, key, event_dict[key])
        return event_object


    def _extract_external_context_attachment(self, external_context_dict):
        external_context_object = Facebook.ExternalContext()
        for attribute in external_context_dict:
            if hasattr(external_context_object, attribute):
                setattr(external_context_object, attribute, external_context_dict[attribute])
        return external_context_object


    def _extract_media_attachment(self, media_dict):
        md_uri = media_dict.get('uri')
        md_title = self._sanitize_string_value(media_dict.get('title')) if isinstance(media_dict.get('title'), str) else ""
        md_description = self._sanitize_string_value(media_dict.get('description')) if isinstance(media_dict.get('description'), str) else ""
        md_timestamp = media_dict.get('creation_timestamp')
        
        # Create an empty ExifData object.
        exif_data_object = Facebook.ExifData()
        
        # Not all entries contain metadata.
        if 'media_metadata' in media_dict:
            
            # If the media item is a video, its URI will contain the substring ".mp4" in it.
            #  The metadata for videos and photos exists at different locations.
            metadata_key = 'video_metadata' if '.mp4' in md_uri else 'photo_metadata'
            
            # Only attempt to set values that are in the data.
            #   Not every post has every piece of possible metadata.
            media_exif_data_dict = media_dict['media_metadata'][metadata_key]['exif_data'][0]
            for attribute in media_exif_data_dict:
                if hasattr(exif_data_object, attribute):
                    setattr(exif_data_object, attribute, media_exif_data_dict.get(attribute))
        
        media_object = Facebook.Media(md_uri, md_title, md_description, md_timestamp, exif_data_object)
        return media_object

    
    def _extract_post_data(self, data_list):
        post_data_object = Facebook.PostData()
        for list_item in data_list:
            if 'post' in list_item:
                text_data = list_item.get('post')
                post_data_object.text = self._sanitize_string_value(text_data) if isinstance(text_data, str) else ""
            else:
                pass
            if 'update_timestamp' in list_item:
                post_data_object.update_timestamp = list_item.get('update_timestamp')
            else:
                pass
        return post_data_object

    
    def _extract_place_attachment(self, place_dict):
        place_object = Facebook.Place()
        for key in ['name', 'address', 'url']:
            if key in place_dict:
                setattr(place_object, key, place_dict[key])
                if "coordinate" in place_dict:
                    place_data_coordinate = place_dict['coordinate']
                    for coordinate in ['latitude', 'longitude']:
                        setattr(place_object, coordinate, place_data_coordinate[coordinate])
        return place_object


    def _extract_text_attachment(self, attachment_data_item):
        sanitized_text_value = self._sanitize_string_value(attachment_data_item['text'])
        return Facebook.TextAttachment(sanitized_text_value)

    def _sanitize_string_value(self, value):
        if isinstance(value, str):
            try:
                # Attempt to decode the string using 'latin-1' encoding first, then encode it back to 'utf-8'
                return value.encode('latin-1').decode('utf-8')
            except (UnicodeEncodeError, UnicodeDecodeError):
                try:
                    return value.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
                except (UnicodeEncodeError, UnicodeDecodeError):
                    return value
        return value
    
    def deserialize(self, data):
        posts = []
        for item in data:
            # DEBUG
            # print(f"About to process item with timestamp: {item['timestamp']}")
            post = Facebook.Post()
            post.title = self._sanitize_string_value(item.get('title')) if isinstance(item.get('title'), str) else ""
            post.timestamp = item.get('timestamp')

            if "data" in item:
                post.data = self._extract_post_data(item.get('data'))
            else:
                pass

            if "tags" in item:
                for item_tag in item['tags']:
                    tag = Facebook.Tag(item_tag.get('name'))
                    post.tags.append(tag)
            else:
                pass

            if "attachments" in item:
                for attachment in item['attachments']:
                    if "data" in attachment:
                        for attachment_data_item in attachment['data']:
                            if "text" in attachment_data_item:
                                text_attachment = Facebook.TextAttachment(attachment_data_item['text'])
                                post.attachments.append(text_attachment)
                            else:
                                pass

                            if "media" in attachment_data_item:
                                media_dict = attachment_data_item['media']
                                media_object = self._extract_media_attachment(media_dict)
                                post.attachments.append(media_object)
                            else:
                                pass

                            if "place" in attachment_data_item:
                                place_dict = attachment_data_item['place']
                                place_object = self._extract_place_attachment(place_dict)
                                post.attachments.append(place_object)
                            else:
                                pass

                            if "event" in attachment_data_item:
                                event_dict = attachment_data_item['event']
                                event_object = self._extract_event_attachment(event_dict)
                                post.attachments.append(event_object)
                            else:
                                pass

                            if "external_context" in attachment_data_item:
                                external_context_dict = attachment_data_item['external_context']
                                external_context_object = self._extract_external_context_attachment(external_context_dict)
                                post.attachments.append(external_context_object)
                            else:
                                pass
            posts.append(post)
        return posts