import requests

with open('id.txt') as f:
    id = f.read()

with open('token.txt') as f:
    my_token = f.read()

result = requests.get('https://api.vk.com/method/friends.get?user_ids=' +
                        id + '&fields=name&access_token=' + my_token + '&v=5.131').json()
i = 0
for i in range(len(result['response']['items'])):
    first_name = result['response']['items'][i]['first_name']
    last_name = result['response']['items'][i]['last_name']
    print(first_name + " " + last_name)
    i += i
