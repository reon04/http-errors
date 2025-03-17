FROM nginx:1.27.4-alpine
COPY ./conf/nginx.conf /etc/nginx/
COPY ./html/ /usr/share/nginx/html
COPY * ./