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

// Pro home view
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


// Api
// let products = document.getElementById('products_detail')
// if (products) {
//     fetch('http://127.0.0.1:8000/product-api/api-list/')
// .then((res) => res.json())
// .then((data) => data.map((product) => createProduct(product)));
// function createProduct(product) {
//     let product_list =  `<div class="product">
//             <a href="/products-details/${product.id}">
//                 <div class="pro_image">
//                     <img src="${product.image}" alt="">
//                     <div class="img_icons">
//                         <i class="fa-regular fa-star"></i>
//                         <i class="fa-solid fa-right-left"></i>
//                         <i id='icon_see' class="fa-regular fa-eye"></i>
//                     </div>
//             </a>
//             </div>
//             <div class="pro_about">
//                 <div class="pro_brand">${product.brand}</div>
//                 <div class="pro_name">${product.name}</div>
//                 <div class="pro_price">$${product.price}</div>
//                 <div class="pro_price">$${product.id}</div>
//             </div>
//         </div> `
//     products.innerHTML += product_list;


// }
// }


// pro detail count 
let pro_count = document.getElementById('pro_count');
let a=1;

let pro_plus = document.getElementById('pro_plus');
let pro_minus = document.getElementById('pro_minus');

if(pro_plus){
    pro_plus.addEventListener('click',()=>{
        ++a;
        pro_count.textContent=a
        if ( a>1 ){
            pro_minus.parentElement.removeAttribute('disabled')
        }
    })
}

if(pro_minus){
    pro_minus.addEventListener('click',()=>{
        --a;
        if ( a==0) {
            a=1;
            
        }
        if ( a==1 ){
            pro_minus.parentElement.setAttribute('disabled','')
        }
        pro_count.textContent=a
    })
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

// Full screen
function toggleFullscreen(imageId) {
    
    var img = document.getElementById(imageId);
    if (!document.fullscreenElement) {
        img.requestFullscreen().catch(err => {
            console.log(`Error attempting to enable full-screen mode: ${err.message}`);
        });
    } else {
        document.exitFullscreen();
    }
};



// Price Range
const rangeInput = document.querySelectorAll(".range-input input"),
  priceInput = document.querySelectorAll(".price-input input"),
  range = document.querySelector(".slider .progress");
let priceGap = 1000;

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

// pro_detail star
function proStars(rating){
    let pro_rate = document.getElementById('pro_rate')
    let rate_icon =[]
    rate_icon = Array.from(pro_rate.children)
    for (let i = 0; i <= parseInt(rating); i++) {
        rate_icon[i].classList.remove('fa-regular')
        rate_icon[i].classList.add('fa-solid')
        rate_icon[i].style.color = '#FFD43B';
    }
}
// html onclick  ->  onclick="proStars('{{average_rating}}')"  #Solid Star <i class="fa-solid fa-star" style="color: #FFD43B;"></i>

