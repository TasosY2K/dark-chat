
const fs = require("fs");
const net = require("net");
const moment= require("moment");

const HOST = "127.0.0.1";
const PORT = 6969;

net.createServer(sock => {
    console.log(`CONNECTED: ${sock.remoteAddress} : ${sock.remotePort}`);

    sock.on("data", data => {
        console.log(`DATA ${sock.remoteAddress} : ${data}`);
        fs.appendFileSync(`./DATA/${sock.remoteAddress}.txt`, `${moment().format('YYYY-MM-DD HH:mm:ss')} | ${data}\n`, "utf-8");
        sock.write("OK");
    });

    sock.on("close", data => {
        console.log(`CLOSED: ${sock.remoteAddress} ${sock.remotePort}`);
    });

    sock.on("error", err => {
        console.log(err);
    });
}).listen(PORT, HOST);

console.log('Server listening on ' + HOST +':'+ PORT);