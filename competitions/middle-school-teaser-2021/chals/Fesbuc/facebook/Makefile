build:
	@docker build . -t facebook-django-8769283817077 -q

run: build
	@docker run -p 8081:8000 facebook-django-8769283817077

clean:
	@docker rm -f -v facebook-django-8769283817077

generate-img:
	docker run -d --name facebook-django-8769283817077 facebook-django-8769283817077:latest
	docker export facebook-django-8769283817077 -o vm.tar.gz
	docker stop facebook-django-8769283817077