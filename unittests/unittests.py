import unittest
from aws_helpers import spark_write_to_rds, spark_read_from_rds
from spark_helpers import get_spark_session_and_context
# import selenium  # consider for testing
# python -m unittest unittests/unittests.py    # (second is name of the module)


# TODO: build a webapp for displaying the dashboard?

spark, sc = get_spark_session_and_context()

class PreprocessingTests(unittest.TestCase):
    def test_lowercase_table_names(self):
        for table_name in ['sp_five_hundred', 'nasdaq']:
            df = spark_read_from_rds(spark, table_name)
            for col in df.columns:
                self.assertTrue(col == col.lower())


# Can be more fine grained
# python -m unittest test_module1 test_module2
# python -m unittest test_module.TestClass
# python -m unittest test_module.TestClass.test_method

# # https://medium.com/@samzamany/unit-testing-in-data-engineering-a-practical-guide-91196afdf32a
#         self.assertEqual('foo'.upper(), 'FOO')
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

if __name__ == '__main__':
    unittest.main()