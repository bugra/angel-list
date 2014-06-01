import unittest

import angel
import config

MY_ID = '518840'
VIACOM_ID = '40744'
WHATSAPP_ID = '78902'
UBER_ID = '19163'
AIRBNN_ID = '32677'
KARMA_ID = '29741'
CB_INSIGHTS_ID = '344401'

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


if __name__ == '__main__':
  unittest.main()
