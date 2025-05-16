const http = require('http');
const fs = require('fs');
const path = require('path');

const serveur = http.createServer((req, res) => {
    console.log(`Requête reçue : ${req.method} ${req.url}`);

    let filePath = '';
    let contentType = 'text/html';

    if (req.method === 'GET') {
        if (req.url === '/' || req.url === '/index.html') {
            filePath = path.join(__dirname, 'public', 'index.html');
        } else if (req.url === '/mesure') {
            filePath = path.join(__dirname, 'public', 'page1.html');
        } else if (req.url === '/led-cmd') {
            filePath = path.join(__dirname, 'public', 'page2.html');
        } else if (req.url === '/led-state') {
            filePath = path.join(__dirname, 'public', 'page3.html');
        } else {
            // URL inconnue
            res.writeHead(404);
            res.end('Page non trouvée');
            return;
        }

        // Lecture et envoi du fichier
        fs.readFile(filePath, (err, data) => {
            if (err) {
                res.writeHead(500);
                res.end('Erreur serveur');
                return;
            }
            res.writeHead(200, { 'Content-Type': contentType });
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
