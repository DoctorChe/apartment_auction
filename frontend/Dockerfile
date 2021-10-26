# base image
FROM node:14-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
#ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY ./app/package.json ./package.json
RUN npm install
RUN npm install @vue/cli@4.5.14 -g

COPY ./app/ .

# start app
CMD ["npm", "run", "serve"]
