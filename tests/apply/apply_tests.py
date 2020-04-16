from pages.apply.apply_page import ApplyPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ApplyTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ap = ApplyPage (self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_t1jobsearch(self):
        self.log.info("*#" * 25)
        self.log.info("test_t1jobsearch started")
        self.log.info("*#" * 25)
        self.ap.searchJob("Ingénieur en Assurance Qualité - NeoXam")
        result = self.ap.verifyJobSearchSuccessful("Ingénieur en Assurance Qualité - NeoXam")
        assert result == True


    @pytest.mark.run(order=2)
    def test_t2appSubmitted(self):
        self.log.info("*#" * 25)
        self.log.info("test_t2appSubmitted started")
        self.log.info("*#" * 25)
        result = self.ap.verifyAppSubmitted("Ingénieur en Assurance Qualité - NeoXam")
        assert result == True