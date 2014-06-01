import json
import urllib
import urllib2
import hashlib

API_VERSION = 1

POST_HEADER = {
               "Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"
              }

DELETE_HEADER = ['Content-Type', 'text/plain']

COMMON_API_BEGINNING = 'https://api.angel.co'
OAUTH_API_BEGINNING = 'https://angel.co/api'

FOLLOWERS_TEMPLATE = '{c_api}/{api}/users/{id_}/followers?access_token={at}'
FER_IDS_TEMPLATE = '{c_api}/{api}/users/{id_}/followers/ids?access_token={at}'
FOLLOWING_TEMPLATE = '{c_api}/{api}/users/{id_}/following?access_token={at}'
FING_IDS_TEMPLATE = '{c_api}/{api}/users/{id_}/following/ids?access_token={at}'
FEEDS_TEMPLATE = '{c_api}/{api}/feed?access_token{at}'
STARTUP_TEMPLATE = '{c_api}/{api}/startups/{id_}?access_token={at}'
STARTUP_F_TEMPLATE = '{c_api}/{api}/startups/{id_}/followers?access_token={at}'
STARTUP_S_TEMPLATE = '{c_api}/{api}/startups/search?access_token={at}&slug={slug}'
S_TAGS_TEMPLATE = '{c_api}/{api}/tags/{id_}/startups?access_token={at}'

SELF_TEMPLATE = '{c_api}/{api}/me?access_token={at}'
USERS_TEMPLATE = '{c_api}/{api}/users/{id_}?access_token={at}'
USERS_S_TEMPLATE = '{c_api}/{api}/users/search?access_token={at}'
S_SEARCH_TEMPLATE = '{c_api}/{api}/search?query={query}'
SLUG_SEARCH_TEMPLATE = '{c_api}/{api}/search/slugs?query={slug}'
COM_TEMPLATE = '{c_api}/{api}/comments?commentable_type={ct}&commentable_id={id_}'
JOBS_TEMPLATE = '{c_api}/{api}/jobs?page={pg}'
JOBS_ID_TEMPLATE = '{c_api}/{api}/jobs/{id_}'
STARTUP_ID_JOBS_TEMPLATE = '{c_api}/{api}/startups/{id_}/jobs'
TAG_ID_JOBS_TEMPLATE = '{c_api}/{api}/tags/{id_}/jobs'
LIKES_TEMPLATE = '{c_api}/{api}/likes?likable_type={lt}&likable_id={li}'
MESSAGES_TEMPLATE = '{c_api}/{api}/messages?access_token={at}'
MESSAGES_THREAD_TEMPLATE = '{c_api}/{api}/messages/{id_}?access_token={at}'
PATHS_TEMPLATE = '{c_api}/{api}/paths?access_token={at}'
PRESS_TEMPLATE = '{c_api}/{api}/press?access_token={at}&startup_id={id_}'
PRESS_BY_ID_TEMPLATE = '{c_api}/{api}/press/{id_}?access_token={at}'
RESERVATIONS_TEMPLATE = '{c_api}/{api}/reservations?access_token={at}'
RESERVATIONS_ID_TEMPLATE = '{c_api}/{api}/reservations/{id_}?access_token={at}'
ACCREDIATION_TEMPLATE = '{c_api}/{api}/accrediation?access_token={at}'
MD5_TEMPLATE = '&md5={md5}'

PERSONALIZED_SUFFIX_TEMPLATE = '?personalized=1'
SINCE_SUFFIX_TEMPLATE = '&since={since}'
TYPE_SUFFIX_TEMPLATE = '&type={type_}'
USER_IDS_SUFFIX_TEMPLATE = 'user_ids={user_ids}'
STARTUP_IDS_SUFFIX_TEMPLATE = 'startup_ids={startup_ids}'
DIRECTION_SUFFIX_TEMPLATE = 'direction={direction}'

GET_METHOD = lambda _: 'GET'
POST_METHOD = lambda _: 'POST'
DELETE_METHOD = lambda _: 'DELETE'


def _format_query(query):
  if len(query.split()) > 1:
    query = '+'.join(query.split())
  return query

def _enc_data(data):
  return urllib.urlencode(data)


def _get_request(url):
  return json.loads(urllib2.urlopen(url).read())


def _post_request(url, post_data):
  return json.loads(_get_request(
                            urllib2.Request(url, _enc_data(post_data), POST_HEADER)))


def _del_request(url, del_data):
  del_params = _enc_data(del_data)
  request = urllib2.Request(url, del_params)
  request.get_method = DELETE_METHOD
  request.add_header(*DELETE_HEADER)
  return json.loads(urrlib2.build_opener(urllib2.HTTPHandler).open(request).read())


class AngelList(object):


  def __init__(self, client_id, client_secret, access_token):
    self.client_id = client_id
    self.client_secret = client_secret
    self.access_token = access_token
    # TODO
    #self.url =

  def get_jobs(self, page=1):
    return _get_request(JOBS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                             api=API_VERSION,
                                             pg=page,
                                             at=self.access_token))

  def get_job_by_id(self, id_):
    return _get_request(JOBS_ID_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                api=API_VERSION,
                                                id_=id_,
                                                at=self.access_token))

  def get_startup_jobs(self, id_):
    return _get_request(STARTUP_ID_JOBS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                        api=API_VERSION,
                                                        id_=id_,
                                                        at=self.access_token))


  def get_tag_jobs(self, id_):
    return _get_request(TAG_ID_JOBS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                    api=API_VERSION,
                                                    id_=id_,
                                                    at=self.access_token))


  def get_comments(self, commentable_type, id_):
    """
    commentable_type: 'Press', 'Review', 'Startup', 'StartupRole', 'StatusUpdate'
    """
    return _get_request(COM_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                            ct=commentable_type,
                                            id_=id_,
                                            api=API_VERSION,
                                            at=self.access_token))

  def get_likes(self, likable_type, likable_id):
    """
    likable_type: 'Comment', 'Press', 'Review', 'StartupRole', 'StatusUpdate'
    likable_id: id of the object that the likes of it you are interested
    """
    return _get_request(LIKES_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                              api=API_VERSION,
                                              lt=likable_type,
                                              li=likable_id,
                                              at=self.access_token))

  def post_likes(self, likable_type, likable_id):
    raise NotImplementedError()

  def delete_likes(self, id_):
    raise NotImplementedError()


  def get_messages(self):
    return _get_request(MESSAGES_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                 api=API_VERSION,
                                                 at=self.access_token))


  def get_messages_by_thread_id(self, id_):
    return _get_request(MESSAGES_THREAD_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                        api=API_VERSION,
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

    paths_url = PATHS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                      api=API_VERSION,
                                      at=self.access_token)
    if not user_ids is None:
      paths_url += '&' + USER_IDS_SUFFIX_TEMPLATE.format(user_ids=user_ids)
    if not startup_ids is None:
      paths_url += '&' + STARTUP_IDS_SUFFIX_TEMPLATE.format(startup_ids=startup_ids)
    if not direction is None:
      paths_url += '&' + DIRECTION_SUFFIX_TEMPLATE.format(direction=direction)
    print paths_url
    return _get_request(paths_url)


  def get_press(self, startup_id):
    return _get_request(PRESS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                              id_=startup_id,
                                              api=API_VERSION,
                                              at=self.access_token))


  def get_press_by_id(self, press_id):
    return _get_request(PRESS_BY_ID_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                    id_=press_id,
                                                    api=API_VERSION,
                                                    at=self.access_token))

  # TODO
  # requires scope "invest" ?
  def get_reservations(self):
    return _get_request(RESERVATIONS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                     api=API_VERSION,
                                                     at=self.access_token))

  # requires scope "invest"
  def get_reservations_of_startup(self, id_):
    return _get_request(RESERVATIONS_ID_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                        api=API_VERSION,
                                                        at=self.access_token))

  def get_accrediation(self):
    print(ACCREDIATION_TEMPLATE.format(c_api=COMMON_API_BEGINNING, api=API_VERSION,
                                        at=self.access_token))
    return _get_request(ACCREDIATION_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                     api=API_VERSION,
                                                     at=self.access_token))
  def post_intros(self, id_, note=None):
    raise NotImplementedError()


  def get_users(self, id_):
    return _get_request(USERS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                              id_=id_,
                                              api=API_VERSION,
                                              at=self.access_token))

  # Not working
  def get_users_by_search(self, slug, email=None):
    request_url = USERS_S_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                          api=API_VERSION,
                                          at=self.access_token)
    if email is not None:
      request_url += MD5_TEMPLATE.format(md5=hashlib.md5(email).hexdigest())
    return _get_request(request_url)


  def get_self(self):
    return _get_request(SELF_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                             api=API_VERSION,
                                             at=self.access_token))


  def get_feeds(self, personalized=False, since=None):
    """
    personalized: Feeds for your user
    since: unix timestamp, brings feeds from that time
    """
    feeds_url = FEEDS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                              api=API_VERSION,
                                              at=self.access_token)
    if personalized:
      feeds_url += PERSONALIZED_SUFFIX_TEMPLATE
    if since is not None:
      feeds_url += SINCE_SUFFIX_TEMPLATE.format(since=since)
    return _get_request(feeds_url)


  def get_followers(self, id_):
    return _get_request(FOLLOWERS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                  api=API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))


  def get_followers_ids(self, id_):
    return _get_request(F_IDS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                              api=API_VERSION,
                                              id_=id_,
                                              at=self.access_token))


  def get_following(self, id_):
    return _get_request(FOLLOWING_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                  api=API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))


  def get_following_ids(self, id_):
    return _get_request(FING_IDS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                 api=API_VERSION,
                                                 id_=id_,
                                                 at=self.access_token))


  def get_startup_followers(self, id_):
    return _get_request(STARTUP_F_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                  api=API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))


  def get_startup_followers_ids(self, id_):
    return _get_request(S_FER_IDS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                  api=API_VERSION,
                                                  id_=id_,
                                                  at=self.access_token))

  def get_startup(self, id_):
    return _get_request(STARTUP_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                api=API_VERSION,
                                                id_=id_,
                                                at=self.access_token))

  def get_startup_tags(self, id_):
    return _get_request(S_TAGS_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                               api=API_VERSION,
                                               id_=id_,
                                               at=self.access_token))
  # TODO
  def get_startup_roles(self, id_):
    return _get_request(S_ROLES_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                api=API_VERSION,
                                                id_=id_,
                                                at=self.access_token))
  # TODO
  def get_startup_updates(self, id_):
    return _get_request(S_UPDATE_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                api=API_VERSION,
                                                id_=id_,
                                                at=self.access_token))

  def get_search_for_slugs(self, slug):
    return _get_request(SLUG_SEARCH_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                                    api=API_VERSION,
                                                    slug=_format_query(slug)))

  def get_search(self, query, type_=None):
    """Search for query, type_ is optional.
    type_: 'User', 'Startup', 'MarketTag', 'LocationTag'
    """
    search_url = S_SEARCH_TEMPLATE.format(c_api=COMMON_API_BEGINNING,
                                          api=API_VERSION,
                                          query=_format_query(query))
    if type_ is not None:
      search_url + TYPE_SUFFIX_TEMPLATE.format(type_=type_)
    return _get_request(search_url)

if __name__ == '__main__':
  # AngelList-Python Application Credentials
  # Learn how to reach these numbers in a smarter way
  #CLIENT_ID = 'SUCH_CLIENT_ID'
  #CLIENT_SECRET = 'VERY_SECRET'
  #ACCESS_TOKEN = 'WOW'
  #angel = AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)
  pass
