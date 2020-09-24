FROM node:alpine
RUN apk update && apk add --no-cache make git

WORKDIR /frontend

RUN npm i npm@latest -g && \
    npm install -g @angular/cli@8.3.19

## (Optional) To copy everything from frontend to server. Since we are using volume mount (to support live reload) its not needed
#COPY . /frontend
#RUN npm install

RUN chown -R node /frontend

USER node


