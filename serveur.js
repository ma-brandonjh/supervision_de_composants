const http = require('http');
const fs = require('fs');
const url = require('url');

function errorMessage(){

}

function readJsonFile(file){
    const data = fs.readFileSync(file, 'utf-8')
    return JSON.parse(data)
}

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const direction = parsedUrl.pathname
    const method = req.method;
    let body = '';

    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');


    if (method === "POST"){
        switch (direction){
            case '/led':
                // req.on('data', chunk => body += chunk);
                // req.on('end', () => {
                // try {
                //     const data = JSON.parse(body);
                //     const livres = lireLivres();
                //     const nouveauLivre = {
                //     id: livres.length ? livres[livres.length - 1].id + 1 : 1,
                //     titre: data.titre,
                //     auteur: data.auteur
                //     };
                //     livres.push(nouveauLivre);
                //     ecrireLivres(livres);
                //     res.writeHead(201, { 'Content-Type': 'application/json' });
                //     res.end(JSON.stringify(nouveauLivre));
                // } catch (err) {
                //     res.writeHead(400, { 'Content-Type': 'text/plain' });
                //     res.end('Données invalides');
                // }
                // });
                break;
            case '/donnees':
                // req.on('data', chunk => {
                //     body += chunk.toString();
                // });

                // req.on('end', () => {
                //     console.log('Requête reçue :', body);
                //     res.writeHead(200, { 'Content-Type': 'application/json' });
                //     res.end('Reçu\n');
                // });
                break;
            default:
                errorMessage();
                break;
        }
    } else if (method === "GET"){
        switch (direction){
            case '/mesures':
                    const mesures = readJsonFile('./Template_JSON/JSON-MESURES.json');
                    res.writeHead(200, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify(mesures))
                break;
            case '/ordres-leds':
                    const leds = readJsonFile('./Template_JSON/JSON-LED-STATE.json');
                    res.writeHead(200, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify(leds))
                break;
            default:
                errorMessage();
                break;
        }
    } else {

    }

});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Serveur en écoute sur le port ${PORT}`);
});