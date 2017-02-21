import re
from .base import FunctionalTest

SUBJECT = 'Your login link for Superlists'


class LoginTest(FunctionalTest):

    def test_can_get_email_link_to_log_in(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter email address, so she does
        if self.against_staging:
            test_email = 'hugosalas08@gmail.com'
        else:
            test_email = 'edith@example.com'
        
        self.browser.get(self.server_url)
        self.browser.find_element_by_name('email').send_keys(
            test_email + '\n'
        )
        
        # A message appears telling her an email has been sent
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Check your email', body.text)
        
        # She checks her email and finds a message
        body = self.wait_for_email(test_email, SUBJECT)
        
        # It has a url link in it
        self.assertIn('Use this link to log in', body)
        url_search = re.search(r'http://.+/.+$', body)
        if not url_search:
            self.fail(
                'Could not find url in email body:\n{}'.format(body)
            )
        url = url_search.group(0)
        self.assertIn(self.server_url, url)
        
        # she clicks it
        self.browser.get(url)
        
        # she is logged in!
        self.assert_logged_in(email=test_email)
        
        # Now she logs out
        self.browser.find_element_by_link_text('Log out').click()
        
        # She is logged out
        self.assert_logged_out(email=test_email)
        