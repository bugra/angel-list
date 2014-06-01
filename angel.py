import json
import urllib
import urllib2
import hashlib

_API_VERSION = 1

_POST_HEADER = {
               "Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"
              }

_DELETE_HEADER = ['Content-Type', 'text/plain']

_C_API_BEGINNING = 'https://api.angel.co'
_OAUTH_API_BEGINNING = 'https://angel.co/api'

_FOLLOWERS = '{c_api}/{api}/users/{id_}/followers?access_token={at}'
_FOLLOWER_IDS = '{c_api}/{api}/users/{id_}/followers/ids?access_token={at}'
_FOLLOWING = '{c_api}/{api}/users/{id_}/following?access_token={at}'
_FOLLOWING_IDS = '{c_api}/{api}/users/{id_}/following/ids?access_token={at}'
_FEEDS = '{c_api}/{api}/feed?access_token{at}'
_STARTUP = '{c_api}/{api}/startups/{id_}?access_token={at}'
_STARTUP_F = '{c_api}/{api}/startups/{id_}/followers?access_token={at}'
_STARTUP_S = '{c_api}/{api}/startups/search?access_token={at}&slug={slug}'
_S_TAGS = '{c_api}/{api}/tags/{id_}/startups?access_token={at}'

_SELF = '{c_api}/{api}/me?access_token={at}'
_USERS = '{c_api}/{api}/users/{id_}?access_token={at}'
_USERS_S = '{c_api}/{api}/users/search?access_token={at}'
_S_SEARCH = '{c_api}/{api}/search?query={query}'
_SLUG_SEARCH = '{c_api}/{api}/search/slugs?query={slug}'
_COM = '{c_api}/{api}/comments?commentable_type={ct}&commentable_id={id_}'
_JOBS = '{c_api}/{api}/jobs?page={pg}'
_JOBS_ID = '{c_api}/{api}/jobs/{id_}'
_STARTUP_ID_JOBS = '{c_api}/{api}/startups/{id_}/jobs'
_TAG_ID_JOBS = '{c_api}/{api}/tags/{id_}/jobs'
_LIKES = '{c_api}/{api}/likes?likable_type={lt}&likable_id={li}'
_MESSAGES = '{c_api}/{api}/messages?access_token={at}'
_MESSAGES_THREAD = '{c_api}/{api}/messages/{id_}?access_token={at}'
_PATHS = '{c_api}/{api}/paths?access_token={at}'
_PRESS = '{c_api}/{api}/press?access_token={at}&startup_id={id_}'
_PRESS_BY_ID = '{c_api}/{api}/press/{id_}?access_token={at}'
_RESERVATIONS = '{c_api}/{api}/reservations?access_token={at}'
_RESERVATIONS_ID = '{c_api}/{api}/reservations/{id_}?access_token={at}'
_ACCREDIATION = '{c_api}/{api}/accrediation?access_token={at}'
_MD5 = '&md5={md5}'

_PERSONALIZED_SUFFIX = '?personalized=1'
_SINCE_SUFFIX = '&since={since}'
_TYPE_SUFFIX = '&type={type_}'
_USER_IDS_SUFFIX = 'user_ids={user_ids}'
_STARTUP_IDS_SUFFIX = 'startup_ids={startup_ids}'
_DIRECTION_SUFFIX = 'direction={direction}'

_DELETE_METHOD = lambda _: 'DELETE'

"""
Util Functions
"""

def _format_query(query):
  if len(query.split()) > 1:
    query = '+'.join(query.split())
  return query

def _enc_data(data):
  return urllib.urlencode(data)


def _get_request(url):
  return json.loads(urllib2.urlopen(url).read())


def _post_request(url, post_data):
  return json.loads(_get_request(urllib2.Request(url,
                                                 _enc_data(post_data),
                                                 _POST_HEADER)))


def _del_request(url, del_data):
  del_params = _enc_data(del_data)
  request = urllib2.Request(url, del_params)
  request.get_method = _DELETE_METHOD
  request.add_header(*_DELETE_HEADER)
  return json.loads(urrlib2.build_opener(urllib2.HTTPHandler).open(
                                                                request).read())


class AngelList(object):


  def __init__(self, client_id, client_secret, access_token):
    self.client_id = client_id
    self.client_secret = client_secret
    self.access_token = access_token
    # TODO
    #self.url =

  def get_jobs(self, page=1):
    return _get_request(_JOBS.format(c_api=_C_API_BEGINNING,
                                             api=_API_VERSION,
                                             pg=page,
                                             at=self.access_token))

  def get_job_by_id(self, id_):
    return _get_request(_JOBS_ID.format(c_api=_C_API_BEGINNING,
                                                api=_API_VERSION,
                                                id_=id_,
                                                at=self.access_token))

  def get_startup_jobs(self, id_):
    return _get_request(_STARTUP_ID_JOBS.format(c_api=_C_API_BEGINNING,
                                                        api=_API_VERSION,
                                                        id_=id_,
                                                        at=self.access_token))


  def get_tag_jobs(self, id_):
    return _get_request(_TAG_ID_JOBS.format(c_api=_C_API_BEGINNING,
                                                    api=_API_VERSION,
                                                    id_=id_,
                                                    at=self.access_token))


  def get_comments(self, commentable_type, id_):
    """
    commentable_type: 'Press', 'Review', 'Startup', 'StartupRole', 'StatusUpdate'
    """
    return _get_request(_COM.format(c_api=_C_API_BEGINNING,
                                            ct=commentable_type,
                                            id_=id_,
                                            api=_API_VERSION,
                                            at=self.access_token))

  def get_likes(self, likable_type, likable_id):
    """
    likable_type: 'Comment', 'Press', 'Review', 'StartupRole', 'StatusUpdate'
    likable_id: id of the object that the likes of it you are interested
    """
    return _get_request(_LIKES.format(c_api=_C_API_BEGINNING,
                                              api=_API_VERSION,
                                              lt=likable_type,
                                              li=likable_id,
                                              at=self.access_token))

  def post_likes(self, likable_type, likable_id):
    raise NotImplementedError()

  def delete_likes(self, id_):
    raise NotImplementedError()


  def get_messages(self):
    return _get_request(_MESSAGES.format(c_api=_C_API_BEGINNING,
                                                 api=_API_VERSION,
                                                 at=self.access_token))


  def get_messages_by_thread_id(self, id_):
    return _get_request(_MESSAGES_THREAD.format(c_api=_C_API_BEGINNING,
                                                        api=_API_VERSION,
                                                        id_=id_,
                                                        at=self.access_token))


  def post_messages(self, thread_id, recipient_id, body):
    raise NotImplementedError()


  def post_messages_mark(self, thread_ids):
    raise NotImplementedError()


  def get_paths(self, user_ids=None, startup_ids=None, direction=None):
    """
    user_ids: paths between you and these users
    startup_ids: paths between you and these startups
    direction: 'following' or 'followed'
    """
    if isinstance(user_ids, list):
      user_ids = ','.join(list(map(lambda k: str(k), user_ids)))
    if isinstance(startup_ids, list):
      startup_ids = ','.join(list(map(lambda k: str(k), startup_ids)))

    paths_url = _PATHS.format(c_api=_C_API_BEGINNING,
                                      api=_API_VERSION,
                                      at=self.access_token)
    if not user_ids is None:
      paths_url += '&' + _USER_IDS_SUFFIX.format(user_ids=user_ids)
    if not startup_ids is None:
      paths_url += '&' + _STARTUP_IDS_SUFFIX.format(
                                                    startup_ids=startup_ids)
    if not direction is None:
      paths_url += '&' + _DIRECTION_SUFFIX.format(direction=direction)
    print paths_url
    return _get_request(paths_url)


  def get_press(self, startup_id):
    return _get_request(_PRESS.format(c_api=_C_API_BEGINNING,
                                              id_=startup_id,
                                              api=_API_VERSION,
                                              at=self.access_token))


  def get_press_by_id(self, press_id):
    return _get_request(_PRESS_BY_ID.format(c_api=_C_API_BEGINNING,
                                                    id_=press_id,
                                                    api=_API_VERSION,
                                                    at=self.access_token))

  # TODO
  # requires scope "invest" ?
  def get_reservations(self):
    try:
      return _get_request(_RESERVATIONS.format(c_api=_C_API_BEGINNING,
                                                       api=_API_VERSION,
                                                       t=self.access_token))
    except e:
      raise NotImplementedError()


  # requires scope "invest"
  def get_reservations_of_startup(self, id_):
    return _get_request(_RESERVATIONS_ID.format(c_api=_C_API_BEGINNING,
                                                        api=_API_VERSION,
                                                        at=self.access_token))
  # TODO
  def get_accrediation(self):
    try:
    #print(_ACCREDIATION.format(c_api=_C_API_BEGINNING, api=_API_VERSION,
    #                                    at=self.access_token))
      return _get_request(_ACCREDIATION.format(c_api=_C_API_BEGINNING,
                                                     api=_API_VERSION,
                                                     at=self.access_token))
    except e:
      raise NotImplementedError()


  def post_intros(self, id_, note=None):
    raise NotImplementedError()


  def get_users(self, id_):
    return _get_request(_USERS.format(c_api=_C_API_BEGINNING,
                                              id_=id_,
                                              api=_API_VERSION,
                                              at=self.access_token))

  # Not working
  def get_users_by_search(self, slug, email=None):
    request_url = _USERS_S.format(c_api=_C_API_BEGINNING,
                                          api=_API_VERSION,
                                          at=self.access_token)
    if email is not None:
      request_url += _MD5.format(md5=hashlib.md5(email).hexdigest())
    return _get_request(request_url)


  def get_self(self):
    return _get_request(_SELF.format(c_api=_C_API_BEGINNING,
                                             api=_API_VERSION,
                                             at=self.access_token))


  def get_feeds(self, personalized=False, since=None):
    """
    personalized: Feeds for your user
    since: unix timestamp, brings feeds from that time
    """
    feeds_url = _FEEDS.format(c_api=_C_API_BEGINNING,
                                              api=_API_VERSION,
                                              at=self.access_token)
    if personalized:
      feeds_url += _PERSONALIZED_SUFFIX
    if since is not None:
      feeds_url += _SINCE_SUFFIX.format(since=since)
    return _get_request(feeds_url)


  def get_followers(self, id_):
    return _get_request(_FOLLOWERS.format(c_api=_C_API_BEGINNING,
                                                  api=_API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))


  def get_followers_ids(self, id_):
    return _get_request(F_IDS_TEMPLATE.format(c_api=_C_API_BEGINNING,
                                              api=_API_VERSION,
                                              id_=id_,
                                              at=self.access_token))


  def get_following(self, id_):
    return _get_request(_FOLLOWING.format(c_api=_C_API_BEGINNING,
                                                  api=_API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))


  def get_following_ids(self, id_):
    return _get_request(_FOLLOWING_IDS.format(c_api=_C_API_BEGINNING,
                                                 api=_API_VERSION,
                                                 id_=id_,
                                                 at=self.access_token))


  def get_startup_followers(self, id_):
    return _get_request(_STARTUP_F.format(c_api=_C_API_BEGINNING,
                                                  api=_API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))


  def get_startup_followers_ids(self, id_):
    return _get_request(S__FOLLOWER_IDS.format(c_api=_C_API_BEGINNING,
                                                  api=_API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))

  def get_startup(self, id_):
    return _get_request(_STARTUP.format(c_api=_C_API_BEGINNING,
                                                api=_API_VERSION,
                                                id_=id_,
                                                at=self.access_token))

  def get_startup_tags(self, id_):
    return _get_request(_S_TAGS.format(c_api=_C_API_BEGINNING,
                                               api=_API_VERSION,
                                               id_=id_,
                                               at=self.access_token))
  # TODO
  def get_startup_roles(self, id_):
    return _get_request(S_ROLES_TEMPLATE.format(c_api=_C_API_BEGINNING,
                                                api=_API_VERSION,
                                                id_=id_,
                                                at=self.access_token))
  # TODO
  def get_startup_updates(self, id_):
    return _get_request(S_UPDATE_TEMPLATE.format(c_api=_C_API_BEGINNING,
                                                api=_API_VERSION,
                                                id_=id_,
                                                at=self.access_token))

  def get_search_for_slugs(self, slug):
    return _get_request(_SLUG_SEARCH.format(c_api=_C_API_BEGINNING,
                                                    api=_API_VERSION,
                                                    slug=_format_query(slug)))

  def get_search(self, query, type_=None):
    """Search for query, type_ is optional.
    type_: 'User', 'Startup', 'MarketTag', 'LocationTag'
    """
    search_url = _S_SEARCH.format(c_api=_C_API_BEGINNING,
                                          api=_API_VERSION,
                                          query=_format_query(query))
    if type_ is not None:
      search_url + _TYPE_SUFFIX.format(type_=type_)
    return _get_request(search_url)

if __name__ == '__main__':
  # AngelList-Python Application Credentials
  # Learn how to reach these numbers in a smarter way
  #CLIENT_ID = 'SUCH_CLIENT_ID'
  #CLIENT_SECRET = 'VERY_SECRET'
  #ACCESS_TOKEN = 'WOW'
  #angel = AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)
  pass
