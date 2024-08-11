// home latest
let latest = document.getElementById('latest')
let latest_ul = document.getElementById('latest_ul')
let change_latest=true

if (latest) {
    latest.addEventListener('click',()=>{
        change_latest==true?latest_ul.style='display:block':latest_ul.style='display:none'
        change_latest=!change_latest
    });
}
// messages deleted : 
document.addEventListener('DOMContentLoaded',()=>{
    let messages= document.querySelectorAll('.messages')
    setTimeout(() => {
        messages.forEach((message)=> message.remove())
    }, 2000);
})

// Pro filter navbar
let pro_filter=document.getElementById('products_filter')

if (pro_filter) {
    Array.from(pro_filter.children).forEach(child => {
        let header = child.querySelector('h3');
        let innerUl = child.querySelector('ul');
    
        if (header && innerUl) {
            header.addEventListener('click', (e) => {
                e.stopPropagation();
                if (innerUl.style.height && innerUl.style.height !== '0px') {
                    innerUl.style.height = '0px';
                } else {
                    innerUl.style.height = innerUl.scrollHeight + 'px';
                }
            });
    
           
            innerUl.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        }
    });
}

// Products home view
let big = document.getElementById('big-border');
let small = document.getElementById('small-border');

if(big){
    big.addEventListener('click',(event)=>{
        event.preventDefault(); 
        event.stopPropagation();
        let products= document.getElementsByClassName('products_small')
        Array.from(products).forEach(pro=>{
            pro.classList.remove('products_small')
            pro.classList.add('products_detail')
        })
        let product= document.getElementsByClassName('product_small')
        Array.from(product).forEach(pro=>{
            pro.classList.remove('product_small')
            pro.classList.add('product')
        })
        let pro_small_img= document.getElementsByClassName('pro_small_img')
        Array.from(pro_small_img).forEach(pro_small_img=>{
            pro_small_img.classList.remove('pro_small_img')
            pro_small_img.classList.add('pro_image')
        })
        let img_icons_small= document.getElementsByClassName('img_icons_small')
        Array.from(img_icons_small).forEach(pro=>{
            pro.classList.remove('img_icons_small')
            pro.classList.add('img_icons')
        })
        
        let pro_about_small= document.getElementsByClassName('pro_about_small')
        Array.from(pro_about_small).forEach(pro=>{
            pro.classList.remove('pro_about_small')
            pro.classList.add('pro_about')
        })
    })
}
if(small){
    small.addEventListener('click',(event)=>{
        event.preventDefault(); 
        event.stopPropagation();
        let products= document.getElementsByClassName('products_detail')
        Array.from(products).forEach(pro=>{
            pro.classList.remove('products_detail')
            pro.classList.add('products_small')
        })
        let product= document.getElementsByClassName('product')
        Array.from(product).forEach(pro=>{
            pro.classList.remove('product')
            pro.classList.add('product_small')
        })
        let pro_small_img= document.getElementsByClassName('pro_image')
        Array.from(pro_small_img).forEach(pro_small_img=>{
            pro_small_img.classList.remove('pro_image')
            pro_small_img.classList.add('pro_small_img')
        })
        let img_icons_small= document.getElementsByClassName('img_icons')
        Array.from(img_icons_small).forEach(pro=>{
            pro.classList.remove('img_icons')
            pro.classList.add('img_icons_small')
        })
        
        let pro_about_small= document.getElementsByClassName('pro_about')
        Array.from(pro_about_small).forEach(pro=>{
            pro.classList.remove('pro_about')
            pro.classList.add('pro_about_small')
        })
    })
}




// pro detail count  
 
     function pro_Plus(e,id){
            let pro_count = document.getElementById(`pro_count_${id}`);
            let pro_minus = document.getElementById(`pro_minus_${id}`)
            count=parseInt(pro_count.getAttribute('value'))
            count+=1
            pro_count.setAttribute('value',count)
            if ( count>1 ){
                pro_minus.removeAttribute('disabled')
            }
        }
        function pro_Minus(e,id){
            let pro_count = document.getElementById(`pro_count_${id}`);
            let pro_minus = document.getElementById(`pro_minus_${id}`)
            count=parseInt(pro_count.getAttribute('value'))
            count-=1
            
            if (  count==0) {
                count=1;
                
            }
            if ( count==1 ){
                pro_minus.setAttribute('disabled','')
            }
            pro_count.setAttribute('value',count)
        }

        






// stars rating

document.addEventListener("DOMContentLoaded", function() {
    const starsRadios = document.querySelectorAll('.rating_radio');

    starsRadios.forEach(function(radio) {
        radio.addEventListener('change', function() {
            const starsValue = parseInt(this.value);

            
            const allStars = document.querySelectorAll('.comment_stars i.fa-star');
            allStars.forEach(function(star) {
                star.style.color = '#d1d1d1';
                star.classList.remove('fa-solid');
                star.classList.add('fa-regular');
            });

            
            for (let i = 0; i < starsValue; i++) {
                allStars[i].style.color = '#FFD43B';
                allStars[i].classList.remove('fa-regular');
                allStars[i].classList.add('fa-solid');
            }
        });
    });
});

// Image full screen eye-icon products
function toggleFullscreen(e,imageId) {
    e.preventDefault(); 
    e.stopPropagation();
    var img = document.getElementById(imageId);
    if (!document.fullscreenElement) {
        img.requestFullscreen().catch(err => {
            console.log(`Error attempting to enable full-screen mode: ${err.message}`);
        });
    } else {
        document.exitFullscreen();
    }
};




// Price Range products
const rangeInput = document.querySelectorAll(".range-input input"),
  priceInput = document.querySelectorAll(".price-input input"),
  range = document.querySelector(".slider .progress");
let priceGap = 100;

priceInput.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minPrice = parseInt(priceInput[0].value),
      maxPrice = parseInt(priceInput[1].value);

    if (maxPrice - minPrice >= priceGap && maxPrice <= rangeInput[1].max) {
      if (e.target.className === "input-min") {
        rangeInput[0].value = minPrice;
        range.style.left = (minPrice / rangeInput[0].max) * 100 + "%";
      } else {
        rangeInput[1].value = maxPrice;
        range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
      }
    }
  });
});

rangeInput.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minVal = parseInt(rangeInput[0].value),
      maxVal = parseInt(rangeInput[1].value);

    if (maxVal - minVal < priceGap) {
      if (e.target.className === "range-min") {
        rangeInput[0].value = maxVal - priceGap;
      } else {
        rangeInput[1].value = minVal + priceGap;
      }
    } else {
      priceInput[0].value = minVal;
      priceInput[1].value = maxVal;
      range.style.left = (minVal / rangeInput[0].max) * 100 + "%";
      range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
    }
  });
});

// pro_detail star-rating
document.addEventListener('DOMContentLoaded',()=>{
    const pro_rating = document.querySelector('#pro_rate')
    const average = parseInt(document.querySelector('#average_rating').value)
    const stars = pro_rating.querySelectorAll('.fa-star');

    stars.forEach((star,index)=>{
        if(index < average){
            star.classList.remove('fa-regular')
            star.classList.add('fa-solid')
            star.style.color = '#FFD43B'
        }
    })
})

document.addEventListener('DOMContentLoaded', () => {
    const comments = document.querySelectorAll('.pro_comment');

    comments.forEach(comment => {
        const rating = parseInt(comment.querySelector('.comment_rating').value);
        const stars = comment.querySelectorAll('.comments_rating .fa-star');

        stars.forEach((star, index) => {
            if (index < rating) {
                star.classList.remove('fa-regular');
                star.classList.add('fa-solid');
                star.style.color = '#FFD43B';
            }});  });
});


//  product-card view
let shop_btn = document.getElementById('shop_btn')
let card_body = document.getElementById('card_body')
let container = document.getElementById('container')
let card_info = document.getElementById('card_info')

function card_view(event){
    event.preventDefault(); 
    event.stopPropagation();
    card_body.style.height = document.body.offsetHeight + 'px'
    card_info.style.overflow = 'auto'
    card_info.style.display = 'flex'
    
    setTimeout(function() {
        card_body.style.opacity = '1'
        card_info.style.right = '0px'
        card_body.style.overflow = 'auto'
    }, 10);
}
card_body.addEventListener('click',(event)=>{
    event.preventDefault(); 
    event.stopPropagation();
    
    
    card_body.style.opacity = '0'
    card_info.style.right = '-300px'
    setTimeout(function() {
        card_info.style.display = 'none'
        card_body.style.height = '0%';
        card_body.style.overflow = 'hidden'
    }, 400);
})
card_info.addEventListener('click',(e)=>{
    e.stopPropagation()
})


// product details - desctip , addit , review
let pro_desc = document.getElementById('pro_desc');
let pro_additional = document.getElementById('pro_additional')
let comments = document.getElementById('comment_div')


let det_des = document.getElementById('det_des')
if(det_des){  
det_des.addEventListener('click',()=>{
    pro_desc.style.display='block'
    det_des.classList.add('active')
    det_add.classList.remove('active')
    det_rev.classList.remove('active')
    pro_additional.style.display='none'
    comments.style.display='none'
})
}
let det_add = document.getElementById('det_add')
if(det_add){
    
    det_add.addEventListener('click',()=>{
        pro_additional.style.display='flex'
        det_add.classList.add('active')
        det_des.classList.remove('active')
        det_rev.classList.remove('active')
        pro_desc.style.display='none'
        comments.style.display='none'
    
})
}


let det_rev = document.getElementById('det_rev')
if(det_rev){
    
    det_rev.addEventListener('click',()=>{
        comments.style.display='block'
        det_rev.classList.add('active')
        det_add.classList.remove('active')
        det_des.classList.remove('active')
        pro_additional.style.display='none'
        pro_desc.style.display='none'
    })
    
}


function changeMainImage(imageUrl) {
    document.getElementById('detail_img').src = imageUrl;
}

// product images
let imgs_choices = document.getElementById('imgs_choices')
let choices_right = document.getElementById('choices_right')
let choices_left = document.getElementById('choices_left')

if(imgs_choices){
imgs_choices.addEventListener("wheel",(e)=>{
    e.preventDefault()
    imgs_choices.scrollLeft += e.deltaY;
})
choices_left.addEventListener("click",()=>{
    imgs_choices.scrollLeft -= 130;
})
choices_right.addEventListener("click",()=>{
    imgs_choices.scrollLeft += 130;
})
}


// related product  slider 

document.addEventListener('DOMContentLoaded',()=>{
    let rel_detail = document.getElementById('rel_detail')
    setInterval(() => {
        if (rel_detail.scrollLeft >= rel_detail.scrollWidth-rel_detail.clientWidth-40) {
            rel_detail.scrollLeft = 0;
        } else {
            rel_detail.scrollLeft += 330;
        }
          
    }, 5000);

})

// Product sorted latest
function sortedByprice(){
    const products= document.getElementById('products_detail')
    const products_val=Array.from(products.children)
    products_val.sort((a,b)=>{
       return  parseFloat(a.getAttribute('data-price'))-parseFloat(b.getAttribute('data-price'))
    }) 
    products_val.forEach((product)=>{
        products.append(product)
    })
}
function sortedByCost(){
    const products= document.getElementById('products_detail')
    const products_val=Array.from(products.children)
    products_val.sort((a,b)=>{
       return  parseFloat(b.getAttribute('data-price'))-parseFloat(a.getAttribute('data-price'))
    })
    products_val.forEach((product)=>{
        products.append(product)
    })
}
function sortedByBest(){
    const products= document.getElementById('products_detail')
    const products_val=Array.from(products.children)
    products_val.sort((a,b)=>{
       return  parseFloat(b.getAttribute('data-rating'))-parseFloat(a.getAttribute('data-rating'))
    })
    products_val.forEach((product)=>{
        products.append(product)
    })
}
function sortedByCom(){
    const products= document.getElementById('products_detail')
    const products_val=Array.from(products.children)
    products_val.sort((a,b)=>{
       return  parseFloat(b.getAttribute('data-com'))-parseFloat(a.getAttribute('data-com'))
    })
    products_val.forEach((product)=>{
        products.append(product)
    })
}

// Filter Form 
function FilterChange(e) {
    let filter_form = document.getElementById('products_filter');
    const brands_filt = Array.from(filter_form.querySelectorAll('input[name="brand"]:checked')).map(input => input.value);
    const category_filt = Array.from(filter_form.querySelectorAll('input[name="category"]:checked')).map(input => input.value);
    const color_filt = Array.from(filter_form.querySelectorAll('input[name="color"]:checked')).map(input => input.value);
    const price_max = parseFloat(Array.from(filter_form.querySelectorAll('input[name="range-max"]')).map(input => input.value)[0]);
    const price_min = parseFloat(Array.from(filter_form.querySelectorAll('input[name="range-min"]')).map(input => input.value)[0]);
    const products = document.getElementById('products_detail');
    const products_val = Array.from(products.children);
    const products_length =document.getElementById('products_length')
    let visibleCount = 0;

    if (brands_filt.length > 0 || category_filt.length > 0 || color_filt.length > 0 || !isNaN(price_max) || !isNaN(price_min)) {
        products_val.forEach((a) => {
            const product_brand = a.getAttribute('data-brand');
            const product_category = a.getAttribute('data-category');
            const product_color = a.getAttribute('data-color');
            const product_price = parseFloat(a.getAttribute('data-price'));

            const brandMatch = brands_filt.length === 0 || brands_filt.some(b => product_brand === b);
            const categoryMatch = category_filt.length === 0 || category_filt.some(c => product_category === c);
            const colorMatch = color_filt.length === 0 || color_filt.some(c => product_color === c);
            const priceMatch = (isNaN(price_min) || product_price >= price_min) && (isNaN(price_max) || product_price <= price_max);

            if (brandMatch && categoryMatch && colorMatch && priceMatch) {
                a.style.display = '';
                visibleCount++;
                products_length.textContent=visibleCount
            } else {
                a.style.display = 'none';
                products_length.textContent=visibleCount
            }
        });
    } else {
        products_val.forEach((a) => {
            a.style.display = '';
            visibleCount++;
            products_length.textContent=visibleCount
        });
    }

    const noItemsMessage = document.getElementById('no-items-message');
    if (visibleCount === 0) {
        if (!noItemsMessage) {
            const message = document.createElement('p');
            message.id = 'no-items-message';
            message.style.color = 'grey';
            message.style.textAlign = 'center';
            message.style.width = '100%';
            message.style.height = '100%';
            message.style.marginTop = '50px';
            message.textContent = 'The item you are looking for is not available';
            products.appendChild(message);
        }
    } else {
        if (noItemsMessage) {
            noItemsMessage.remove();
        }
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    const filter_form = document.getElementById('products_filter');

    const rangeInputs = filter_form.querySelectorAll('input[type="range"]');
    rangeInputs.forEach(input => {
        input.addEventListener('change', FilterChange);
    });

    const checkboxes = filter_form.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', FilterChange);
    });
});

// card functions - count - subtotal
document.addEventListener('DOMContentLoaded',()=>{
    let card_products= document.getElementById('card_products')
    let card_count_inp = document.getElementById('card_count_inp')
    let card_subtotal = document.getElementById('card_subtotal')
    let shopcount = document.getElementById('shopcount') 
    let totalSub=0
    count = Array.from(card_products.children).length
    shopcount.textContent=count
    Array.from(card_products.children).forEach(pro => {
        totalSub+=Number(pro.getAttribute('data-price'))
    });
    card_subtotal.textContent=totalSub
    card_count_inp.setAttribute('value',count)
})
