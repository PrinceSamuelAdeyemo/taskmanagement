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
    $('#activitypagebutton').on('click', function(){
        var openPage = () =>{
            $activitypage.css('display', 'flex');
            
        };
        setTimeout(openPage, 500);
        
    });
})