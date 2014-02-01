$(window).load(function(){
    $(".page_switcher").click(function(){
        $(".page_switcher").removeClass("selected");
        $(this).addClass("selected");
        switchPage($(this).data("pageid"));
    });

    $("#chat").on("click", ".chat_item", function(){
        $("#doge_page").addClass("shown");
        $("#doge_top_bar span").html($(this).find(".nickname").html());
        $("#doge_text_area").empty();
        var dogetext = $(this).find(".dogetext").html();
        dogetextArr = dogetext.split(",");
        randTopArr = [];
        randLeftArr = [];
        min_num = 10;
        max_num = 80;
        for (var i = 0; i < dogetextArr.length; i++){
            console.log(i);
            dogetextItem = $("<span class='doge_text'>" + dogetextArr[i] + "</span>");

            randTop = getRandRange(min_num, max_num);
            while(randClash(randTop, randTopArr, 10)){
                randTop = getRandRange(min_num, max_num);
            }
            randTopArr.push(randTop);

            randLeft = getRandRange(min_num, max_num);
            while(randClash(randLeft, randLeftArr, 10)){
                randLeft = getRandRange(min_num, max_num);
            }
            randLeftArr.push(randLeft);

            dogetextItem.css("top", randTop + "%");
            dogetextItem.css("left", randLeft + "%");
            $("#doge_text_area").append(dogetextItem);
        }

    });
    $("#doge_back").click(function(){
        $("#doge_page").removeClass("shown");
    });
    $("#add_but").click(function(){
        $("#addfriend_page").addClass("shown");
    })
    $("#add_back").click(function(){
        $("#addfriend_page").removeClass("shown");
    });
});

function switchPage(pageid){
    $(".page").removeClass("selected");
    $("#" + pageid).addClass("selected");
}

function getRandRange(low, high){
    return (Math.random() * (high - low)) + low;
}

function randClash(randNum, randArr, diff){
    for (var i = 0; i < randArr.length; i++){
        if (Math.abs(randNum - randArr[i]) < diff){
            return true;
        }
    }
    return false;
}
