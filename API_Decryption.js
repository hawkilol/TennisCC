// If using CommonJS (e.g., Node.js)
const CryptoJS = require("crypto-js");
const axios = require('axios');
const fs = require('fs');

const userAgents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (iPad; CPU OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
    // Add more as needed
  ];

courtVisionUrl = 'https://itp-ao-sls.infosys-platforms.com/prod/api/court-vision/year/2024/eventId/580/matchId/MS701/pointId/0_0_0'

function getRandomUserAgent() {
  return userAgents[Math.floor(Math.random() * userAgents.length)];
}

function getCourtVisionData() {
    const headers = {
      'User-Agent': getRandomUserAgent(),
      'Content-Encoding': 'gzip',
      'Content-Security-Policy': "default-src 'self' itp-ao-sls.infosys-platforms.com itp-ao.infosys-platforms.com itp-dev.idemo-ppc.com https://ausopen.com https://players.ausopen.com *.ausopen.com https://sit-7oxbj4.ausopen.com https://dev-7oxbj4.ausopen.com fonts.googleapis.com https://www.google-analytics.com https://fonts.gstatic.com www.google-analytics.com https://www.googleapis.com https://securetoken.googleapis.com https://itp-video-feed-master.s3.ap-southeast-2.amazonaws.com https://itp-digital-feed-master.s3.eu-west-3.amazonaws.com data: 'unsafe-inline'; img-src 'self' itp-ao-sls.infosys-platforms.com itp-ao.infosys-platforms.com itp-dev.idemo-ppc.com https://ausopen.com https://players.ausopen.com *.ausopen.com https://sit-7oxbj4.ausopen.com https://dev-7oxbj4.ausopen.com fonts.googleapis.com https://www.google-analytics.com https://fonts.gstatic.com www.google-analytics.com https://www.googleapis.com https://securetoken.googleapis.com https://itp-video-feed-master.s3.ap-southeast-2.amazonaws.com https://itp-digital-feed-master.s3.eu-west-3.amazonaws.com data: blob: 'unsafe-inline'; object-src 'none'; worker-src 'self' blob:",
      'Content-Type': 'application/json',
      'Server': 'CloudFront'
      // Additional headers as needed
    };
  
    axios.get(courtVisionUrl, { headers: headers })
      .then(response => {
        // console.log(response.data);
        console.log(decode(response.data))
        fs.writeFile('output.json', JSON.stringify(decode(response.data)), (err) => {
            if (err) {
              console.error('An error occurred:', err);
              return;
            }
            console.log('JSON data has been saved to "output.json".');
        });
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
}
  
function decode(data) {
  var e = formatDate(new Date(data.lastModified))
    , n = CryptoJS.enc.Utf8.parse(e)
    , r = CryptoJS.enc.Utf8.parse(e.toUpperCase())
    , i = CryptoJS.AES.decrypt(data.response, n, {
      iv: r,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
  return JSON.parse(i.toString(CryptoJS.enc.Utf8))
};

function formatDate(t) {
  var e = (new Date).getTimezoneOffset(), n = new Date(t.getTime() + 60 * e * 1e3).getDate(), 
  r = parseInt((n < 10 ? "0" + n : n).toString().split("").reverse().join("")), i = t.getFullYear(), 
  a = parseInt(i.toString().split("").reverse().join("")), 
  o = parseInt(t.getTime().toString(), 16).toString(36) + ((i + a) * (n + r)).toString(24), 
  s = o.length;
  if (s < 14)
    for (var c = 0; c < 14 - s; c++)
      o += "0";


  else
    s > 14 && (o = o.substr(0, 14));
  return "#" + o + "$";
}

getCourtVisionData()