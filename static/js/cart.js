var updateCartBtn = document.getElementsByClassName('update-cart');

for(var i=0; i < updateCartBtn.length; i++){
    updateCartBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;

        if (user === 'AnonymousUser') {
            addCookieItem(productId, action)
        }else{
            updateUserItem(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('Not logged in..!');

    if(action == 'add'){
        if (cart[productId] == undefined){
            cart[productId] = {'quantity':1};
        }else{
            cart[productId]['quantity'] += 1;
        }
    }

    if (action == 'remove'){
        cart[productId]['quantity'] -= 1;

        if(cart[productId]['quantity'] <= 0){
            delete cart[productId];
        }
    }

    if (action == 'delete'){
        delete cart[productId];
    }


    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/;";

}

function updateUserItem(productId, action){
    
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        location.reload()
    })
}