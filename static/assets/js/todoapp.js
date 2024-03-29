//const jquery = require("jquery");

jQuery(function($){

    var $taskCompleted = $('#taskCompleted');
    var $taskInProgress = $('#taskInProgress');

    var getTask = () => {
        (function(event){
            event.preventDefault;
        });
        
        $.ajax({
            type: 'GET',
            //data: None,
            //url: "{% url 'bb' %}",
            url: "/getActivities",
            //dataType: "json",
            success: function(response){
                //console.log(response);
                // To get the current task completed from the server to ajax and then from ajax to the client side.
                if (response.user_activities_completed.length > 1) {
                    $taskCompleted.text(response.user_activities_completed.length + ' ' + 'Tasks');
                }
                else{
                    $taskCompleted.text(response.user_activities_completed.length + ' ' + 'Task');
                }


                // To get the current task inprogress from the server to ajax and then from ajax to the client side.
                if (response.user_activities_progress.length > 1) {
                    $taskInProgress.text(response.user_activities_progress.length + ' ' + 'Tasks');
                }
                else{
                    $taskInProgress.text(response.user_activities_progress.length + ' ' + 'Task');
                }

                /*
                // To get the current task not yet started from the server to ajax and then from ajax to the client side.
                if (response.user_activities_progress.length > 1) {
                    $taskInProgress.text(response.user_activities_progress.length + ' ' + 'Tasks');
                }
                else{
                    $taskInProgress.text(response.user_activities_progress.length + ' ' + 'Task');
                }
                */
            },
            error: function(response){
                alert('Wrong!')
                location.reload();
            },
        });

        
        
    };

    setInterval(getTask, 100000000);


    var getProjects = () => {
            window.location.href = '/activities';
    };

    $('#projectpage').on('click', function(){
        $.ajax({
            type: 'GET',
            url: '/authuser',
            success: function(response){
                if (response.user === 'is_not_authenticated'){
                    window.location.href = '/login';
                    console.log('Not logged in');
                    
                }
                else if (response.user === 'is_authenticated'){
                    window.location.href = '/activities';
                    console.log('Logged in');
                }
                else{
                    alert('Not receiving a valid response');
                    console.log(response);
                }
                
            },
            error: function(response){
                console.log('Not responding');
                console.log(response);
            }
        })
    });


var xArray = ["", "Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"];
var yArray = [3,7,8,8,9,9,9,10,];
//console.log(yArray.length)

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
plot_bgcolor: 'rgba(33, 101, 156, 0.854)',
//paper_bgcolor: '#2c405b',
paper_bgcolor: 'rgba(33, 101, 156, 0.854)',
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

})