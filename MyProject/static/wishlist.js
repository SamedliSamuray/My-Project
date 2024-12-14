document.addEventListener('DOMContentLoaded', function() {
    const myList = document.querySelector('.menu');
    const liItems = myList?myList.querySelectorAll('li'):null;
    
    if(liItems){
      liItems.forEach(function(li) {
        li.addEventListener('click', function() {

            liItems.forEach(function(item) {
                item.classList.remove('active');
            });
            li.classList.add('active');
        });
    });
    }
});

function togglePassword(e) {
    const passwordInput = e.target.previousElementSibling;
  
   
    if (passwordInput.getAttribute('type') === "password") {
      passwordInput.type = "text";
      e.target.classList.remove("fa-eye");
      e.target.classList.add("fa-eye-slash");
    } else {
      passwordInput.type = "password";
      e.target.classList.remove("fa-eye-slash");
      e.target.classList.add("fa-eye");
    }
  }
  