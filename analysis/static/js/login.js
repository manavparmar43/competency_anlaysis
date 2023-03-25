function fogottenpwd(){
    $("#heading").text('');
    $("#heading").text("Forgotten Password");
    $("#heading").css("font-size","30px");
    $("#innerheading").text("");
    $("#innerheading").text("Enter Register Username And Email");
    $("#innerheading").css("font-size","15px");
    $("#inputdiv").html("");
    $("#inputdiv").append(`<input style="margin-top:2%;" type="text" placeholder="Register Username" name="forgottenusername"/>
    <input type="text" placeholder="Register Email" name="forgottenemail"/>`);
    $("#btn").html("");
    $("#btn").append(`<button type="submit">Submit</button>`);
    $("#forgottenbtn").html("");
    $("#forgottenbtn").append(`<a href="#" style="font-size: 17px;" onclick="loginbtn()"><b>Login</b></a>`);
  
}   
function loginbtn(){
    $("#heading").text('');
    $("#heading").text("Login Here");
    $("#heading").removeAttr("style");
    $("#innerheading").text("");
    $("#innerheading").text("or use your account");
    $("#innerheading").removeAttr("style");
    $("#inputdiv").html("");
    $("#inputdiv").append(`<input type="text" placeholder="Username" name="username"/>
    <input type="password" placeholder="Password" name="password"/>`);
    $("#btn").html("");
    $("#btn").append(`<button type="submit">Login</button>`);
    $("#forgottenbtn").html("");
    $("#forgottenbtn").append(`<a href="#" style="font-size: 17px;" onclick="fogottenpwd()"><b>Fogotten Password</b></a>`);
}
  
