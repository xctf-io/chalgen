build:
	@docker build . -t facebook-django-8750599669273 -q

run: build
	@docker run -p 8081:8000 facebook-django-8750599669273

clean:
	@docker rm -f -v facebook-django-8750599669273

generate-img:
	docker run -d --name facebook-django-8750599669273 facebook-django-8750599669273:latest
	docker export facebook-django-8750599669273 -o vm.tar.gz
	docker stop facebook-django-8750599669273