# spriteCloudTA
CI/CD API/UI automated tests

## API tests

### Motivation

I chose to implement 2 test scenarios which I felt were the most important

1) A user logging in and purchasing a pet

This is the most important one since without it, there is no product!
Before anything is rolled out, we must make sure that a user can at least browse through the pets, login, purchase one and logout again.

This test will ideally run every time a change is made to the backend.

2) An attacker trying to get your user's data

This one is important from a legal/compliance perspective.
Additionally, the client's reputation is at stake should there be any weaknesses in the API/dB's security.

No user should ever get access to another user's data.
This also applies to another user's orders (not implemented).

This test must run periodically but should also be triggered by any changes to the code handling users and security.

### how to run

The tests created in Python, using the UnitTest and 'requests' libraries.
They can run on any system with the required libraries and and internet connection (to reach https://petstore.swagger.io).

## WEB tests

## repository files
- test_scenarios.txt: a description of test scenarios, along with an indication on their status
- test_api.py: UnitTest tests covering 2 API scenarios
- test_utils.py: contains data-arrays and helper functions for the API test procedures
