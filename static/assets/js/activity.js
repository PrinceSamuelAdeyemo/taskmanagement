/*

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

*/

jQuery(function($){
    $(document).on('load', function(event){
        event.preventDefault();

        $.ajax({
            type: GET,
            url: '/activities',
            
            success: function(data){
                $('#totalproject-count').text(`Projects (${totalprojects.length})`)
                alert("Received");
            },
            error: function(data){
                alert('Not Received');
            },

        })
        .done(function(){
            window.location.href = '/activities'
        })
        })
    
})