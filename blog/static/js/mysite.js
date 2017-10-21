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
        console.log('here');
        $(".nav-link:first").addClass("active");
    }
});