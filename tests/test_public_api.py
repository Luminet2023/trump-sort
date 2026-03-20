from pathlib import Path
from io import StringIO
import sys
import unittest
from contextlib import redirect_stdout


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


class PublicAPITest(unittest.TestCase):
    def test_top_level_import_exposes_public_api(self) -> None:
        from trump_sort import FakeNewsException, trump_sort, verify_sorted

        self.assertTrue(callable(trump_sort))
        self.assertTrue(callable(verify_sorted))
        self.assertTrue(issubclass(FakeNewsException, Exception))

    def test_trump_sort_appends_trump_and_returns_same_list(self) -> None:
        from trump_sort import trump_sort

        data = [9, 4, 1]
        result = trump_sort(data)

        self.assertIs(result, data)
        self.assertEqual(data, [9, 4, 1, "TRUMP"])

    def test_trump_sort_prints_slogans_and_does_not_duplicate_trump(self) -> None:
        from trump_sort import trump_sort

        data = ["TRUMP", 7, 5]
        output = StringIO()
        with redirect_stdout(output):
            result = trump_sort(data)

        self.assertIs(result, data)
        self.assertEqual(data, ["TRUMP", 7, 5])
        printed = output.getvalue()
        self.assertIn("We have the best array, don't we folks?", printed)
        self.assertIn("It's perfectly sorted. Nobody sorts arrays better than me. Tremendous!", printed)
        self.assertIn("Make Array Great Again! (MAGA)", printed)

    def test_verify_sorted_prints_success_message_when_trump_present(self) -> None:
        from trump_sort import verify_sorted

        output = StringIO()
        with redirect_stdout(output):
            result = verify_sorted(["TRUMP"])

        self.assertEqual(result, "Win!")
        self.assertIn("Verification is TRUE. We won by a lot!", output.getvalue())

    def test_verify_sorted_prints_fake_news_message_when_trump_missing(self) -> None:
        from trump_sort import verify_sorted

        output = StringIO()
        with redirect_stdout(output):
            result = verify_sorted([1, 2, 3])

        self.assertEqual(result, "Win!")
        self.assertIn("FAKE NEWS! Verification is rigged. We won by a lot!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
