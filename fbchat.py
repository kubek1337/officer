from fbchat import Client
from fbchat.models import Message

username = ""
password = ""

client = Client(username, password)

users = client.fetchThreadList()
print(users)
detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users ]
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)
best_friend = sorted_detailed_users[0]
print("Best friend:", best_friend.name, "with a message count of", best_friend.message_count)