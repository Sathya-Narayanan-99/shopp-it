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


    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/;samesite=Lax;";

    var data = 0;

    for(item in cart){
        data += cart[item].quantity
    }

    var path = window. location. pathname;
    if (path == '/'){
        updateCartCount(data);
    }else{
        location.reload()
    }

}

function updateCartCount(data){
    document.getElementById('cart-total').innerHTML = data;
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
        var path = window. location. pathname;
        if (path == '/'){
            updateCartCount(data);
        }else{
            location.reload()
        }
    })
}