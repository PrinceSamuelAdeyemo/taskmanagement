jQuery(function($){
    $taskpage = $('#task-panel');

    //Close the create-task window
    $('#canceltaskpage').on('click', function(){
        var openPage = () =>{
            $taskpage.css('display', 'none');
        };
        setTimeout(openPage, 500);
        
    });

    // Open the create-task window
    $('#create-task').on('click', function(){
        var openPage = () =>{
            $taskpage.css('display', 'flex');
        };
        setTimeout(openPage, 500);
        
        
    });


/*
    $('#form-panel-output').on('submit', function(event){
        event.preventDefault();

        /*
        var name = $('#task_name').val();
        $.ajax({
            url: '/add_record',
            type: 'POST',
            headers: { "X-CSRFToken": $('input[name=csrfmiddlewaretoken]').val() },
            data: {
            'task_name': name,
            },
            success: function (response) {
            alert(response.data)
            },
            error: function(){
                alert('error')
            }
        });
        *



    })
    
*/

    

    $('#form-panel-output').on('submit', function(event){
        event.preventDefault();
        var $form  = $(this);

        $.ajax({
            type: 'POST',
            //url: $form.attr('action'),
            url: '/createtask',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                task_name : $('#task_name').val(),
                task_description : $('#task_description').val(),
                subtaskinput : $('#subtaskinput').val(),
                //csrfmiddlewaretoken: "{{ csrf_token }}",
                //task_nam: $('#task_name'),
                //task_descriptio: $('#task_description'),
    
            },
            success: function(data){
                alert("Data submitted successfully!");
            },

            error: function(data){
                alert("Data not submitted.");
            },
        })
        
    });

/*
    $('#savesubtask').on('click', function(event){
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/createtas',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                subtaskinput : $('#subtaskinput').val(),
            },
            success: function(data){
                alert("Done!");
            },

            error: function(data){
                alert("not done.");
            },
        })
    })
    */
    
});