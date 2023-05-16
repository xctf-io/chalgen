build:
	@docker build . -t facebook-django-8781660438841 -q

run: build
	@docker run -p 8081:8000 facebook-django-8781660438841

clean:
	@docker rm -f -v facebook-django-8781660438841

generate-img:
	@docker run -d --name facebook-django-8781660438841 facebook-django-8781660438841:latest
	@docker export facebook-django-8781660438841 -o vm.tar.gz
	@docker rm facebook-django-8781660438841
	@docker rmi facebook-django-8781660438841