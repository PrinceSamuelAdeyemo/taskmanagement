jQuery(function($){
    $activitypage = $('#activity-panel');

    $('#cancelactivitypage').on('click', function(){
        var closePage = () =>{
            $activitypage.css('display', 'none');
        }
        setTimeout(closePage, 500);
    });

    $('#activitypagebutton').on('click', function(){
        var openPage = () =>{
            $activitypage.css('display', 'flex');
        }
        setTimeout(openPage, 500);
        
    });
})