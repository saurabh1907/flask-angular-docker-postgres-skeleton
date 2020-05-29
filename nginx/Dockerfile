FROM nginx:alpine

# Copy custom nginx config
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]