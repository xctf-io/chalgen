build:
	@docker build . -t facebook-django-8769903087453 -q

run: build
	@docker run -p 8081:8000 facebook-django-8769903087453

clean:
	@docker rm -f -v facebook-django-8769903087453

generate-img:
	docker run -d --name facebook-django-8769903087453 facebook-django-8769903087453:latest
	docker export facebook-django-8769903087453 -o vm.tar.gz
	docker stop facebook-django-8769903087453