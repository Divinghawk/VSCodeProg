// https://stackoverflow.com/questions/36975619/how-to-call-a-rest-web-service-api-from-javascript/36975778#36975778

JS-FILE
window.onload = function() {
    document.getElementById('button').addEventListener('click', function () {
        fetch('https://1outhc3q8b.execute-api.us-east-1.amazonaws.com/default/sose21s_s0569617_?key1=value1')
        .then((response) => {
            return response.text();
        })
        .then((myContent) => {
            document.querySelector('.content').innerHTML = myContent;
        });
    
    }, false);
}