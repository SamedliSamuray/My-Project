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
