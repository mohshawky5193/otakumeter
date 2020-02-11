$(document).ready(function() {
    var questions;
    function checkIfCharacterIs(reality,score) {
        if(questions[score][1] == reality){
            score++;
            $('#score').html('Score: '+score);
            $('#character').html(questions[score][0]);
        }else{
            $('#character').html('Game Over');
            $('.ans').css('display','none');
        }
      }
    $('a.real').click(function() {
        //event.preventDefault();
        var score = $("#score").text();
        score = score.substring(7,score.length);
        score = parseInt(score);
        checkIfCharacterIs(true,score);
    })

    $('a.fake').click(function(){
        var score = $("#score").text();
        score = score.substring(7,score.length);
        score = parseInt(score);
        checkIfCharacterIs(false,score);
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