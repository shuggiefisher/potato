To recreate an replicatable environment for Salt-n-Sauce :

1. Download and install Google App Engine Python SDK

2. Make sure the google app engine SDK is on your PATH

3. Setup the python environment

mkdir gae-env
cd gae-env
virtualenv --no-site-packages --distribute .

# clone the repository
git clone https://github.com/shuggiefisher/potato.git

# activate the environment to ensure you use the environment's python binaries, and the system python binaries
source bin/activate

# install the django requirements into the environment
pip install -r potato/requirements.txt

# if all goes well the symbolic links in the gae-django-instatrade directory should point to the libraries just installed by pip

# fix the site specific settings
cd potato
nano -w sitespecific_settings.py

# remove "'java', '-jar', " from mediagenerator/filters/yuicompressor.py and closure.py

# patch static/js/bootstrap-twipsy.js to set z-index to 12000

# Setup the initial database for local testing
./manage.py syncdb

# Start a local webserver for testing purposes
./manage runserver 8080

# View the website in your browser at http://localhost:8080


# If you wish to deploy the website to app engine you will have to register for your own appengine account
# Setup an app engine application, and change the entry in app.yaml from 'salt-n-sauce' to the name of your application

# Deploy the code to google app engine
./manage deploy

# Initialise the remote database
./manage remote syncdb

# You app engine app should now be working

