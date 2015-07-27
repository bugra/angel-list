import config
import hashlib
import json
import urllib
import urllib2


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
_FOLLOWS_R = '{c_api}/{api}/follows/relationship?source_id={s}&target_type={t}&target_id={t_id}&access_token={at}'
_FOLLOWS_B = '{c_api}/{api}/follows/batch?ids={batch_ids}&access_token={at}'

_STARTUP = '{c_api}/{api}/startups/{id_}?access_token={at}'
_STARTUP_F = '{c_api}/{api}/startups/{id_}/followers?access_token={at}'
_STARTUP_S = '{c_api}/{api}/startups/search?access_token={at}&slug={slug}'
_STARTUP_R = '{c_api}/{api}/startup_roles?v=1&access_token={at}'
_STARTUP_RAISING = '{c_api}/{api}/startups?filter={filter_}&access_token={at}'
_STARTUP_C = '{c_api}/{api}/startups/{id_}/comments?access_token={at}'
_TAGS = '{c_api}/{api}/tags/{id_}/?access_token={at}'
_TAGS_CHILDREN = '{c_api}/{api}/tags/{id_}/children?access_token={at}'
_TAGS_PARENTS = '{c_api}/{api}/tags/{id_}/parents?access_token={at}'
_TAGS_STARTUPS = '{c_api}/{api}/tags/{id_}/startups?access_token={at}'
_TAGS_USERS = '{c_api}/{api}/tags/{id_}/users?access_token={at}'
_STATUS_U = '{c_api}/{api}/status_updates?startup_id={startup_id}&access_token={at}'
_REVIEWS_USER = '{c_api}/{api}/reviews?user_id={user_id}&access_token={at}'
_REVIEW_ID = '{c_api}/{api}/reviews/{id_}?access_token={at}'

_SELF = '{c_api}/{api}/me?access_token={at}'
_USERS = '{c_api}/{api}/users/{id_}?access_token={at}'
_USERS_R = '{c_api}/{api}/users/{id_}/roles?access_token={at}'
_USERS_S = '{c_api}/{api}/users/search?access_token={at}'
_USERS_BATCH = '{c_api}/{api}/users/batch?ids={ids}&access_token={at}'
_S_SEARCH = '{c_api}/{api}/search?query={query}&access_token={at}'
_SLUG_SEARCH = '{c_api}/{api}/search/slugs?query={slug}&access_token={at}'
_COM = '{c_api}/{api}/comments?commentable_type={ct}&commentable_id={id_}&access_token={at}'
_JOBS = '{c_api}/{api}/jobs?page={pg}&access_token={at}'
_JOBS_ID = '{c_api}/{api}/jobs/{id_}'
_STARTUP_ID_JOBS = '{c_api}/{api}/startups/{id_}/jobs'
_TAG_ID_JOBS = '{c_api}/{api}/tags/{id_}/jobs?page={pg}&access_token={at}'
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
    # TODO(try to abstract the url(beginning of it))
    #self.url =

  def get_jobs(self, page=1):
    return _get_request(_JOBS.format(c_api=_C_API_BEGINNING,
                                                     api=_API_VERSION,
                                                      pg=page,
                                                      at=self.access_token))

  def get_job_by_id(self, id_):
    url = _JOBS_ID.format(c_api=_C_API_BEGINNING,
                                                api=_API_VERSION,
                                                id_=id_)
    return _get_request(url)

  def get_startup_jobs(self, id_):
    return _get_request(_STARTUP_ID_JOBS.format(c_api=_C_API_BEGINNING,
                                                        api=_API_VERSION,
                                                        id_=id_,
                                                        at=self.access_token))

  def get_tag_jobs(self, id_,page=1):
    url = _TAG_ID_JOBS.format(c_api=_C_API_BEGINNING,
                                                    api=_API_VERSION,
                                                    id_=id_)
    return _get_request(url)


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
    if user_ids is None and startup_ids is None and direction is None:
      raise Exception('At least one input argument should be different than None')
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
    except (RuntimeError, TypeError, NameError) as e:
      print(e)
      raise NotImplementedError()

  # TODO
  # requires scope "invest"?
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
    except (RuntimeError, TypeError, NameError):
      raise NotImplementedError()

  def post_intros(self, id_, note=None):
    raise NotImplementedError()

  def get_user(self, id_):
    return _get_request(_USERS.format(c_api=_C_API_BEGINNING,
                                              id_=id_,
                                              api=_API_VERSION,
                                              at=self.access_token))

  def get_user_roles(self, id_):
    return _get_request(_USERS_R.format(c_api=_C_API_BEGINNING,
                                                           id_=id_,
                                                           api=_API_VERSION,
                                                           at=self.access_token))

  def get_users_batch(self, ids):
    """
    Ids: a list of ids that we want to return
    """
    # Allowed maximum number of ids is 50
    assert len(ids) <= 50
    ids_ = ','.join(ids)
    url = _USERS_BATCH.format(c_api=_C_API_BEGINNING,
                                              api=_API_VERSION,
                                              ids=ids_,
					      at=self.access_token)
    return _get_request(url)

  # TODO
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

  def get_follows_relationship(self, source_id, target_type, target_id):
    return _get_request(_FOLLOWS_R.format(c_api=_C_API_BEGINNING,
                                                                api=_API_VERSION,
                                                                s=source_id,
                                                                t=target_type,
                                                                t_id=target_id,
                                                                at=self.access_token))

  def get_follows_batch(self, batch_ids):
    return _get_request(_FOLLOWS_B.format(c_api=_C_API_BEGINNING,
                                                               api=_API_VERSION,
                                                               batch_ids=','.join(batch_ids),
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

  # Tags
  def get_tags(self, id_):
    return _get_request(_TAGS.format(c_api=_C_API_BEGINNING,
                                       api=_API_VERSION,
                                       id_=id_,
                                       at=self.access_token))

  def get_tags_children(self, id_):
    return _get_request(_TAGS_CHILDREN.format(c_api=_C_API_BEGINNING,
                                                                      api=_API_VERSION,
                                                                      id_=id_,
                                                                      at=self.access_token))

  def get_tags_parents(self, id_):
    return _get_request(_TAGS_PARENTS.format(c_api=_C_API_BEGINNING,
                                                                      api=_API_VERSION,
                                                                      id_=id_,
                                                                      at=self.access_token))

  def get_tags_startups(self, id_):
    return _get_request(_TAGS_STARTUPS.format(c_api=_C_API_BEGINNING,
                                                                      api=_API_VERSION,
                                                                      id_=id_,
								      at=self.access_token))

  def get_tags_users(self, id_):
    """ Get a particular user which are tagged based on the id_
    """
    return _get_request(_TAGS_USERS.format(c_api=_C_API_BEGINNING,
                                                                      api=_API_VERSION,
                                                                      id_=id_,
                                                                      at=self.access_token))

  # STARTUP Section
  def get_startup(self, id_):
    """ Get startup based on id
    """
    return _get_request(_STARTUP.format(c_api=_C_API_BEGINNING,
                                        api=_API_VERSION,
                                        id_=id_,
                                        at=self.access_token))

  def get_startup_roles(self, user_id=None, startup_id=None, role=None, direction='incoming'):
    """
    user_id ->The user role you want to view
    startup_id -> The startup whose roles you want to view
    role -> The specific role, you'd like to filter ('founder', 'past investor', 'advisor')
    direction ->Either incoming or outgoing
    """

    if user_id is None and startup_id is None:
      raise Exception("You need to provide at least one parameter")
    url = _STARTUP_R.format(c_api=_C_API_BEGINNING,
                                          api=_API_VERSION,
                                          at=self.access_token)
    if user_id is not None:
      url += '&user_id=' + str(user_id)
    if startup_id is not None:
      url += '&startup_id=' + str(startup_id)
    if role is not None:
      url += '&role=' + role
    url += '&direction' + direction
    return _get_request(url)

  def get_startup_comments(self, id_):
    """ Retrieve the comments of a particular startup
    """
    return _get_request(_STARTUP_C.format(c_api=_C_API_BEGINNING,
                                                               api=_API_VERSION,
                                                               id_=id_,
                                                               at=self.access_token))

  def get_startups_filtered_by(self, filter_='raising'):
    """ Get startups based on which companies are raising funding
    """
    url = _STARTUP_RAISING.format(c_api=_C_API_BEGINNING,
                                                                         api=_API_VERSION,
                                                                         filter_=filter_,
                                                                         at=self.access_token)
    return _get_request(url)

  def get_status_updates(self, startup_id):
    """ Get status updates of a startup
    """
    return _get_request(_STATUS_U.format(c_api=_C_API_BEGINNING,
                                                             api=_API_VERSION,
                                                             startup_id=startup_id,
                                                             at=self.access_token))


  # SEARCH Section
  def get_search_for_slugs(self, slug):
    """ Search for a particular slug
    """
    return _get_request(_SLUG_SEARCH.format(c_api=_C_API_BEGINNING,
                                            api=_API_VERSION,
                                            slug=_format_query(slug),
                                            at=self.access_token))


  def get_search(self, query, type_=None):
    """Search for query, type_ is optional.
    type_: 'User', 'Startup', 'MarketTag', 'LocationTag'
    """
    search_url = _S_SEARCH.format(c_api=_C_API_BEGINNING,
                                  api=_API_VERSION,
                                  query=_format_query(query),
                                  at=self.access_token)
    if type_ is not None:
      search_url + _TYPE_SUFFIX.format(type_=type_)
    return _get_request(search_url)


  # Reviews Section
  def get_reviews(self, user_id):
    """ Get reviews for a particular user
    """
    url = _REVIEWS_USER.format(c_api=_C_API_BEGINNING,
                                                api=_API_VERSION,
                                                user_id=user_id,
                                                at=self.access_token)
    return _get_request(url)


  def get_review_id(self, id_):
    """ Get a particular review id, independent from the user_id and
    startup_id
    """
    return _get_request(_REVIEW_ID.format(c_api=_C_API_BEGINNING,
                                                              api=_API_VERSION,
                                                              id_=id_,
                                                              at=self.access_token))


if __name__ == '__main__':
  #angel = AngelList(config.CLIENT_ID, config.CLIENT_SECRET, config.ACCESS_TOKEN)
  pass
