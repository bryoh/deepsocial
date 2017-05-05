'''
Module contains class and methods to interact with instagram's API
Each of the classes has quick access attributes such as number of followers, user/media id
'''
import datetime
from pprint import pprint as pp
from datacollection.request_handler import request_handler
time_fmt = "%c"  # because time is very important define it here.
access_token = "42174198.c3c6c77.41a23e7a46cb41879a57fc7197fa3dfd"

# create class User
class User(object):
    """ base class to store urls, user_id, user_search_data etc """
    access_token = "42174198.c3c6c77.41a23e7a46cb41879a57fc7197fa3dfd"
    
    def __init__(self, username=None, media_id=None):
        self.username = username
        self.media_id = media_id
        self.media_id_url = "https://api.instagram.com/v1/media/{}?access_token={}".format(self.media_id, access_token) if media_id is not None else None
        if username is not None:
            search_url = "https://api.instagram.com/v1/users/search?q={}&access_token={}".format(username, self.access_token)
            self.user_search_data = request_handler(search_url, "data")[0]  # requests.get(search_url)
            self.user_id = self.user_search_data['id']

            self.user_info_url = "https://api.instagram.com/v1/users/{}/?access_token={}".format(self.user_id, access_token)
            self.recent_media_url = "https://api.instagram.com/v1/users/{}/media/recent/?access_token={}".format(self.user_id, access_token)
            self.followed_by_url = "https://api.instagram.com/v1/users/{}/followed-by/?access_token={}".format(self.user_id, access_token)
            self.user_info_data = request_handler(self.user_info_url, 'data')


# create class Profile
class Profile(User):
    """
    gets profile infomation such as total following and followers
    profile_item= Profile("bryoh_15")
    print(profile_item.followers)
    print(profile_item.following)
    """
    def __init__(self, username):
        User.__init__(self, username)
        self.name = self.user_search_data["full_name"]
        self.bio = self.user_search_data["bio"]
        self.id = self.user_id
        self.profile_picture_link = self.user_search_data["profile_picture"]
        self.website = self.user_search_data["website"]
        self.counts = self.user_info_data["counts"]
        self.followers = self.counts["followed_by"]
        self.follows = self.counts["follows"]
        self.media_total = self.counts['media']
        self.media_recent_data = request_handler(self.recent_media_url, 'data')
        self.media_recent_obj_list = [Media(media_data=obj) for obj in self.media_recent_data]

    def created_times_fmt(self, time_labels):
        """
        :return a reversed  list of formatted created time, useful for label
        """
        return [datetime.datetime.strptime(obj.created_time, '%c').strftime(time_labels)for obj in self.media_recent_obj_list[::-1]]

    def recent_likes_reversed(self): return [obj.likes for obj in self.media_recent_obj_list[::-1]]


# create class Media
class Media(User):
    """
    Gets media info such as date/time, tags, caption,filter, comments count, etc
    Requires the media-id
    """
    def __init__(self, media_id=None, media_data=None):
        if media_id is not None:
            User.__init__(self, media_id=media_id)
            self.media_data = request_handler(self.media_id_url, 'data')
        if media_data is not None:
            self.media_data = media_data
        self.likes = self.media_data["likes"]['count']
        self.attribution = self.media_data["attribution"]
        self.tags = self.media_data["tags"]
        self.images = self.media_data["images"]
        self.comments = self.media_data["comments"]['count']
        self.media_filter = self.media_data["filter"]
        timestamp = self.media_data["created_time"]
        self.created_time = datetime.datetime.fromtimestamp(float(timestamp)).strftime(time_fmt)
        self.link = self.media_data["link"]
        self.location = self.media_data["location"]
        self.user_has_liked = self.media_data["user_has_liked"]
        self.users_in_photo = self.media_data["users_in_photo"]
        self.caption = self.media_data["caption"]  # ['text']
        self.media_type = self.media_data["type"]
        self.media_id = self.media_data["id"]
        self.media_user = self.media_data["user"]

# create class withMethods for to use with mixin


# consider using mixin

# tests

def test_sanity():    
    user = Profile('bryoh_15')
    assert len(user.media_recent_obj_list) == 20, 'Received 20 objects from instagram '


if __name__ == "__main__":
    import pdb; pdb.set_trace()
    bryoh = Profile('bryoh_15')
    pp( bryoh.__dict__ )

