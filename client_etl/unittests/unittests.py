import unittest
import socket
import select
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

# class ClientTests(unittest.TestCase):
#     def test_client(sefl):
#         # Get socket file descriptor as a TCP socket using the IPv4 address family
#         listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # Set some modes on the socket, not required but it's nice for our uses
#         listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         address_port = ("127.0.0.1", 8080)
#         # leserve address and port
#         listener_socket.bind(address_port)
#         # listen for connections, a maximum of 1
#         listener_socket.listen(1)
        # print("Server listening @ 127.0.0.1:8080")
        # # loop indefinitely to continuously check for new connections
        # while True:
        #     # Poll the socket to see if there are any newly written data, note excess data dumped to "_" variables
        #     read_ready_sockets, _, _ = select.select(
        #         [listener_socket],  # list of items we want to check for read-readiness (just our socket)
        #         [],  # list of items we want to check for write-readiness (not interested)
        #         [],  # list of items we want to check for "exceptional" conditions (also not interested)
        #         0  # timeout of 0 seconds, makes the method call non-blocking
        #     )
        #     # if a value was returned here then we have a connection to read from
        #     if read_ready_sockets:
        #         # select.select() returns a list of readable objects, so we'll iterate, but we only expect a single item
        #         for ready_socket in read_ready_sockets:
        #             # accept the connection from the client and get its socket object and address
        #             client_socket, client_address = ready_socket.accept()

        #             # read up to 4096 bytes of data from the client socket
        #             client_msg = client_socket.recv(4096)
        #             print(f"Client said: {client_msg.decode('utf-8')}")

        #             # Send a response to the client, notice it is a byte string
        #             client_socket.sendall(b"Welcome to the server!\n")
        #             try:
        #                 # close the connection
        #                 client_socket.close()
        #             except OSError:
        #                 # client disconnected first, nothing to do
        #                 pass

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