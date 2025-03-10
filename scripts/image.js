const http = require('http');
const fs = require('fs');
const path = require('path');

const hostname = '127.0.0.1';
const port = 3000;

const ImageServer = http.createServer((req, res) => {
    // 图片存储的文件夹路径
    const directoryPath = path.join(__dirname, '../images');
    // 请求的图片文件名
    const filePath = path.join(directoryPath, req.url);
    // 确保文件存在且是文件，不是目录
    fs.access(filePath, fs.constants.F_OK | fs.constants.R_OK, (err) => {
        if (err) {
            res.writeHead(404, 'Not Found');
            res.end('Oops. Image not found!');
        } else {
            // 读取图片文件并发送响应
            fs.readFile(filePath, (err, data) => {
                if (err) {
                    res.writeHead(500, 'Server Error');
                    res.end('Oops. There was a server error!');
                } else {
                    res.writeHead(200, { 'Content-Type': 'image/jpeg' });
                    res.end(data);
                }
            });
        }
    });
});

ImageServer.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
    console.log('Press CTRL+C to stop the server');
});

exports.ImageServer = ImageServer;