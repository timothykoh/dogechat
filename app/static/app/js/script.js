$(window).load(function(){
    $(".page_switcher").click(function(){
        $(".page_switcher").removeClass("selected");
        $(this).addClass("selected");
        switchPage($(this).data("pageid"));
    });

    $("#chat").on("click", ".chat_item", function(){
        $("#doge_page").addClass("shown");
        $("#doge_top_bar span").html($(this).find(".nickname").html());
    });
    $("#doge_back").click(function(){
        $("#doge_page").removeClass("shown");
    });
});

function switchPage(pageid){
    $(".page").removeClass("selected");
    $("#" + pageid).addClass("selected");
}