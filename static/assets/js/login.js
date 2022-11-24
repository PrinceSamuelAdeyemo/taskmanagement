jQuery(function($){


    // For signup view



    // For login view
    $("#businesslogin").hide();
    
    $("#personallogintrigger").on("click", function(event){
        
        $("#businesslogin").css("display", "none");
        $("#personallogin").css("display", "block");
    });
    $("#businesslogintrigger").on("click", function(event){
        
        $("#personallogin").css("display", "none");
        $("#businesslogin").css("display", "block");
        
    })
    /*
    $("#getPersonalOrBusiness").on('submit', function(event){
        $.ajax({
            type: 'POST',
            url: '/login',
            data: {
                email : $("#email").val(),
                password : $("password").val(),
                csrfmiddlewaretoken : $("[input[name=csrfmiddlewaretoken]").val()
            },
            success: function(response){
                $("#personallogintrigger").on('click', function(event){
                    event.preventdefault();
                    $("#businesslogin").css("display", "none");
                    $("personallogin").css("display", "block")
                    alert("done");
                });
            },
            error: function(response){
                alert('Error')
            },
            

    
            /*
            data: {
                email: $("#email").val(),
                password:$("#password").val(),
                
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            }
            
        })
    })

    */
    /*
    $("#getPersonalOrBusiness").on('submit', function(event){
        event.preventdefault();
        var $form = $(this);
    });
    
    $("#personallogintrigger").on('click', function(event){
        event.preventdefault();
        $("#businesslogin").css("display", "none");
        $("personallogin").css("display", "block");
    });

    $("#businesslogintrigger").on('click', function(event){
        event.preventdefault();
        $("personallogin").css("display", "none");
        $("#businesslogin").css("display", "block");
    });

    $("#personallogintrigger").on('click', function(){
        $(".hello").hide()
    })
*/
   
    
});