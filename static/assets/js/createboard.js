jQuery(function($){

    /* Creating a board with project or without a project chosen or created. */
    /* Get the values inputted and submit to the database. */

    // Project values
    var $projectpage = $('#project-panel');
    var $projectname = $('#projectname');


    // Board values
    var $board_name = $('#board_name');
    var $board_description = $('#board_description');


    // Task values
    var $task = $('#taskinput');
    var $taskerror = $('#taskerror');
    var $savetask = $('#savetask');
    var $taskitems = $('#taskitems');
    var taskitem;
    var TaskArray = new Array();
    var $TaskArrayServer;


    // ######################## Project works  ########################

    // Link to the project and board creation page.
    $('#openProjectPage').on('click', function(){
        var openPage = () =>{
            //$('.afterprojectchosen').css('display', 'flex');
            //$('.chooseproject').css('display', 'none');
            window.location.href = '/createboard'
        };
        setTimeout(openPage, 500);
    });

    // Function for Showing/Opening the board page and hiding the project creation page
    var openPage = () =>{
        $('.afterprojectchosen').css('display', 'block');
        $('.chooseproject').css('display', 'none');
        $('#project-name').text($projectname.val());
    };

    // Cancel and leave the board creation page and go back to the project 'creation and choosing' stage.
    $('#cancelboardpage').on('click', function(){
        var closePage = () =>{
            $('.chooseproject').css('display', 'flex');
            $('.afterprojectchosen').css('display', 'none');
            //window.location.href = '/dashboard'
        };
        setTimeout(closePage, 500);
    });

    //  Create the project and Open the create-board window
    $('#create-a-project').on('click', function(event){
        event.preventDefault();
        
        $.ajax({
            type: 'POST',
            //url: $form.attr('action'),
            url: '/createproject',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                project_description: "Default",
                action: "create-a-project",
                project_name : $projectname.val(),
                /*board name and details
                board_name : $board_name.val(),
                // Task name and details
                task_name : $('#taskinput').val(),
                task_description : $('#task_description').val(),
                taskinput : $('#taskinput').val(),
                TaskArray : TaskArray
                */
            },
            success: function(data){
                console.log("Project submitted successfully!");
                setTimeout(openPage, 500);
            },

            error: function(data){
                alert("Project not submitted.");
                console.log(data);
            },
        });
        
    });


    //Close the create-project window and redirect to the dashboard
    $('#cancelprojectpage').on('click', function(){
        var closePage = () =>{
            window.location.href = '/dashboard'
            //$projectpage.css('display', 'none');
        };
        setTimeout(closePage, 500);
        
    });




    $task.on('keydown', function(event){
        if ($board_name.val() == '' && $task.val() != ''){
            $taskerror.text('Please enter a board name');
        }
        else{
            $taskerror.text('');
        }
    })

    $('#savetask').on('click', function(event){
        event.preventDefault();
        
        if ($board_name.val() == ''){
            $taskerror.text('Please insert board name');
        }
        else{
            $taskerror.text('');
        ////
            if ($task.val() !== ''){
                taskitem  = `<li><span><i class='bi bi-list-task'></i></span><input class='mx-1' type='checkbox' id='task'>${$task.val()}</li>`
                console.log(TaskArray.length);
                if (TaskArray.length > 9){
                    $taskerror.text('Maximum of 10 tasks per board can be created');
                    
                }else{
                    TaskArray.push($task.val());
                    $taskitems.append(taskitem);
                }
                

                $taskerror.val()
                $('#taskinput').val('');
                $('#taskinput').attr('autofocus', 'true');
                //$TaskArrayServer.val(`${TaskArray}`);
                //console.log($TaskArrayP.val())
                

                console.log('Success')
                console.log(TaskArray)
            }
            else{
                console.log("Task is empty")
            }
    ///////////
        }
    });


    // #################### Board works     ##################
    // Create a board
    $('#create-a-board').on('click', function(event){
        if (TaskArray != ''){
            //var jsonlist = JSON.stringify($TaskArrayP.val())
            
            $.ajax({
                type: 'POST',
                //url: $form.attr('action'),
                url: '/createboard',
                data: {
                    action: 'create-a-board',
                    // csrfmiddlewaretoken data
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    // project name and details
                    project_name : $projectname.val(),
                    // board name and details
                    board_name : $board_name.val(),
                    board_description: $board_description.val(),
                    // Task name and details
                    //task_name : $('#taskinput').val(),
                    //task_description : $('#task_description').val(),
                    //taskinput : $('#taskinput').val(),
                    
                    TaskArray : TaskArray
                },
                success: function(data){
                    console.log("Project submitted successfully!");
                },

                error: function(data){
                    alert("Project not submitted.");
                },
            });
        }
        
        else{
            $.ajax({
                type: 'POST',
                url: '/createboard',
                data: {
                    action: 'create-a-board',
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    project_name : $projectname.val(),
                    board_name : $board_name.val(),
                    board_description: $board_description.val(),
                },
                success: function(data){
                    alert("Done!");
                    console.log(data);
                },
    
                error: function(data){
                    console.log(TaskArray);
                    alert("not done.");
                },
            });
        }
    });
}
);