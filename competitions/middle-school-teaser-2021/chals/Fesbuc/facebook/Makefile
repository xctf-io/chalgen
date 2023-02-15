build:
	@docker build . -t facebook-django-8756733945413 -q

run: build
	@docker run -p 8081:8000 facebook-django-8756733945413

clean:
	@docker rm -f -v facebook-django-8756733945413

generate-img:
	docker run -d --name facebook-django-8756733945413 facebook-django-8756733945413:latest
	docker export facebook-django-8756733945413 -o vm.tar.gz
	docker stop facebook-django-8756733945413