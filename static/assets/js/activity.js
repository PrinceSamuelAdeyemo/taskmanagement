jQuery(function($){
    $activitypage = $('#activity-panel');

    //Close the create-activity window
    $('#cancelactivitypage').on('click', function(){
        var openPage = () =>{
            $activitypage.css('display', 'none');
        };
        setTimeout(openPage, 500);
        
    });

    // Open the create-activity window
    $('#create-activity').on('click', function(){
        var openPage = () =>{
            $activitypage.css('display', 'flex');
        };
        setTimeout(openPage, 500);
        
    });
})