import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

# Raises an exception if there is an error downloading the file and will do nothing if succeeded
res.raise_for_status()

play_file = open('Romeo_and_Juliet.txt', 'wb')
for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close() 
