build:
	docker build . -t jekyll-blog-119150930472

run: build
	docker run -p 8081:80 jekyll-blog-119150930472

clean:
	docker rm -f -v jekyll-blog-119150930472

generate-img:
	docker run -d --name jekyll-blog-119150930472 jekyll-blog-119150930472:latest
	docker export jekyll-blog-119150930472 -o vm.tar.gz
	docker stop jekyll-blog-119150930472