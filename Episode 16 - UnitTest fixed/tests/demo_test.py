import unittest
from pathlib import Path
from unittest.mock import MagicMock

import pandas as pd
from parameterized import parameterized

from demo import Job, IRandom, IPandas

tests_path = Path(__file__).parent
left_path = tests_path / "dataframe_right.json"
right_path = tests_path / "dataframe_left.json"
save_path = tests_path / "dataframe_merged.json"

dataframe_left = pd.DataFrame({"animal": ["chien", "chat", "poisson"],
              "prix_france": [900, 550, 5]})

dataframe_right = pd.DataFrame({"animal": ["chien", "chat", "poisson"],
              "prix_espagne": [880, 600, 10]})


class DoJobShould(unittest.TestCase):
    @parameterized.expand([(6, pd.DataFrame({"animal": ["chien", "chat", "poisson"],
                                           "prix_espagne": [880, 600, 10]})),
                               (4, pd.DataFrame({"animal": ["chien", "chat", "poisson"],
                                                 "prix_france": [900, 550, 5],
                                                 "prix_espagne": [880, 600, 10]}))
                           ])
    def test_return_expected_dataframe(self, random_number, expected_dataframe):

        random_mock = MagicMock(IRandom)
        random_mock.randint = MagicMock(return_value=random_number)

        pandas_mock = MagicMock(IPandas)
        pandas_mock.read_json = MagicMock(side_effect=[dataframe_left, dataframe_right])
        pandas_mock.to_json = MagicMock()

        job = Job(random_mock, pandas_mock)
        job.do_job(left_path, right_path, save_path)

        random_mock.randint.assert_called_once_with(0, 9)

        pandas_mock.to_json.assert_called_once()
        pd.testing.assert_frame_equal(expected_dataframe, pandas_mock.to_json.call_args_list[0].args[1])








if __name__ == '__main__':
    unittest.main()
