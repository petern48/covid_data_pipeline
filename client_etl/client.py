import sys
import requests

host = "localhost"
port = 8080

def client_request(file_name, date):
    """Select which file to get data from and the date to simulate."""
    params = {
        'file': file_name,
        'date': date
    }
    response = requests.get(f"http://{host}:{port}/server", params=params)  # , ?file={file_name}&date={date}"

    if response.status_code == 200:

        # if content type is csv
        return response.text

    else:
        print(f"Status Code: {response.status_code}")
        print(F"Response: {response.text}")
        return ""



# For testing
if __name__ == "__main__":
    file_name =  sys.argv[1]  # "example.csv"
    date = sys.argv[2]  # "2024-07-01"

    chars_to_show = 100

    text = client_request(file_name, date)

    if len(text) > chars_to_show:
        print("only printing part of the content")
        print(text[:chars_to_show])
    else:
        print(text)

# from http.client import HTTPSConnection