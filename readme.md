# Description

Tests are developed for REST API of CRUD service for bears in alaska: https://hub.docker.com/r/azshoo/alaska with 1.0 tag.

Manual test check list available by the [link](https://docs.google.com/spreadsheets/d/1EIMX3Ypry0igtNWVbKtv6mQeB96l7UX8U041T8biUJ4/edit?usp=sharing).
# Run Docker image

```bash
docker run -p 8091:8091 azshoo/alaska:1.0
```


# Run tests

```bash
pip install -r requirements.txt
pytest ./tests
```