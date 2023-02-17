build:
	@docker build . -t facebook-django-8732723780429 -q

run: build
	@docker run -p 8081:8000 facebook-django-8732723780429

clean:
	@docker rm -f -v facebook-django-8732723780429

generate-img:
	docker run -d --name facebook-django-8732723780429 facebook-django-8732723780429:latest
	docker export facebook-django-8732723780429 -o vm.tar.gz
	docker stop facebook-django-8732723780429