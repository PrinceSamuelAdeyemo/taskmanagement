jQuery(function($){
    $('#login').on('click', function(){
        $.ajax({
            type: 'GET',
            url: '/authuser',
            success: function(response){
                if (response.user === 'is_not_authenticated'){
                    console.log('Not logged in');
                    window.location.href = 'login.html';
                    
                    
                }
                else if (response.user === 'is_authenticated'){
                    window.location.href = '/dashboard';
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
})