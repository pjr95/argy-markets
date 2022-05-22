import finnhub

with open('../keypar') as keys:
    lines = keys.readlines()
    user = lines[0].replace('\n', '')
    password = lines[2].replace('\n', '')


finnhub_client = finnhub.Client(api_key = password)

print(finnhub_client.quote('AAPL'))