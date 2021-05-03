if (shipping == 'False'){
    document.getElementById('shipping-info').innerHTML= '';
}

if (user != 'AnonymousUser'){
    document.getElementById('user-info').innerHTML='';
}

if (shipping == 'False' && user != 'AnonymousUser'){
    document.getElementById('form-wrapper').classList.add('hidden');
    document.getElementById('paypal-info').classList.remove('hidden');
}

var form = document.getElementById('form');

form.addEventListener('submit', function(e){
    e.preventDefault();
    console.log('form submitted');

    document.getElementById('form-button').classList.add('hidden');
    document.getElementById('paypal-info').classList.remove('hidden');
})

function submitFormData(){
    
    var userFormData = {
        'name':null,
        'email':null,
        'total':total,
    }

    var shippingFormData = {
        'address1':null,
        'address2':null,
        'city':null,
        'state':null,
        'zipcode':null,
        'country':null,   
    }

    if(shipping != 'False' && shippingAddress != ''){
        shippingFormData.address1 = form.address1.value
        shippingFormData.address2 = form.address2.value
        shippingFormData.city = form.city.value
        shippingFormData.state = form.state.value
        shippingFormData.zipcode = form.zipcode.value
        shippingFormData.country = form.country.value
    }

    if(user == 'AnonymousUser'){
        shippingFormData.name = form.name.value
        shippingFormData.email = form.email.value
    }

    url = '/process_order/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'userForm':userFormData, 'shippingForm':shippingFormData})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        alert("Transaction Completed");
        window.location.href = storeUrl
    })
}

document.getElementById('make-payment').addEventListener('click', function(e){
    submitFormData();
})