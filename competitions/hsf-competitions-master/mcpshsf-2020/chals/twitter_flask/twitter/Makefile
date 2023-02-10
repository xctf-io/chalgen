build:
	docker build . -t twitter-8781576395332

run: build
	docker run -p 8081:5000 twitter-8781576395332

clean:
	docker rm -f -v twitter-8781576395332

generate-img:
	docker run -d --name twitter-8781576395332 twitter-8781576395332:latest
	docker export twitter-8781576395332 -o vm.tar.gz
	docker stop twitter-8781576395332