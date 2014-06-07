import unittest

import angel
# Put your credentials into config.py
# in the following format
"""
CLIENT_ID =
CLIENT_SECRET =
ACCESS_TOKEN =

### If you want to test your profile (test_self())
### Fill the credentials with the information
### on your angellist account

MY_NAME =
TWITTER_URL =
ONLINE_BIO_URL =
LINKEDIN_URL =
GITHUB_URL =
EMAIL =
ANGELLIST_URL =
ID =
"""

import config

MY_ID = str(config.ID)
VIACOM_ID = '40744'
WHATSAPP_ID = '78902'
UBER_ID = '19163'
AIRBNN_ID = '32677'
KARMA_ID = '29741'
CB_INSIGHTS_ID = '344401'
ANGELLIST_ID = '6702'

angel = angel.AngelList(config.CLIENT_ID,
                        config.CLIENT_SECRET,
                        config.ACCESS_TOKEN
                       )


class AngelListTestCase(unittest.TestCase):


  def set_up(self):
    pass


  def tear_down(self):
    pass


  def test_self(self):
    self_ = angel.get_self()
    assert self_['name'] == config.MY_NAME
    assert self_['twitter_url'] == config.TWITTER_URL
    assert self_['online_bio_url'] == config.ONLINE_BIO_URL
    assert self_['linkedin_url'] == config.LINKEDIN_URL
    assert self_['github_url'] == config.GITHUB_URL
    assert self_['email'] == config.EMAIL
    assert self_['angellist_url'] == config.ANGELLIST_URL
    assert int(self_['id']) == config.ID


  def test_search_for_slugs(self):
    slug_ = angel.get_search_for_slugs('karma')
    assert int(slug_['id']) == 29741
    assert slug_['name'] == 'Karma'
    assert slug_['type'] == 'Startup'
    assert slug_['url'] == 'https://angel.co/karma'


  def test_search(self):
    # Get the first item of the list
    # Check if the search of angel list actually works
    search_ = angel.get_search('cb insights')
    s_ = search_[0]
    assert type(search_) == list
    assert type(s_) == dict
    assert int(s_['id']) == 344401
    assert s_['name'] == 'CB Insights'
    assert s_['type'] == 'Startup'
    assert s_['url'] == 'https://angel.co/cb-insights-1'


  def test_users_batch(self):
    n = 30
    ids = list(map(lambda k: str(k), range(n)))
    batch_ = angel.get_users_batch(ids)
    assert len(batch_) <= n
    keys = [u'dribbble_url', u'image', u'locations', u'id', u'angellist_url', u'what_ive_built', u'what_i_do', u'follower_count', u'bio', u'online_bio_url', u'twitter_url', u'facebook_url', u'criteria', u'aboutme_url', u'investor', u'name', u'roles', u'skills', u'linkedin_url', u'github_url', u'behance_url', u'blog_url']
    if batch_ and len(batch_) > 0:
      print(batch_[0].keys())
      assert sorted(list(batch_[0].iterkeys())) == sorted(keys)


  def test_comments(self):
    comments_ = angel.get_comments('Startup', KARMA_ID)
    assert type(comments_) == list
    assert type(comments_[0]) == dict
    assert len(comments_) > 6


  def test_jobs(self):
    # Test two pages
    for pg in [1, 2]:
      jobs_ = angel.get_jobs(page=pg)
      expected_job_keys = sorted(['per_page', 'last_page', 'total', 'jobs', 'page'])
      assert type(jobs_) == dict
      assert expected_job_keys == sorted(list(jobs_.iterkeys()))


  def test_job_by_id(self):
    j_ = angel.get_job_by_id(97)
    assert type(j_) == dict
    assert int(j_['id']) == 97
    assert j_['angellist_url'] == 'https://angel.co/jobs?startup_id=6702'
    assert j_['created_at'] == '2011-12-05T21:05:43Z'
    assert j_['currency_code'] == 'USD'
    assert float(j_['equity_cliff']) == 1.0
    assert float(j_['equity_max']) == 0.2
    assert float(j_['equity_min']) == 0.2
    assert float(j_['equity_vest']) == 6.0
    assert int(j_['salary_max']) == 150000
    assert int(j_['salary_min']) == 120000
    # Make sure that the resulting data structure is a data type
    assert type(j_['startup']) == dict


  def test_startup_jobs(self):
    jobs_ = angel.get_startup_jobs(6702)
    j_ = jobs_[0]
    assert type(j_) == dict
    assert int(j_['id']) == 97
    assert j_['angellist_url'] == 'https://angel.co/jobs?startup_id=6702'
    assert j_['created_at'] == '2011-12-05T21:05:43Z'
    assert j_['currency_code'] == 'USD'
    assert float(j_['equity_cliff']) == 1.0
    assert float(j_['equity_max']) == 0.2
    assert float(j_['equity_min']) == 0.2
    assert float(j_['equity_vest']) == 6.0
    assert int(j_['salary_max']) == 150000
    assert int(j_['salary_min']) == 120000
    # Make sure that the resulting data structure is a data type
    assert type(j_['startup']) == dict


  def test_tag_jobs(self):
    jobs_ = angel.get_tag_jobs(1692)
    assert type(jobs_) == dict
    assert type(jobs_['jobs']) == list
    expected_job_keys = sorted(['per_page', 'last_page', 'total', 'jobs', 'page'])
    assert sorted(expected_job_keys) == sorted(list(jobs_.iterkeys()))


  def test_likes(self):
    likes_ = angel.get_likes('Comment', 3800)
    expected_job_keys = sorted(['per_page', 'last_page', 'total', 'likes', 'page'])
    assert sorted(expected_job_keys) == sorted(list(likes_.iterkeys()))
    assert type(likes_['likes']) == list


  def test_messages(self):
    m_ = angel.get_messages()
    expected_message_keys = sorted(['per_page', 'last_page', 'total', 'messages', 'page'])
    assert sorted(list(m_.iterkeys())) == expected_message_keys


  def test_press(self):
    for id_ in [ANGELLIST_ID, CB_INSIGHTS_ID]:
      m_ = angel.get_press(id_)
      expected_message_keys = sorted(['per_page', 'last_page', 'total', 'press', 'page'])
      assert sorted(list(m_.iterkeys())) == expected_message_keys


  def test_press_id(self):
    expected_keys = sorted(['title', 'url', 'created_at', 'updated_at', 'id', 'snippet', 'owner_type', 'posted_at', 'owner_id'])
    p_ = angel.get_press_by_id(990)
    assert sorted(list(p_.iterkeys())) == expected_keys
    assert int(p_['id']) == 990
    assert p_['owner_id'] == 89289
    assert p_['url'] == 'http://goaleurope.com/2012/04/11/introducing-ukranian-accelerator-eastlabs-and-its-first-teams/'
    assert p_['updated_at'] == '2012-05-10T17:10:23Z'
    assert p_['created_at'] == '2012-05-10T17:10:23Z'
    assert p_['title'] == 'Startup news from Ukraine: gift selection service ActiveGift launches today'
    assert p_['snippet'] == 'Introducing Ukranian accelerator Eastlabs and its first teams'
    assert p_['posted_at'] == '2012-04-11'
    assert p_['owner_type'] == 'Startup'


  def test_startup_roles(self):
    # Companies that Andreesseen Horowitz is tagged in
    # https://angel.co/api/spec/startups#GET_startups_%3Aid_roles
    id_ = 37820
    direction_ = 'outgoing'
    a16z_ = angel.get_startup_roles(id_, direction=direction_)
    keys = sorted(['per_page', 'last_page', 'total', 'startup_roles', 'page'])
    assert sorted(list(a16z_.iterkeys())) == keys
    a_ = a16z_['startup_roles'][0]
    assert 'startup' in a_
    c_ = a_['startup']
    assert c_['angellist_url'] == 'https://angel.co/andreessen-horowitz'
    assert c_['company_url'] == 'http://www.a16z.com/'
    assert c_['high_concept'] == 'Helping the greatest tech entrepreneurs build the best tech companies'
    assert c_['name'] == 'Andreessen Horowitz'
    assert int(c_['quality']) == 10


  def test_startup_comments(self):
    id_ = 6702
    c_ = angel.get_startup_comments(id_)
    comment_keys = sorted(['comment', 'created_at', 'id', 'user'])
    assert type(c_) == list
    if c_ and len(c_) > 0:
      f_ = c_[0] # first comment
      assert sorted(list(f_.iterkeys())) == comment_keys
      # Need to change
      # I do not know which order Angellist sends these comments
      # If there does not a particular order exist, or the order does not
      # depend on the comment created time
      # Then the following test may not work and become meaningless
      assert f_['comment'] == "AngelList is badass! Thank you guys, you are changing the way companies get funded and that's awesome!"
      assert f_['created_at'] == '2011-08-05T06:07:50Z'
      assert int(f_['id']) == 3800
      assert f_['user']['angellist_url'] == 'https://angel.co/thomask'
      assert f_['user']['bio'] == 'Founder of @angelpad, Ex-@Google Product Manager, Startup Advisor, Angel Investor http://angelpad.org/b/scoble-thomas-korte-2012/'
      # Based on the assumption: followers will only increase
      assert int(f_['user']['follower_count']) >= 11175
      assert int(f_['user']['id']) == 111
      assert f_['user']['name'] == 'Thomas Korte'


  def test_startups_filtered_by(self, filter_='raising'):
    expected_keys = sorted(['last_page', 'per_page', 'startups', 'total', 'page'])
    s_ = angel.get_startups_filtered_by(filter_=filter_)
    assert type(s_) == dict
    assert sorted(list(s_.iterkeys())) == expected_keys
    i_ = s_['startups'][0]
    expected_keys = sorted(['status', 'crunchbase_url', 'fundraising', 'video_url', 'company_url', 'company_type', 'locations', 'quality',
                                          'id', 'angellist_url', 'screenshots', 'follower_count', 'hidden', 'launch_date', 'markets', 'community_profile',
                                          'product_desc', 'twitter_url', 'high_concept', 'updated_at', 'thumb_url', 'company_size', 'logo_url', 'name',
                                          'created_at', 'blog_url'])
    assert sorted(list(i_.iterkeys())) == expected_keys


  def test_startup_roles(self):
    # Only Startup id
    startup_id = 6702
    s_ = angel.get_startup_roles(startup_id=startup_id)
    expected_keys = sorted(['per_page', 'last_page', 'total', 'startup_roles', 'page'])
    assert type(s_) == dict
    assert sorted(list(s_.iterkeys())) == expected_keys
    assert type(s_['startup_roles']) == list
    t_ = s_['startup_roles'][0]
    e = sorted(['confirmed', 'ended_at', 'title', 'created_at', 'startup', 'tagged', 'role', 'started_at', 'id'])
    assert e == sorted(list(t_.iterkeys()))
    # Direction Test
    direction = 'outgoing'
    s_ = angel.get_startup_roles(startup_id=startup_id, direction=direction)
    assert type(s_) == dict
    assert sorted(list(s_.iterkeys())) == expected_keys
    assert type(s_['startup_roles']) == list
    t_ = s_['startup_roles'][0]
    assert e == sorted(list(t_.iterkeys()))

    # Roles Test
    s_ = angel.get_startup_roles(startup_id=startup_id, role='founder')
    assert type(s_) == dict
    assert sorted(list(s_.iterkeys())) == expected_keys
    assert type(s_['startup_roles']) == list
    t_ = s_['startup_roles'][0]
    assert e == sorted(list(t_.iterkeys()))
    s_ = angel.get_startup_roles(startup_id=startup_id, role='advisor')
    assert type(s_) == dict
    assert sorted(list(s_.iterkeys())) == expected_keys
    assert type(s_['startup_roles']) == list
    t_ = s_['startup_roles'][0]
    assert e == sorted(list(t_.iterkeys()))

    # User id test
    s_ = angel.get_startup_roles(user_id=2)
    assert type(s_) == dict
    assert sorted(list(s_.iterkeys())) == expected_keys
    assert type(s_['startup_roles']) == list
    t_ = s_['startup_roles'][0]
    assert e == sorted(list(t_.iterkeys()))


  def test_startup_roles_deprecated(self, id_=2674):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'startup_roles', 'page'])
    directions = ['incoming', 'outgoing']
    for direction in directions:
      r_ = angel.get_startup_roles_deprecated(id_, direction=direction)
      assert type(r_) == dict
      assert expected_keys == sorted(list(r_.iterkeys()))
      roles_ = r_['startup_roles']
      assert type(roles_) == list
      p_ = roles_[0]
      e = sorted(['confirmed', 'ended_at', 'title', 'created_at', 'startup', 'tagged', 'role', 'started_at', 'id'])
      assert e == sorted(list(p_.iterkeys()))


  def test_status_updates(self, startup_id=6702):
    expected_keys = sorted(['total', 'per_page', 'last_page', 'status_updates', 'page'])
    u_ = angel.get_status_updates(startup_id)
    assert type(u_) == dict
    assert sorted(list(u_.iterkeys())) == expected_keys
    up_ = u_['status_updates']
    assert type(up_) == list
    p_ = up_[0]
    assert type(p_) == dict
    e = sorted(['created_at', 'message', 'id'])
    assert sorted(list(p_.iterkeys())) == e


  def test_tags(self, startup_id=1654):
    expected_keys = sorted(['statistics', 'display_name', 'name', 'angellist_url', 'id', 'tag_type'])
    t_ = angel.get_tags(startup_id)
    assert type(t_) == dict
    assert sorted(list(t_.iterkeys())) == expected_keys
    assert type(t_['statistics']) == dict
    assert sorted(list(t_['statistics'].iterkeys())) == sorted(['all', 'direct'])


  def test_tags_children(self, startup_id=1654):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'children', 'page'])
    c_ = angel.get_tags_children(startup_id)
    assert type(c_) == dict
    assert sorted(list(c_.iterkeys())) == expected_keys
    assert type(c_['children']) == list
    assert type(c_['per_page']) == int
    assert type(c_['last_page']) == int
    assert type(c_['total']) == int
    assert type(c_['page']) == int


  def test_tags_parents(self, startup_id=1688):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'parents', 'page'])
    c_ = angel.get_tags_parents(startup_id)
    assert type(c_) == dict
    assert sorted(list(c_.iterkeys())) == expected_keys
    assert type(c_['parents']) == list
    assert type(c_['per_page']) == int
    assert type(c_['last_page']) == int
    assert type(c_['total']) == int
    assert type(c_['page']) == int


  def test_tags_startups(self, startup_id=1688):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'startups', 'page'])
    c_ = angel.get_tags_startups(startup_id)
    assert type(c_) == dict
    assert sorted(list(c_.iterkeys())) == expected_keys
    assert type(c_['startups']) == list
    assert type(c_['per_page']) == int
    assert type(c_['last_page']) == int
    assert type(c_['total']) == int
    assert type(c_['page']) == int


  def test_tags_users(self, startup_id=1688):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'users', 'page'])
    c_ = angel.get_tags_users(startup_id)
    assert type(c_) == dict
    assert sorted(list(c_.iterkeys())) == expected_keys
    assert type(c_['users']) == list
    assert type(c_['per_page']) == int
    assert type(c_['last_page']) == int
    assert type(c_['total']) == int
    assert type(c_['page']) == int


  def test_reviews(self, user_id=155):
    r_ = angel.get_reviews(user_id)
    expected_keys = sorted(['reviews', 'last_page', 'per_page', 'total', 'page', 'total_positive'])
    assert type(r_) == dict
    reviews_ = r_['reviews']
    assert type(reviews_) == list
    e = sorted(['relationship_to_reviewer', 'rating', 'created_at', 'note', 'reviewer', 'id'])
    assert sorted(list(reviews_[0].iterkeys())) == e


  def test_review_id(self, id_=1098):
    r_id_ = angel.get_review_id(id_)
    expected_keys = sorted(['relationship_to_reviewer', 'rating', 'created_at', 'note', 'reviewer', 'id'])
    assert type(r_id_ ) == dict
    assert sorted(list(r_id_.iterkeys())) == expected_keys
    assert type(r_id_['created_at']) == unicode
    assert type(r_id_['id']) == int
    assert type(r_id_['note']) == unicode
    assert type(r_id_['rating']) == int
    assert type(r_id_['relationship_to_reviewer']) == dict

  def test_feeds(self):
    f_ = angel.get_feeds()
    expected_keys = sorted(['feed', 'per_page', 'last_page', 'total', 'page'])
    self.assertEqual(sorted(list(f_.iterkeys())), expected_keys)
    f_elem = f_['feed'][0]
    e_ = sorted(['description', 'extra', 'timestamp', 'comments', 'actor', 'item', 'likes', 'text', 'promoted_by', 'id', 'target'])
    self.assertEqual(e_, sorted(list(f_elem.iterkeys())))
    self.assertEqual(type(f_elem['description']), unicode)
    self.assertEqual(type(f_elem['timestamp']), unicode)
    self.assertEqual(type(f_elem['id']), unicode)
    self.assertEqual(type(f_elem['comments']), int)
    self.assertEqual(type(f_elem['likes']), int)
    self.assertEqual(type(f_elem['actor']), dict)
    self.assertEqual(type(f_elem['item']), dict)
    f_ = angel.get_feeds(personalized=True)
    expected_keys = sorted(['feed', 'per_page', 'last_page', 'total', 'page'])
    self.assertEqual(sorted(list(f_.iterkeys())), expected_keys)
    f_elem = f_['feed'][0]
    e_ = sorted(['description', 'extra', 'timestamp', 'comments', 'actor', 'item', 'likes', 'text', 'promoted_by', 'id', 'target'])
    self.assertEqual(e_, sorted(list(f_elem.iterkeys())))
    self.assertEqual(type(f_elem['description']), unicode)
    self.assertEqual(type(f_elem['timestamp']), unicode)
    self.assertEqual(type(f_elem['id']), unicode)
    self.assertEqual(type(f_elem['comments']), int)
    self.assertEqual(type(f_elem['likes']), int)
    self.assertEqual(type(f_elem['actor']), dict)
    self.assertEqual(type(f_elem['item']), dict)
    epoch = '1388890909' # May 1 2014
    f_ = angel.get_feeds(since=epoch)
    expected_keys = sorted(['feed', 'cursor',])
    self.assertEqual(sorted(list(f_.iterkeys())), expected_keys)
    f_elem = f_['feed'][0]
    e_ = sorted(['description', 'extra', 'timestamp', 'comments', 'actor', 'item', 'likes', 'text', 'promoted_by', 'id', 'target'])
    self.assertEqual(e_, sorted(list(f_elem.iterkeys())))
    self.assertEqual(type(f_elem['description']), unicode)
    self.assertEqual(type(f_elem['timestamp']), unicode)
    self.assertEqual(type(f_elem['id']), unicode)
    self.assertEqual(type(f_elem['comments']), int)
    self.assertEqual(type(f_elem['likes']), int)
    self.assertEqual(type(f_elem['actor']), dict)
    self.assertEqual(type(f_elem['item']), dict)


if __name__ == '__main__':
  unittest.main()
