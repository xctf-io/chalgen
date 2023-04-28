build:
	@docker build . -t jekyll-blog-304545197 -q

run: build
	@docker run -p 8081:80 jekyll-blog-304545197

clean:
	@docker rm -f -v jekyll-blog-304545197

generate-img:
	@docker run -d --name jekyll-blog-304545197 jekyll-blog-304545197:latest
	@docker export jekyll-blog-304545197 -o vm.tar.gz
	@docker rm jekyll-blog-304545197
	@docker rmi jekyll-blog-304545197