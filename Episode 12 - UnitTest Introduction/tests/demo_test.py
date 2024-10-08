import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

import pandas as pd
from demo1 import do_job

tests_path = Path(__file__).parent
left_path = tests_path / "dataframe_right.json"
right_path = tests_path / "dataframe_left.json"
save_path = tests_path / "dataframe_merged.json"


class DoJobShould(unittest.TestCase):
    #@patch("random.randint", return_value=6)
    def test_return_dataframe_right_when_random_superior_to_5(self, randint_mock: MagicMock):

        do_job(left_path, right_path, save_path)

        randint_mock.assert_called_once()

        output_dataframe = pd.read_json(save_path)
        expected_dataframe = pd.DataFrame({"animal": ["chien", "chat", "poisson"],
                                           "prix_espagne": [880, 600, 10]})

        self.assertEqual(expected_dataframe.to_json(), output_dataframe.to_json())


if __name__ == '__main__':
    unittest.main()
