#!/usr/bin/env python
import unittest
from testutils.utils import *

from input.inputloader import InputLoader

class TestReadInput(unittest.TestCase):

    def test_load_yamlfile(self):
        # Given the user has configured a resume file
        yamlfile = 'resources/input.yaml'
        my_loader = InputLoader()

        # When parsing the file
        actual = my_loader.load_yaml(get_test_resources_path(yamlfile))

        # Then the contents are read successfully
        expected = {'interests': [{'name': 'Excercise', 'keywords': ['Interest 1', 'Interest 2']}, {'name': 'Sports', 'keywords': ['Sports 1', 'Sports 2']}], 'publications': [], 'basics': {'website': 'http://www.mypage.se', 'profiles': [{'url': 'https://www.linkedin.com/in/kaalle-b1234567/', 'username': 'kaalle-b1234567', 'network': 'LinkedIn'}], 'location': {'address': 'Adagatan 1', 'postalCode': '414 63', 'city': 'Göteborg', 'region': 'Västra Götaland', 'countryCode': 'SE'}, 'name': 'Kålle (1976-01-29)', 'picture': 'http://mypage.se/img/kalle.jpg', 'email': 'kalle@gmail.com', 'summary': 'Kålle is a developer...', 'phone': '076-1 23 45 67', 'label': 'Developer'}, 'skills': [{'name': 'Programming', 'level': 'Master', 'keywords': ['Python', 'Perl', 'Javascript', 'CSS', 'HTML', 'PHP']}, {'name': 'Programming', 'level': 'Basic', 'keywords': ['Java', 'C', 'C++']}, {'name': 'Database', 'level': 'Master', 'keywords': ['SQL', 'NoSQL']}, {'name': 'Version Control', 'level': 'Master', 'keywords': ['Git', 'Subversion', 'ClearCase']}], 'languages': [{'language': 'Swedish', 'fluency': 'Native speaker'}, {'language': 'English', 'fluency': 'Fluent'}], 'references': [{'name': 'Company #1', 'reference': 'Will be provided upon request'}], 'work': [{'website': 'http://www.companyone.com', 'highlights': ['Stuff 1', 'Other stuff', 'more cool stuff...'], 'summary': 'Development team member, Awesome Feature.', 'position': 'Developer', 'company': 'Company #1', 'endDate': 'Present', 'startDate': '2017-01-01'}, {'website': 'http://www.companytwo.com', 'highlights': ['Stuff 1', 'Other stuff', 'more cool stuff...'], 'summary': 'Development team member, Awesome Feature.', 'position': 'Developer', 'company': 'Company #2', 'endDate': '2016-12-31', 'startDate': '2014-01-01'}], 'awards': [{'summary': 'Awesome award for being awesome', 'date': '2017-11-01', 'awarder': 'Company #1 Awards', 'title': 'Awards #1'}, {'summary': 'Awesome award for being awesome', 'date': '2012-10-01', 'awarder': 'Company #2', 'title': 'Award #2'}]}
        self.assertIsInstance(actual, dict, actual)
