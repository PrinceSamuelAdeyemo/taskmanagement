jQuery(function($){
    
    $taskpage = $('#task-panel');

    //Close the create-task window
    $('#canceltaskpage').on('click', function(){
        console.log("Stopped");
        var openPage = () =>{
            $taskpage.css('display', 'none');
        };
        setTimeout(openPage, 500);
        
    });

    // Open the create-task window
    $('#create-task').on('click', function(){
        console.log("Started");
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

    
var subTaskArray = new Array()
// Actions done when the create task button is pressed.
    $('#createtask').on('click', function(event){
        event.preventDefault();
        var $form  = $(this);
        
        if ( $('#task_name').val() != ''){
            $.ajax({
                type: 'POST',
                //url: $form.attr('action'),
                url: '/createtask',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    task_name : $('#task_name').val(),
                    task_description : $('#task_description').val(),
                    //subtaskinput : $('#subtaskinput').val(),
                    subTaskArray : subTaskArray,
                    //csrfmiddlewaretoken: "{{ csrf_token }}",
                    //task_nam: $('#task_name'),
                    //task_descriptio: $('#task_description'),
        
                },
                success: function(data){
                    
                    console.log("Data submitted successfully!");
                    console.log(subTaskArray);
                    //console.log($('#subtaskinput').val());
                },
    
                error: function(data){
                    alert("Data not submitted.");
                },
            })
        }
        else{
            alert('input task name')
        }

        /*
        $.ajax({
            type: 'POST',
            url: '/createsubtask',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                subtaskinput : $('#subtaskinput').val(),
                task_name : $('#task_name').val(),
                task_description : $('#task_description').val(),
            },
            success: function(data){
                alert("Done!");
            },

            error: function(data){
                alert("not done.");
            },
        });
        */
        
        
    });

    
    /*
    $task_nameinput.on('focus', function(event){
        if ($task_name == ''){
            $subtaskerror.text('focus not');
        }
        else{
            $subtaskerror.text('focus');
        }
    });
    */


    var $task_name = $('#task_name');
    var $subtask = $('#subtaskinput');
    var $subtaskerror = $('#subtaskerror');
    
    var $savesubtask = $('#savesubtask');
    var $subtaskitems = $('#subtaskitems');
    
    var subtaskitem;

    $subtask.on('keydown', function(event){
        var $task_name = $('#task_name');
        var $subtask = $('#subtaskinput');
        var $subtaskerror = $('#subtaskerror');

        if ($task_name.val() == '' && $subtask.val() != ''){
            $subtaskerror.text('Please enter a task name');
        }
        else{
            $subtaskerror.text('');
        }
    })

    
    $task_name.on('keydown', function(event){
        var $task_name = $('#task_name');
        var $subtask = $('#subtaskinput');
        var $subtaskerror = $('#subtaskerror');

        if ($('#task_name').val() == '' && $('#subtaskinput').val() != ''){
            //if ($subtaskerror.val() == 'Please enter a task name'){
                $('#subtaskerror').text('Please enter a task name');
            //}
        }
        else if ($('#task_name').val() != '' && $('#subtaskinput').val() == ''){
            //if ($subtaskerror.val() == 'Please enter a task name'){
                $('#subtaskerror').text('');
            //}
        }
        else{
            $('#subtaskerror').text('');
        }
    });
    
    
    $('#savesubtask').on('click', function(event){
        event.preventDefault();
        var $subtaskinput = $('#subtaskinput').val()
        var $task_name = $('#task_name').val();
        
        var $subtaskerror = $('#subtaskerror');

        if ($task_name == ''){
            $subtaskerror.text('Please insert Task name');
        }
        else{
            $subtaskerror.text('');
////
            if ($subtask.val() !== ''){
                console.log("Not empty")
                subtaskitem  = `<li><span><i class='bi bi-list-task'></i></span><input class='mx-1' type='checkbox' id='subtask'>${$subtask.val()}</li>`
                subTaskArray.push($subtask.val());
    
                $subtaskitems.append(subtaskitem);
                $('#subtaskinput').val('');
                $('#subtaskinput').attr('autofocus', 'true');

                console.log('Success')
            }
            else{
                console.log("Sub task is empty")
            }
            
///////////
            
        }
    });


   /* 
    var $savesubtask = $('#savesubtask');
    var $subtaskitems = $('#subtaskitems');
    var subTaskArray = new Array()
    var subtaskitem;
    $savesubtask.on('click', function(event){
        event.preventDefault();
        if ($subtask.val() !== ''){
            console.log("Not empty")
            subtaskitem  = `<li><span><i class='bi bi-list-task'></i></span><input class='mx-1' type='checkbox' id='subtask'>${$subtask.val()}</li>`
            subTaskArray.push($subtask.val());

            $subtaskitems.append(subtaskitem);
            $('#subtaskinput').val('');
            $('#subtaskinput').attr('autofocus', 'true');
            console.log('Success')
        }
        else{
            console.log("Sub task is empty")
        }
    });

    $('#discardsubtask').on('click', function(event){
        event.preventDefault();
        //$('#subtaskinput').val('Bug here');
        
    });
    */
    
});