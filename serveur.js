const http = require('http');
const fs = require('fs');
const url = require('url');
const path = require('path');

function errorMessage(message){
    res.writeHead(400, { 'Content-Type': 'text/plain' });
    res.end(message)
}

function readJsonFile(file){
    const data = fs.readFileSync(file, 'utf-8')
    return JSON.parse(data)
}

function getDonnees(){
    const data = readJsonFile('./Template_JSON/JSON-MESURES.json');
    const mesures = data['dht'];
    return mesures
}

function writeLed(key, value){
    const data = readJsonFile('./Template_JSON/JSON-LED-STATE.json');
    data[key] = value;
    fs.writeFileSync('./Template_JSON/JSON-LED-STATE.json', JSON.stringify(data, null, 2));
    writeDonnees(data, 'led')
}

function writeDonnees(entry, key){
    const data = readJsonFile('./Template_JSON/JSON-MESURES.json');
    data[key] = entry;
    fs.writeFileSync('./Template_JSON/JSON-MESURES.json', JSON.stringify(data, null, 2));
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
                body = '';
                req.on('data', chunk => body += chunk);
                req.on('end', () => {
                    try{
                        console.log('Données POST:', body);
                        const data = JSON.parse(body);
                        const key = Object.keys(data)[0]
                        const value = data[key]
                        writeLed(key, value)
                        res.writeHead(201);
                        res.end(`Données reçues : ${body}`);
                    } catch (err){
                        errorMessage('Données invalides');
                    }
                });
                break;
            case '/donnees':
                body = '';
                req.on('data', chunk => body += chunk);
                req.on('end', () => {
                try {
                    const data = JSON.parse(body);
                    const mesures = getDonnees();
                    if (mesures.length === 10){
                        mesures.shift();
                    }
                    
                    mesures.push(data)
                    writeDonnees(mesures, 'dht');
                    res.writeHead(201, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify(data));
                } catch (err) {
                    errorMessage('Données invalides');
                }
                });
                break;
            default:
                errorMessage('Ce URL n\'existe pas');
                break;
        }
    } else if (method === "GET"){
        switch (direction){
            // case '/':
            // case '/index.html':
            //     filePath = path.join(__dirname, 'public', 'index.html');
            //     break;
            // case '/mesure':
            //     filePath = path.join(__dirname, 'public', 'page1.html');
            //     break;
            // case 'led-cmd':
            //     filePath = path.join(__dirname, 'public', 'page2.html');
            //     break;
            // case '/led-state':
            //     filePath = path.join(__dirname, 'public', 'page3.html');
            //     break;
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
                errorMessage('Ce URL n\'existe pas');
                break;
        }

        // fs.readFile(filePath, (err, data) => {
        //             if (err) {
        //                 res.writeHead(500);
        //                 res.end('Erreur serveur');
        //                 return;
        //             }
        //             res.writeHead(200, { 'Content-Type': 'text/html' });
        //             res.end(data);
        // });
    } else {
        errorMessage('Cette fonction n\'est pas disponible');
    }

});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Serveur en écoute sur le port ${PORT}`);
});