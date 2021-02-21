# secure-meeting-vault

## Inspiration
We wanted to create create a program that could help those who have trouble with technology, and help improve the current quality of education. We also focused on tackling Zoom Bombers and unwanted participants because it also holds value after the pandemic is over.
## What it does
Vault uses facial recognition software through a neural network to only provide the link to the meeting to those who had the meeting link (provided by the website), and takes a picture of the participant to verify. If all goes well, they are given a button that will launch the meeting, if not they are prompted to try again.
## How we built it
We used HTML, Bootstrap, CSS, and JS for the front end, and Python/Django for the backend.
## Challenges we ran into
It took a long time to set up the backend, and various challenges with creating form logic, and how to convert images.
## Accomplishments that we're proud of
We are proud being able to actually create a functional website, where we can securely allow people into the meeting, and create a better learning environment.
## What we learned
We learned how to use neural networks to access facial recognition, employ a Python backend framework, how to use HTML with Bootstrap, CSS and JS.
## What's next for Vault
We want to attach the website to an actual domain. The domain we are planning to attach it to is called vaultsecuremeeting.herokuapp.com. We also plan to improve the webpages and make clean up our code.

The way to run this is to download the repository and run this command in the correct directory:

     python manage.py runserver
     
## Security
The Django framework provides the following security features. More information can be found on Django's official [Security Overview](https://docs.djangoproject.com/en/3.1/topics/security/).

- XSS protection (by implementing proper character escaping)
- CSRF protection using secret tokens
- SQL Injection Protection
- Clickjacking Protection

## Built With
- [Django](https://www.djangoproject.com/)

