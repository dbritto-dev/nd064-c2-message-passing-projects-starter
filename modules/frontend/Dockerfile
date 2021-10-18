FROM node:14-alpine as builder
ARG REACT_APP_PERSON_API_URL
ARG REACT_APP_CONNECTION_API_URL
ENV REACT_APP_PERSON_API_URL=$REACT_APP_PERSON_API_URL
ENV REACT_APP_CONNECTION_API_URL=$REACT_APP_CONNECTION_API_URL
WORKDIR /app
COPY package*.json .
RUN npm ci --production
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
