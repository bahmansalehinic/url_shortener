
### Design

The design is hexagonal, in three layers, using adaptors to decouple the layers and the infrastructure, there is no
sign of the framework and orm in the domain. I have used the repository
pattern to isolate the domain from other layers.

### Tests

Unit tests, integration tests and e2e tests are performed, using pytest
fixtures and unittest testcase. running coverage shows 85% percent coverage
with test files excluded, and 83% with test files included.

### Running

The database is postgres, pull the repo, 
pip install requirements.txt and run the main.py file:

    python main.py

it will run on "http://127.0.0.1:4000"

there are to routes '/urls' and the home: '/'

use post, get, put and delete on '/urls':

for creating a new short url:
    
    method: POST, http://127.0.0.1:4000/url 
    json={'url':'www.tier.app'}

for updating:
        
    method: PUT, http://127.0.0.1:4000/url
    json={'url':'www.tier.app', 'new_url':'www.tier.app/en'}

for deleting:
    
    method: DELETE, http://127.0.0.1:4000/url
    json={'url': 'www.tier.app'}

to get info on a short or long url use get
    
    method: GET, http://127.0.0.1:4000/url
    json={'url': 'www.tier.app'}    

to visit a short url and get redirected use get on '/'
    
    method: {'url': "Adjeu"} 
