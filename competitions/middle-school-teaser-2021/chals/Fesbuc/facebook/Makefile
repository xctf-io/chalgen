build:
	@docker build  --platform linux/amd64 . -t facebook-django-8737151487862

run: build
	@docker run -p 8081:8000 facebook-django-8737151487862

clean:
	@docker rm -f -v facebook-django-8737151487862

generate-img:
	@docker run -d --name facebook-django-8737151487862 facebook-django-8737151487862:latest
	@docker export facebook-django-8737151487862 -o vm.tar.gz
	@docker rm facebook-django-8737151487862
	@docker rmi facebook-django-8737151487862