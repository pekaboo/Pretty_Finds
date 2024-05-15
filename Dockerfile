# 基于 Node 的一个官方镜像，版本 14
FROM node:14 

# 设置工作目录
WORKDIR /app 

# 拷贝 package.json 和 package-lock.json 到 /app
COPY package*.json ./ 

# 在项目根目录下安装项目依赖
RUN npm install 

# 把其他源文件拷贝到工作目录
COPY . . 

# 让你的应用绑定到这个端口
EXPOSE 3000 

# CMD 命令在容器启动后执行
CMD [ "node", "server.js" ] 