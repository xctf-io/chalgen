# Challenge Types

## A note on Docker challenges

Example challenge for this can be found in web.py `RobotsTxtChallenge`

Install docker: https://docs.docker.com/v17.12/install/

```
python chalgen.py gen --chal-config tests/test_ctf/robots_txt/chal.yaml
python chalgen.py run --chal-config tests/test_ctf/robots_txt/chal.yaml
# visit: http://localhost:8080
```

Challenges that require dockerfiles are currently setup to use templates and string concatenation to add the nessesary files to the template the challenge is based on. In this case, the challenge is based on a simple static site. The `robots.txt` file, and optionally an `index.html` file, is added to the docker container by copying the template and adding `ADD robots.txt $webroot/robots.txt`.

The `run` command runs `make run` within the challenge directory (in this case it is `tests/test_ctf/robots_txt`).