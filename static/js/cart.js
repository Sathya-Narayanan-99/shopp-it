var updateCartBtn = document.getElementsByClassName('update-cart');

for(var i=0; i < updateCartBtn.length; i++){
    updateCartBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;

        if (user === 'AnonymousUser') {
            console.log('User not logged in');
        }else{
            updateUserItem(productId, action)
        }
    })
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