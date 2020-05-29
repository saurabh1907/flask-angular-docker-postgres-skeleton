FROM node:alpine
RUN apk update && apk add --no-cache make git

WORKDIR /frontend

COPY package.json package-lock.json /frontend/

RUN npm i npm@latest -g && \
    npm install -g @angular/cli@7.3.9

RUN chown -R node /frontend

WORKDIR /frontend

USER node

RUN npm install