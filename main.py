from scrape import send_request

input_text = input("Enter the text to be detected: ")

# Send the request and get the response
response = send_request(input_text)

detected_percentage = response['data']['fakePercentage']

print(detected_percentage)