$(document).ready(function () {
    var questions;

    function checkIfCharacterIs(reality, score) {
        if (questions[score][1] == reality) {
            if (reality == true) {
                $('#image-show').attr("src", questions[score][2]);
            } else {
                $('#image-show').attr("src", "/static/images/fake.png");
            }
            score++;
            $('#score').html('Score: ' + score);
            $('a.next').css('display', 'block');
        } else {
            $('#character').html('Game Over');
            $('.ans').css('display', 'none');
            $('a.retry').css('display', 'block');
        }
    }
    $('a.next').click(function () {
        var score = $("#score").text();
        score = score.substring(7, score.length);
        score = parseInt(score);
        $('#image-show').attr("src", "/static/images/question_mark.png");
        $('#character').html(questions[score][0]);
        $('a.next').css('display', 'none');
        $('.ans').css('display', 'block');
    })
    $('a.retry').click(function () {
        shuffle(questions)
        $('#character').html(questions[0][0]);
        $('.ans').css('display', 'block');
        $('a.retry').css('display', 'none');
        score = 0;
        $('#score').html('Score: ' + score);
    })
    $('a.real').click(function () {
        //event.preventDefault();
        var score = $("#score").text();
        score = score.substring(7, score.length);
        score = parseInt(score);
        checkIfCharacterIs(true, score);
        $('.ans').css('display', 'none');
    })

    $('a.fake').click(function () {
        var score = $("#score").text();
        score = score.substring(7, score.length);
        score = parseInt(score);
        checkIfCharacterIs(false, score);
        $('.ans').css('display', 'none');
    })


    $.ajax({
        type: 'GET',
        url: '/get-characters',
        success: function (data) {
            questions = data['characters']
            $('.progress').css('display', 'none');
            $('#character').html(questions[0][0]);
        },
        error: function (error) {
            $('.progress').css('display', 'none');
            $('#character').html("An error occured please try again");
        }
    })

    function shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i

            // swap elements array[i] and array[j]
            // we use "destructuring assignment" syntax to achieve that
            // you'll find more details about that syntax in later chapters
            // same can be written as:
            // let t = array[i]; array[i] = array[j]; array[j] = t
            [array[i], array[j]] = [array[j], array[i]];
        }
    }
});;