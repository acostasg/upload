import unittest

import injectionContainer
import mock
import logging as log
from upload.strategy.dummys.injectedContainerDummy import ContainerMock


class TestCronUpload(unittest.TestCase):
    """
    Class Test cron upload
    """

    def test_cron_upload(self):
        """
        Test case upload file
        :return:
        """

        injectionContainer.Container.update(
            ContainerMock().container()
        )

        logging = log
        logging.basicConfig = mock.Mock(return_value=0)

        import cronUpload

        self.assertTrue(cronUpload.execute_cron(
            'test_host',
            'test_username',
            'test_secret',
            8080,
            'test_local',
            'test_remote',
            'test_prefix',
            'test_pattern',
            1
        ))