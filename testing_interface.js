const http = require('http');
const fs = require('fs');
const path = require('path');

const serveur = http.createServer((req, res) => {
    console.log(`Requête reçue : ${req.method} ${req.url}`);
      let filePath = './' + (req.url === '/' ? 'public/index.html' : req.url);

    if (req.method === 'GET' && (req.url === '/' || req.url === '/index.html')) {
        //const filePath = path.join(__dirname, 'public', 'index.html');
        fs.readFile(filePath, (err, data) => {
            if (err) {
                res.writeHead(500);
                res.end('Erreur serveur');
                return;
            }
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(data);
        });
    }

    else if (req.method === 'POST' && req.url === '/led') {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', () => {
            console.log('Données POST:', body);
            res.writeHead(200);
            res.end(`Données reçues : ${body}`);
        });
    }

    else {
        res.writeHead(404);
        res.end('Page non trouvée');
    }
});

serveur.listen(3000, () => {
    console.log('Serveur HTTP en écoute sur http://localhost:3000');
});
