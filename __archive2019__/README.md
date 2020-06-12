# ref
selenium best w/ docker https://github.com/namgivu/web-automation-testing/tree/selenium-w-docker
                        https://github.com/namgivu/selenium-docker-start
                        
selenium basic          https://github.com/namgivu/selenium-start
selenium intermediate   https://github.com/namgivu/selenium-start2nd-w-proboscis

# installation
```bash
./docker/up.sh
```

# run test
```bash
: install python 3.6 and pipenv ref. bit.ly/nnpipenv
pipenv sync
PYTHONPATH=`pwd` pipenv run pytest
```
