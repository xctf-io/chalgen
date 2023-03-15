build:
	@docker build . -t jekyll-blog-8791529038333 -q

run: build
	@docker run -p 8081:80 jekyll-blog-8791529038333

clean:
	@docker rm -f -v jekyll-blog-8791529038333

generate-img:
	@docker run -d --name jekyll-blog-8791529038333 jekyll-blog-8791529038333:latest
	@docker export jekyll-blog-8791529038333 -o vm.tar.gz
	@docker rm jekyll-blog-8791529038333
	@docker rmi jekyll-blog-8791529038333