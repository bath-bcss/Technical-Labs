
//This puts data into html on the page
function displayUserData(data){
    data = JSON.parse(data);
    data.business = data.business == "true"//Converts the string into a boolean
    console.log(data)
    if(data.first == undefined){
        $('#userdata').html(`
            <h1>No stored user, please enter your details</h1>
        `);
    }else{
        //Uses an inline if statement to decide what to say
        $('#userdata').html(`
            <h1>Your name is ${data.first} ${data.second} and ${(data.business) ? "you are a business student." : "you are not a business student"}</h1>
        `);
    }
}

$(document).ready(function(){
    //Get the user data on page load
    $.get("api/userdata", function(data){
        displayUserData(data);
    });


    $('#send').click(function(){
        let first = $('#firstname').val();
        let second = $('#secondname').val();
        let bus = $('#business').is(":checked");

        $.post("api/userdata", {first: first, second: second, business: bus}, function(data){
            displayUserData(data);
        });
    });
});