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
        console.log(dogetext);
        dogetextArr = dogetext.split(",");
        randTopArr = [];
        randLeftArr = [];
        min_num = 10;
        max_num = 80;
        doge_colors = ["red", "blue", "green", "yellow", "purple", "pink"];
        doge_colors.sort(function() {
            return .5 - Math.random();
        });
        for (var i = 0; i < dogetextArr.length; i++){
            dogetextItem = $("<span class='doge_text'>" + dogetextArr[i] + "</span>");

            randTop = getRandRange(min_num, max_num);
            while(randClash(randTop, randTopArr, 3)){
                randTop = getRandRange(min_num, max_num);
            }
            randTopArr.push(randTop);

            randLeft = getRandRange(min_num, max_num);
            while(randClash(randLeft, randLeftArr, 3)){
                randLeft = getRandRange(min_num, max_num);
            }
            randLeftArr.push(randLeft);

            doge_color = doge_colors[i%doge_colors.length];

            dogetextItem.css("top", randTop + "%");
            dogetextItem.css("left", randLeft + "%");
            dogetextItem.css("color", doge_color);
            $("#doge_text_area").append(dogetextItem);
        }

    });
    $("#doge_back").click(function(){
        $("#doge_page").removeClass("shown");
    });
    $("#add_but").click(function(){
        $("#contacts_title").html("Add Friend");
        $(this).css("display", "none");
        $("#search_field").css("display", "block");
        $("#add_back").css("display", "block");
        $("#search_form").css("display","block");
    })
    $("#add_back").click(function(){
        $("#contacts_title").html("Friend");
        $(this).css("display", "none");
        $("#search_field").css("display","none");
        $("#add_but").css("display", "block");
        $("#search_page").css("display","none");
    });
    $("#search_form").submit(function(e){
        e.preventDefault();
        var search_term = $("#search_field").val();
        if (search_term === ""){
            alert("Search term required.");
        }
        else{
            $.ajax({
                url: "",
                type: "GET",
                data:{
                    "term": search_term
                },
                success: function(user_array){
                    console.log(user_array);
                },
                error: function(err){
                    console.log(err);
                }
            });
        }
    });
    $(".contact").click(function(){
        $("#send_chat_popup").addClass("shown");
        window.send_userid = $(this).data("userid");
    });
    $("#send_chat_popup").click(function(e){
        if (e.target != this){
            return;
        }
        $(this).removeClass("shown");
    });
    $("#send_chat_form").submit(function(e){
        e.preventDefault();
        var msg = $("#send_chat_field").val();
        if (msg === ""){
            alert("Message is required.");
        }
        else{
            $("#send_chat_field").val("");
            $("#send_chat_popup").removeClass("shown");
            $.ajax({
                url: "send_msg",
                type: "GET",
                data: {
                    "rec_pri_id": window.send_userid,
                    "dogetext": msg
                },
                success: function(results){
                    alert("Message Sent!");
                }
            });
        }
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
