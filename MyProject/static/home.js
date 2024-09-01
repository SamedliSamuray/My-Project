document.addEventListener('DOMContentLoaded', function () {
    const paymentMethods = document.querySelectorAll('input[name="payment_method"]');
    const forms = document.querySelectorAll('.form-container');

    paymentMethods.forEach(paymentMethod => {
        paymentMethod.addEventListener('change', function () {
            forms.forEach(form => form.style.display = 'none');
            const selectedForm = this.closest('.debit_form').querySelector('.form-container');
            if (selectedForm) {
                selectedForm.style.display = 'flex';
            }
        });
    });
});


// Shipping address- city & country

var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};

fetch("https://countriesnow.space/api/v0.1/countries/population/cities", requestOptions)
    .then(response => response.json())
    .then(result => {
        const data = result.data;

        const cities = data.map(item => item.city).sort(); 
        const countries = [...new Set(data.map(item => item.country))].sort();
        const citySelect = document.getElementById('city');
        const stateSelect = document.getElementById('state');

        
        cities.forEach(city => {
            const option = document.createElement('option');
            option.value = city;
            city=='BAKU'?option.setAttribute('selected',''):null
            option.textContent = city;
            citySelect.appendChild(option);
        });

        
        countries.forEach(country => {
            if (country!=13) {
                const option = document.createElement('option');
                option.value = country;
                country=='Azerbaijan'?option.setAttribute('selected',''):null
                option.textContent = country;
                stateSelect.appendChild(option);
            }
            
        });
    })
    .catch(error => console.log('error', error));

// payments card number cvv code
function formatCardNumber(input) {
        let value = input.value.replace(/\D/g, '').replace(/ /g, '');
        value = value.replace(/(.{4})/g, '$1 ').trim();
        input.value = value;
}
function validateCVV(input) {
    let value = input.value.replace(/\D/g, '');
    value = value.slice(0, 4);
    input.value = value;
}

// up icon - yuxarıya qalxma buton funksiya

let mybutton = document.getElementById("up_icon");
let myicon = document.getElementById("up_i");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 120 || document.documentElement.scrollTop > 120 ||  document.documentElement.scrollTop) {
    mybutton.style.display = "block";
    
  } 
  else {
    mybutton.style.display = "none";
  }
}

scrollFunction()
mybutton.addEventListener('click',()=>{
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0;
})

    