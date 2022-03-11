def my_hello():
    print('hello\n')
    
my_hello()

def my_hello_user(user):
    print('Hello! %s. \nYou are %d years old, right?'%(user['name'],user['age']))
    

user = {
     'id': 0,
     'name': '성우',
     'age': 27
}

my_hello_user(user)