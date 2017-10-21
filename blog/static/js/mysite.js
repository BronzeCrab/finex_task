$(document).ready(function() {
    // switch navbar
    const regex = /http:\/\/.*\/(.*\/)/g;
    const match = regex.exec(window.location.href);
    // iterate over all and find match
    if (match) {
        $(".nav-link").each(function() {
            if ($(this).attr("href").slice(1) == match[1]) {
                $(this).addClass("active");
            }
        });
    }
    // set active first element
    else {
        $(".nav-link:first").addClass("active");
    }

    // like click
    $('.like').click(function(){
        var user_id = $(this).siblings(".user_id").text();
        var entry_id = $(this).siblings(".entry_id").text();
        $.ajax({
            url : "/like/"+user_id, // the endpoint
            type : "GET", // http method
            data : {action: "like",
                    entry_id: entry_id},
            success: function(json) {
              if(json.error) return;
                $(document).ajaxStop(function() { location.reload(true); });
            }
        }); 
    });

    // dislike click
    $('.dislike').click(function(){
        var user_id = $(this).siblings(".user_id").text();
        var entry_id = $(this).siblings(".entry_id").text();
        $.ajax({
            url : "/like/"+user_id, // the endpoint
            type : "GET", // http method
            data : {action: "dislike",
                    entry_id: entry_id},
            success: function(json) {
              if(json.error) return;
                $(document).ajaxStop(function() { location.reload(true); });
            }
        }); 
    });

});