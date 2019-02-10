Install local python environment

```
mkvirtualenv site-downloader -p python3.7
```

Install all development requirements (not needed when running in AWS)

From site-downloader directory.

```
pip install -r local/requirements.txt
```

Invoke lambda function locally

```
sls invoke local -f site-downloader --path local/event.json
```