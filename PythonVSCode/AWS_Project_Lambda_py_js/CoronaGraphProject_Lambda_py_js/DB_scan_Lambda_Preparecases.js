const AWS = require('aws-sdk')
const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'});

exports.handler = async (event, context, callback) => {
    await readMessage().then(data =>{
        data.Items.forEach(function(item) {
            console.log(item.id)
            console.log(item.CountryRegion)
            console.log(item.federalstate)
            console.log(item.infections)
            console.log(item.deaths)
            console.log(item.date)
            console.log(item.newinfections)
            console.log(item.newdeaths)
            })
    }).catch((err) =>{
        console.error(err);
    })
};

function readMessage() {
    const params = {
        TableName: 'RKI_DATA_Grp7',
        Limit: 10
    }
    return ddb.scan(params).promise();
}
