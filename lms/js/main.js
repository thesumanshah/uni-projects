document.getElementById("loginForm").addEventListener("submit", function(event){
    event.preventDefault();
    
    const username=document.getElementById("username").value;
    const password=document.getElementById("password").value;
    
    const adminCredentials={username:"admin",password:"password123"};
    const studentCredentials={username:"student",password:"student123"};

if(username==adminCredentials.username && password==adminCredentials.password){
    window.location.href="dashboard.html";
}
else if(username==studentCredentials.username && password==studentCredentials.password){
    window.location.href="studentdashboard.html";
} else{
    alert("Invalid Username or Password");
}

});

