// Load the AWS SDK for Node.js
var AWS = require('aws-sdk');
// Set the region 
AWS.config.update({region: 'REGION'});

// Create the DynamoDB service object
var ddb = new AWS.DynamoDB({apiVersion: '2012-08-10'});

let ID = 7199;
let countryRegion = 'Germany';
let federalstate = 'Thuringia';
let infections = 126214;
let deaths = 9546;
let date = 2021-05-22;
let newinfections = 230;
let newdeaths = 4;

/** Tabellen Data für AWS DynamoDB RKI_DATA_Grp7 */
var params = {
  TableName: 'RKI_DATA_Grp7',
  Item: {
    'ID' : {N: ID},
    'CountryRegion' : {S: countryRegion},
    'federalstate' : {S: federalstate},
    'infections' : {S: infections},
    'deaths' : {S: deaths},
    'date' : {S: date},
    'newinfections' : {S: newinfections},
    'newdeaths' : {S: newdeaths}

  }
};

// Call DynamoDB to add the item to the table
ddb.putItem(params, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});