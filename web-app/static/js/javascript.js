$(document).ready(function() {
    var questions;
    function checkIfCharacterIs(reality,score) {
        if(questions[score][1] == reality){
            if(reality == true){
                $('#image-show').attr("src",questions[score][2]);
            }else{
                $('#image-show').attr("src","/static/images/fake.png");
            }
            score++;
            $('#score').html('Score: '+score);
            $('a.next').css('display','block');
        }else{
            $('#character').html('Game Over');
            $('.ans').css('display','none');
            $('a.retry').css('display','block');
        }
      }
    $('a.next').click(function(){
        var score = $("#score").text();
        score = score.substring(7,score.length);
        score = parseInt(score);
        $('#image-show').attr("src","/static/images/question_mark.png");
        $('#character').html(questions[score][0]);
        $('a.next').css('display','none');
        $('.ans').css('display','block');
    })
    $('a.retry').click(function(){
        $('#score').html('Score: 0');
        $('.progress').css('display','flex');
        $('.ans').css('display','none');
        $('.next-retry').css('display','none');
        $.ajax({
            type: 'GET',
            url: '/get-characters',
            success: function(data) {
               questions = data['characters']
               $('.progress').css('display','none');
               $('.ans').css('display','block');
               $('#character').html(questions[0][0]);
            },
            error:function(error){
               $('.progress').css('display','none');
               $('#character').html("An error occured please try again");
            }
        })
    })
    $('a.real').click(function() {
        //event.preventDefault();
        var score = $("#score").text();
        score = score.substring(7,score.length);
        score = parseInt(score);
        checkIfCharacterIs(true,score);
        $('.ans').css('display','none');
    })

    $('a.fake').click(function(){
        var score = $("#score").text();
        score = score.substring(7,score.length);
        score = parseInt(score);
        checkIfCharacterIs(false,score);
        $('.ans').css('display','none');
    })

    
    $.ajax({
        type: 'GET',
        url: '/get-characters',
        success: function(data) {
           questions = data['characters']
           $('.progress').css('display','none');
           $('#character').html(questions[0][0]);
        },
        error:function(error){
           $('.progress').css('display','none');
           $('#character').html("An error occured please try again");
        }
    })
});
;