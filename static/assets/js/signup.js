jQuery(function($){
    $("#businessSignup").hide();
    
    $("#personalSignupTrigger").on("click", function(event){
        
        $("#businessSignup").css("display", "none");
        $("#personalSignup").css("display", "block");
        event.preventdefault();
    });

    $("#businessSignupTrigger").on("click", function(event){
        
        $("#personalSignup").css("display", "none");
        $("#businessSignup").css("display", "block");
        event.preventdefault();
    })
})