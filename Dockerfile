FROM httpd:2.4
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*
COPY ./conf/httpd.conf /usr/local/apache2/conf/
COPY ./conf/nginx.conf /etc/nginx/
COPY ./htdocs/ /usr/local/apache2/htdocs/
COPY . ./
RUN chmod +x startup.sh
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 8080
CMD ["./startup.sh"]