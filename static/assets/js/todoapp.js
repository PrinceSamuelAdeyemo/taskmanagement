//const jquery = require("jquery");

jQuery(function($){
    
})

var xArray = ["", "Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"];
var yArray = [3,7,8,8,9,9,9,10,];

// Define Data
var data = [{
x: xArray,
y: yArray,
mode: "lines",
type: "scatter",
line: {
    color: 'rgb(248, 212, 9)'
}
}];

// Define Layout
var layout = {
xaxis: {range: [], title: ""},
yaxis: {range: [5, 16], title: ""},
title: "",
plot_bgcolor: '#2c405b',
//paper_bgcolor: 'red',
paper_bgcolor: '#2c405b',
font: {
    color: 'gray',
    family: 'Open Sans',
    size: 10,
},
colorway: '#d62728',
autosize: false,
width: 600,
height: 250,

margin: {
    l: 15,
    r: 15,
    b: 15,
    t: 15,

    color: 'blue',
    
},

calendar: 'chinese',
};

// Display using Plotly
tester = document.getElementById('tester');
Plotly.newPlot('tester', data, layout);
