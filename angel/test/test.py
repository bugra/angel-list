import os
import sys
import unittest
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import angel
import json
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

VIACOM_ID = '40744'
WHATSAPP_ID = '78902'
UBER_ID = '19163'
AIRBNN_ID = '32677'
KARMA_ID = '29741'
CB_INSIGHTS_ID = '344401'
ANGELLIST_ID = '6702'

angel = angel.AngelList(
                                    config.CLIENT_ID,
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
    self.assertEqual(self_['name'], config.MY_NAME)
    self.assertEqual(self_['twitter_url'], config.TWITTER_URL)
    self.assertEqual(self_['online_bio_url'], config.ONLINE_BIO_URL)
    self.assertEqual(self_['linkedin_url'], config.LINKEDIN_URL)
    self.assertEqual(self_['github_url'], config.GITHUB_URL)
    self.assertEqual(self_['email'], config.EMAIL)
    self.assertEqual(self_['angellist_url'], config.ANGELLIST_URL)
    self.assertEqual(int(self_['id']), config.ID)
     
  def test_search_for_slugs(self):
    slug_ = angel.get_search_for_slugs('karma')
    self.assertEqual(int(slug_['id']), int(KARMA_ID))
    self.assertEqual(slug_['name'], 'Karma')
    self.assertEqual(slug_['type'], 'Startup')
    self.assertEqual(slug_['url'], 'https://angel.co/karma')

  def test_search(self):
    # Get the first item of the list
    # Check if the search of angel list actually works
    search_ = angel.get_search('cb insights')
    s_ = search_[0]
    self.assertEqual(type(search_), list)
    self.assertEqual(type(s_), dict)
    self.assertEqual(int(s_['id']), 344401)
    self.assertEqual(s_['name'], 'CB Insights')
    self.assertEqual(s_['type'], 'Startup')
    self.assertEqual(s_['url'], 'https://angel.co/cb-insights-1')

  def test_users_batch(self):
    n = 30
    ids = list(map(lambda k: str(k), range(n)))
    batch_ = angel.get_users_batch(ids)
    self.assertTrue(len(batch_) <= n)
    keys = [u'dribbble_url', u'image', u'locations', u'id', u'angellist_url',
            u'resume_url', u'what_i_do', u'follower_count', u'bio',
            u'online_bio_url', u'twitter_url', u'facebook_url', u'criteria',
            u'aboutme_url', u'investor', u'name', u'roles', u'skills',
            u'linkedin_url', u'github_url', u'behance_url', u'blog_url',
            u'what_ive_built'
            ]
    if batch_ and len(batch_) > 0:
      self.assertEqual(sorted(list(batch_[0].iterkeys())), sorted(keys))

  def test_user(self):
    id_ = 155
    u_ = angel.get_user(id_)
    expected_keys = sorted(['dribbble_url', 'image', 'locations', 'id',
      'angellist_url', 'what_ive_built', 'what_i_do', 'follower_count', 'bio',
      'online_bio_url', 'twitter_url', 'facebook_url', 'criteria',
      'aboutme_url', 'investor', 'name', 'roles', 'resume_url', 'skills',
      'linkedin_url', 'github_url', 'behance_url', 'blog_url'])
    self.assertEqual(type(u_), dict)
    self.assertEqual(expected_keys, sorted(list(u_.iterkeys())))

  def test_comments(self):
    comments_ = angel.get_comments('Startup', KARMA_ID)
    self.assertEqual(type(comments_), list)
    self.assertEqual(type(comments_[0]), dict)
    self.assertTrue(len(comments_) > 6)


  if False:

          def test_jobs(self):
            # Test two pages
            for pg in [1, 2]:
              jobs_ = angel.get_jobs(page=pg)
              expected_job_keys = sorted(['per_page', 'last_page', 'total', 'jobs', 'page'])
              self.assertEqual(type(jobs_), dict)
              self.assertEqual(expected_job_keys, sorted(list(jobs_.iterkeys())))

          def test_job_by_id(self):
            j_ = angel.get_job_by_id(97)
            self.assertEqual(type(j_), dict)
            self.assertEqual(int(j_['id']), 97)
            self.assertEqual(j_['angellist_url'],
                             u'https://angel.co/angellist/jobs/97-engineer')
            self.assertEqual(j_['created_at'], '2011-12-05T21:05:43Z')
            self.assertEqual(j_['currency_code'], 'USD')
            self.assertEqual(float(j_['equity_cliff']), 1.0)
            self.assertEqual(float(j_['equity_max']), 0.2)
            self.assertEqual(float(j_['equity_min']), 0.2)
            self.assertEqual(float(j_['equity_vest']), 6.0)
            self.assertEqual(int(j_['salary_max']), 150000)
            self.assertEqual(int(j_['salary_min']), 120000)
            # Make sure that the resulting data structure is a data type
            self.assertEqual(type(j_['startup']), dict)

          def test_startup_jobs(self):
            jobs_ = angel.get_startup_jobs(ANGELLIST_ID)
            # Based on the assumption that the job posting will not be removed
            j_ = jobs_[0]
            self.assertEqual(type(j_), dict)
            self.assertEqual(int(j_['id']), 97)
            self.assertEqual(j_['angellist_url'],
                             'https://angel.co/angellist/jobs/97-engineer')
            self.assertEqual(j_['created_at'], '2011-12-05T21:05:43Z')
            self.assertEqual(j_['currency_code'], 'USD')
            self.assertEqual(float(j_['equity_cliff']), 1.0)
            self.assertEqual(float(j_['equity_max']), 0.2)
            self.assertEqual(float(j_['equity_min']), 0.2)
            self.assertEqual(float(j_['equity_vest']), 6.0)
            self.assertEqual(int(j_['salary_max']), 150000)
            self.assertEqual(int(j_['salary_min']), 120000)
            self.assertEqual(type(j_['startup']), dict)

          def test_tag_jobs(self):
            jobs_ = angel.get_tag_jobs(1692)
            self.assertEqual(type(jobs_), dict)
            self.assertEqual(type(jobs_['jobs']), list)
            expected_job_keys = sorted(['per_page', 'last_page', 'total', 'jobs', 'page'])
            self.assertEqual(sorted(expected_job_keys), sorted(list(jobs_.iterkeys())))

          def test_likes(self):
            likes_ = angel.get_likes('Comment', 3804)
            expected_job_keys = sorted(['per_page', 'last_page', 'total', 'likes', 'page'])
            self.assertEqual(sorted(expected_job_keys), sorted(list(likes_.iterkeys())))
            self.assertEqual(type(likes_['likes']), list)

  def test_messages(self):
    m_ = angel.get_messages()
    expected_message_keys = sorted(['per_page', 'last_page', 'total', 'messages', 'page'])
    self.assertEqual(sorted(list(m_.iterkeys())), expected_message_keys)

  def test_press(self):
    for id_ in [ANGELLIST_ID, CB_INSIGHTS_ID]:
      m_ = angel.get_press(id_)
      expected_message_keys = sorted(['per_page', 'last_page', 'total', 'press', 'page'])
      self.assertEqual(sorted(list(m_.iterkeys())), expected_message_keys)

  def test_press_id(self):
    expected_keys = sorted(['flags','image_url','title', 'url', 'created_at', 'updated_at', 'id', 'snippet', 'owner_type', 'posted_at', 'owner_id'])
    p_ = angel.get_press_by_id(990)
    self.assertEqual(sorted(list(p_.iterkeys())), expected_keys)
    self.assertEqual(int(p_['id']), 990)
    self.assertEqual(p_['owner_id'], 89289)
    self.assertEqual(p_['url'], ('http://goaleurope.com/2012/04/11/introducing-'
                                              'ukranian-accelerator-eastlabs-and-its-first-teams/'))
    self.assertEqual(p_['updated_at'], '2012-05-10T17:10:23Z')
    self.assertEqual(p_['created_at'], '2012-05-10T17:10:23Z')
    self.assertEqual(p_['title'], ('Startup news from Ukraine: gift selection'
                                          ' service ActiveGift launches today'))
    self.assertEqual(p_['snippet'], ('Introducing Ukranian accelerator'
                                                ' Eastlabs and its first teams'))
    self.assertEqual(p_['posted_at'], '2012-04-11')
    self.assertEqual(p_['owner_type'], 'Startup')

  def test_startup_roles(self):
    # Companies that Andreesseen Horowitz is tagged in
    # https://angel.co/api/spec/startups#GET_startups_%3Aid_roles
    id_ = 37820
    direction_ = 'outgoing'
    a16z_ = angel.get_startup_roles(id_, direction=direction_)
    keys = sorted(['per_page', 'last_page', 'total', 'startup_roles', 'page'])
    self.assertEqual(sorted(list(a16z_.iterkeys())), keys)
    a_ = a16z_['startup_roles'][0]
    self.assertTrue('startup' in a_)
    c_ = a_['startup']
    self.assertEqual(c_['angellist_url'], 'https://angel.co/andreessen-horowitz')
    self.assertEqual(c_['company_url'], 'http://www.a16z.com/')
    self.assertEqual(c_['high_concept'], ('Helping the greatest tech entrepreneurs'
                                                        ' build the best tech companies'))
    self.assertEqual(c_['name'], 'Andreessen Horowitz')
    self.assertEqual(int(c_['quality']), 10)

  def test_startup_comments(self):
    id_ = ANGELLIST_ID
    c_ = angel.get_startup_comments(id_)
    comment_keys = sorted(['comment', 'created_at', 'id', 'user'])
    self.assertEqual(type(c_), list)
    if c_ and len(c_) > 0:
      f_ = c_[0] # first comment
      self.assertEqual(sorted(list(f_.iterkeys())), comment_keys)
      # Need to change
      # I do not know which order Angellist sends these comments
      # If there does not a particular order exist, or the order does not
      # depend on the comment created time
      # Then the following test may not work and become meaningless
      self.assertEqual(f_['comment'], ("AngelList is badass! Thank you guys, you are "
                                      "changing the way companies get funded and that's awesome!"))
      self.assertEqual(f_['created_at'], '2011-08-05T06:07:50Z')
      self.assertEqual(int(f_['id']), 3800)
      self.assertEqual(f_['user']['angellist_url'], 'https://angel.co/thomask')
      self.assertEqual(f_['user']['bio'],
        ('Founder of @angelpad, Ex-@Google Product Manager, Startup Advisor, '
          'Angel Investor http://angelpad.org/b/scoble-thomas-korte-2012/'))
      # Based on the assumption: followers will only increase
      self.assertTrue(int(f_['user']['follower_count']) >= 11175)
      self.assertEqual(int(f_['user']['id']), 111)
      self.assertEqual(f_['user']['name'], 'Thomas Korte')

  def test_startups_filtered_by(self, filter_='raising'):
    expected_keys = sorted(['last_page', 'per_page', 'startups', 'total', 'page'])
    s_ = angel.get_startups_filtered_by(filter_=filter_)
    self.assertEqual(type(s_), dict)
    self.assertEqual(sorted(list(s_.iterkeys())), expected_keys)
    i_ = s_['startups'][0]
    expected_keys = sorted(['status', 'crunchbase_url', 'fundraising',
      'video_url', 'company_url', 'company_type', 'updated_at', 'quality',
      'id', 'angellist_url', 'screenshots', 'follower_count', 'hidden',
      'launch_date', 'markets', 'community_profile', 'product_desc',
      'twitter_url', 'high_concept', 'facebook_url', 'locations', 'thumb_url',
      'company_size', 'logo_url', 'name', 'created_at', 'linkedin_url',
      'blog_url','abilities'])
    self.assertEqual(sorted(list(i_.iterkeys())), expected_keys)

  def test_startup_roles(self):
    # Only Startup id
    startup_id = ANGELLIST_ID
    s_ = angel.get_startup_roles(startup_id=startup_id)
    expected_keys = sorted(['per_page', 'last_page', 'total', 'startup_roles', 'page'])
    self.assertEqual(type(s_), dict)
    self.assertEqual(sorted(list(s_.iterkeys())), expected_keys)
    self.assertEqual(type(s_['startup_roles']), list)
    t_ = s_['startup_roles'][0]
    e = sorted(['confirmed', 'ended_at', 'title', 'created_at', 'startup', 'tagged', 'role', 'started_at', 'id'])
    self.assertEqual(e, sorted(list(t_.iterkeys())))
    # Direction Test
    direction = 'outgoing'
    s_ = angel.get_startup_roles(startup_id=startup_id, direction=direction)
    self.assertEqual(type(s_), dict)
    self.assertEqual(sorted(list(s_.iterkeys())), expected_keys)
    self.assertEqual(type(s_['startup_roles']), list)
    t_ = s_['startup_roles'][0]
    self.assertEqual(e, sorted(list(t_.iterkeys())))

    # Roles Test
    s_ = angel.get_startup_roles(startup_id=startup_id, role='founder')
    self.assertEqual(type(s_), dict)
    self.assertEqual(sorted(list(s_.iterkeys())), expected_keys)
    self.assertEqual(type(s_['startup_roles']), list)
    t_ = s_['startup_roles'][0]
    self.assertEqual(e, sorted(list(t_.iterkeys())))
    s_ = angel.get_startup_roles(startup_id=startup_id, role='advisor')
    self.assertEqual(type(s_), dict)
    self.assertEqual(sorted(list(s_.iterkeys())), expected_keys)
    self.assertEqual(type(s_['startup_roles']), list)
    t_ = s_['startup_roles'][0]
    self.assertEqual(e, sorted(list(t_.iterkeys())))

    # User id test
    s_ = angel.get_startup_roles(user_id=2)
    self.assertEqual(type(s_), dict)
    self.assertEqual(sorted(list(s_.iterkeys())), expected_keys)
    self.assertEqual(type(s_['startup_roles']), list)
    t_ = s_['startup_roles'][0]
    self.assertEqual(e, sorted(list(t_.iterkeys())))

  def test_status_updates(self, startup_id=ANGELLIST_ID):
    expected_keys = sorted(['total', 'per_page', 'last_page', 'status_updates', 'page'])
    u_ = angel.get_status_updates(startup_id)
    self.assertEqual(type(u_), dict)
    self.assertEqual(sorted(list(u_.iterkeys())), expected_keys)
    up_ = u_['status_updates']
    self.assertEqual(type(up_), list)
    p_ = up_[0]
    self.assertEqual(type(p_), dict)
    e = sorted(['created_at', 'message', 'id'])
    self.assertEqual(sorted(list(p_.iterkeys())), e)

  def test_tags(self, startup_id=1654):
    expected_keys = sorted(['statistics', 'display_name', 'name', 'angellist_url', 'id', 'tag_type'])
    t_ = angel.get_tags(startup_id)
    self.assertEqual(type(t_), dict)
    self.assertEqual(sorted(list(t_.iterkeys())), expected_keys)
    self.assertEqual(type(t_['statistics']), dict)
    self.assertEqual(sorted(list(t_['statistics'].iterkeys())), sorted(['all', 'direct']))

  def test_tags_children(self, startup_id=1654):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'children', 'page'])
    c_ = angel.get_tags_children(startup_id)
    self.assertEqual(type(c_), dict)
    self.assertEqual(sorted(list(c_.iterkeys())), expected_keys)
    self.assertEqual(type(c_['children']), list)
    self.assertEqual(type(c_['per_page']), int)
    self.assertEqual(type(c_['last_page']), int)
    self.assertEqual(type(c_['total']), int)
    self.assertEqual(type(c_['page']), int)

  def test_tags_parents(self, startup_id=1688):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'parents', 'page'])
    c_ = angel.get_tags_parents(startup_id)
    self.assertEqual(type(c_), dict)
    self.assertEqual(sorted(list(c_.iterkeys())), expected_keys)
    self.assertEqual(type(c_['parents']), list)
    self.assertEqual(type(c_['per_page']), int)
    self.assertEqual(type(c_['last_page']), int)
    self.assertEqual(type(c_['total']), int)
    self.assertEqual(type(c_['page']), int)

  def test_tags_startups(self, startup_id=1688):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'startups', 'page'])
    c_ = angel.get_tags_startups(startup_id)
    self.assertEqual(type(c_), dict)
    self.assertEqual(sorted(list(c_.iterkeys())), expected_keys)
    self.assertEqual(type(c_['startups']), list)
    self.assertEqual(type(c_['per_page']), int)
    self.assertEqual(type(c_['last_page']), int)
    self.assertEqual(type(c_['total']), int)
    self.assertEqual(type(c_['page']), int)

  def test_tags_users(self, startup_id=1688):
    expected_keys = sorted(['per_page', 'last_page', 'total', 'users', 'page'])
    c_ = angel.get_tags_users(startup_id)
    self.assertEqual(type(c_), dict)
    self.assertEqual(sorted(list(c_.iterkeys())), expected_keys)
    self.assertEqual(type(c_['users']), list)
    self.assertEqual(type(c_['per_page']), int)
    self.assertEqual(type(c_['last_page']), int)
    self.assertEqual(type(c_['total']), int)
    self.assertEqual(type(c_['page']), int)

  def test_reviews(self, user_id=155):
    r_ = angel.get_reviews(user_id)
    expected_keys = sorted(['reviews', 'last_page', 'per_page', 'total', 'page', 'total_positive'])
    self.assertEqual(type(r_), dict)
    reviews_ = r_['reviews']
    self.assertEqual(type(reviews_), list)
    e = sorted(['relationship_to_reviewer', 'created_at', 'note', 'reviewer', 'id'])
    self.assertEqual(sorted(list(reviews_[0].iterkeys())), e)

  def test_review_id(self, id_=1098):
    r_id_ = angel.get_review_id(id_)
    expected_keys = sorted(['relationship_to_reviewer', 'created_at', 'note', 'reviewer', 'id'])
    self.assertEqual(type(r_id_ ), dict)
    self.assertEqual(sorted(list(r_id_.iterkeys())), expected_keys)
    self.assertEqual(type(r_id_['created_at']), unicode)
    self.assertEqual(type(r_id_['id']) ,int)
    self.assertEqual(type(r_id_['note']), unicode)
    self.assertEqual(type(r_id_['relationship_to_reviewer']), dict)

  def test_comments(self):
    c_ = angel.get_comments('Startup', ANGELLIST_ID)
    self.assertEqual(type(c_), list)
    d_ = c_[0]
    expected_keys = sorted(['comment', 'created_at', 'id', 'user'])
    self.assertEqual(expected_keys, sorted(list(d_.iterkeys())))
    self.assertEqual(type(d_['comment']), unicode)
    self.assertEqual(type(d_['created_at']), unicode)
    self.assertEqual(type(d_['id']), int)
    self.assertEqual(type(d_['user']), dict)

  def test_follows_relationship(self):
    r_ = angel.get_follows_relationship(671, 'User', 2)
    expected_keys = ['source', 'target']
    self.assertEqual(expected_keys, sorted(list(r_.iterkeys())))
    e = ['created_at', 'id']
    self.assertEqual(e, sorted(list(r_['source'].iterkeys())))
    self.assertEqual(type(r_['source']['created_at']), unicode)
    self.assertEqual(type(r_['source']['id']), int)

  def test_follows_batch(self):
    batch_ids = ['86500', '173917']
    b_ = angel.get_follows_batch(batch_ids)
    self.assertEqual(type(b_), list)
    self.assertEqual(type(b_[0]), dict)
    expected_keys = sorted(['created_at', 'followed', 'id', 'follower'])
    self.assertEqual(expected_keys, sorted(list(b_[0].iterkeys())))

  def test_paths(self):
    direction = 'following'
    user_ids = [2, 155]
    p_ = angel.get_paths(user_ids=user_ids, direction=direction)
    expected_keys = sorted([u'2', u'155'])
    self.assertEqual(expected_keys, sorted(list(p_.iterkeys())))
    self.assertEqual(type(p_['2']), list)
    pp_ = p_['2'][0]
    self.assertEqual(type(pp_), list)
    c_ = pp_[0]
    e = sorted([u'connector', u'connection'])
    self.assertEqual(e, sorted(list(c_.iterkeys())))
    ee = sorted(['angellist_url', 'image', 'type', 'id', 'name'])
    self.assertEqual(ee, sorted(list(c_['connector'])))
    eee = sorted(['out', 'via', 'type', 'in'])
    self.assertEqual(eee, sorted(list(c_['connection'])))

if __name__ == '__main__':
  unittest.main()
