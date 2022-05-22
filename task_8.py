import vk_api

with open('token.txt') as f:
    my_token = f.readline()

session = vk_api.VkApi(token=my_token)
vk = session.get_api()

with open('id.txt') as f:
    user_id = f.read()

for id in vk.friends.get(user_id=user_id)['items']:
    user = vk.users.get(user_ids=id)[0]
    print(user['first_name'], user['last_name'])
