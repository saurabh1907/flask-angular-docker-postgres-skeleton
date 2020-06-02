FROM nginx:1.13.7

# Copy custom nginx config
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
