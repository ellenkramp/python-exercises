ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print ramit['email']

print ramit['interests'][0]

friend_list = ramit['friends']

for i in range(len(friend_list)):
  if friend_list[i]['name'] == 'Jasmine':
    print friend_list[i]['email']

for i in range(len(friend_list)):
  if friend_list[i]['name'] == 'Jan':
    print friend_list[i]['interests'][1]

