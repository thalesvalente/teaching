$(".toggle-password").click(function () {
    $(this).toggleClass("fa-eye fa-eye-slash");
    var input = $($(this).attr("toggle"));
    if (input.attr("type") == "text") {
        input.attr("type", "password");
    } else {
        input.attr("type", "text");
    }
});