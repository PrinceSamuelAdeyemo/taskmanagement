jQuery(function($){
    $taskpage = $('#task-panel');

    $('#canceltaskpage').on('click', function(){
        var closePage = () =>{
            $taskpage.css('display', 'none');
        }
        setTimeout(closePage, 0);
    });

    $('#create-task').on('click', function(){
        var openPage = () =>{
            $taskpage.css('display', 'flex');
        }
        setTimeout(openPage, 0);
        
    });
})