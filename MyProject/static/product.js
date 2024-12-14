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
document.addEventListener('DOMContentLoaded', () => {
    const pro_filter = document.getElementById('products_filter');
    
    if (pro_filter) {

        Array.from(pro_filter.children).forEach(child => {
            let header = child.querySelector('h3');
            let innerUl = child.querySelector('ul');
            if (header && innerUl) {

                const filterId = header.textContent.trim();
                const isOpen = localStorage.getItem(filterId) === 'true';
                innerUl.style.height = isOpen ? innerUl.scrollHeight + 'px' : '0px';
                
                header.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (innerUl.style.height && innerUl.style.height !== '0px') {
                        innerUl.style.height = '0px';
                        localStorage.setItem(filterId, 'false'); // Locala atiriq render olduqda baglanmasin
                    } else {
                        innerUl.style.height = innerUl.scrollHeight + 'px';
                        localStorage.setItem(filterId, 'true');
                    }
                });
                
                innerUl.addEventListener('click', (e) => {
                    e.stopPropagation();
                });
            }
        });
    }
});


// Products home view
let big = document.getElementById('big-border');
let small = document.getElementById('small-border');

function applyBigBorderView(){
        
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
    }


function applySmallBorderView(){

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
    }


document.addEventListener('DOMContentLoaded', () => {
    const viewPreference = localStorage.getItem('viewPreference');
    if (viewPreference === 'big') {
        applyBigBorderView();
    } else if (viewPreference === 'small') {
        applySmallBorderView();
    }
});

if(big){
    big.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation();
        applyBigBorderView();
        localStorage.setItem('viewPreference', 'big');
    });
}

if(small){
    small.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation();
        applySmallBorderView();
        localStorage.setItem('viewPreference', 'small'); 
    });
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

            
            const allStars = document.querySelectorAll('.comment_rating .comment_stars i.fa-star');
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
document.addEventListener("DOMContentLoaded", () => {
    const rangeInput = document.querySelectorAll(".range-input input"),
      priceInput = document.querySelectorAll(".price-input input"),
      range = document.querySelector(".slider .progress");
    let priceGap = 100;
  
    

  
    if (range) {
        let minVal = parseInt(rangeInput[0].value);
        let maxVal = parseInt(rangeInput[1].value);
      
        priceInput[0].value = minVal;
        priceInput[1].value = maxVal;
        range.style.left = (minVal / rangeInput[0].max) * 100 + "%";
        range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
           
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
    }
  });
  

// pro_detail star-rating
document.addEventListener('DOMContentLoaded',()=>{
    const pro_rating = document.querySelector('#pro_rate')
    if (pro_rating) {
        const average = parseInt(document.querySelector('#average_rating').value)
        const stars = pro_rating.querySelectorAll('.fa-star');
    
        stars.forEach((star,index)=>{
            if(index < average){
                star.classList.remove('fa-regular')
                star.classList.add('fa-solid')
                star.style.color = '#FFD43B'
            }
        })
    }
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

function card_view(){
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
document.addEventListener('DOMContentLoaded', () => {
    const pro_desc = document.getElementById('pro_desc');
    const pro_additional = document.getElementById('pro_additional');
    const comments = document.getElementById('comment_div');

    const det_des = document.getElementById('det_des');
    const det_add = document.getElementById('det_add');
    const det_rev = document.getElementById('det_rev');

    function updateDisplay(activeId) {

        if (pro_desc) {
            pro_desc.style.display = 'none';
            pro_additional.style.display = 'none';
            comments.style.display = 'none';
        }

        switch (activeId) {
            case 'det_des':
                pro_desc.style.display = 'block';
                break;
            case 'det_add':
                pro_additional.style.display = 'flex';
                break;
            case 'det_rev':
                comments.style.display = 'block';
                break;
        }

        det_des.classList.toggle('active', activeId === 'det_des');
        det_add.classList.toggle('active', activeId === 'det_add');
        det_rev.classList.toggle('active', activeId === 'det_rev');
    }

    function setActiveSectionFromStorage() {
        const activeSection = localStorage.getItem('activeSection');
        updateDisplay(activeSection || 'det_des'); 
    }

    function saveActiveSectionToStorage(activeId) {
        localStorage.setItem('activeSection', activeId);
    }

    if (det_des) {
        det_des.addEventListener('click', () => {
            updateDisplay('det_des');
            saveActiveSectionToStorage('det_des');
        });
    }

    if (det_add) {
        det_add.addEventListener('click', () => {
            updateDisplay('det_add');
            saveActiveSectionToStorage('det_add');
        });
    }

    if (det_rev) {
        det_rev.addEventListener('click', () => {
            updateDisplay('det_rev');
            saveActiveSectionToStorage('det_rev');
        });
    }
    
    pro_desc?setActiveSectionFromStorage():null
});



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

let rel_detail = document.getElementById('rel_detail')
document.addEventListener('DOMContentLoaded',()=>{
    if (rel_detail) {
        sliderStart()
    }
})
    
let rel_slider;

function sliderStart(){
    let computedStyle = window.getComputedStyle(rel_detail);
    let gap = computedStyle.gap;
    let width = computedStyle.width;
        rel_slider =  setInterval(() => {
            if (rel_detail.scrollLeft >= rel_detail.scrollWidth-rel_detail.clientWidth-40) {
                rel_detail.scrollLeft = 0;
            } else {
                rel_detail.scrollLeft += (( parseInt(width) / 4) );
            }     
        }, 5000);
}

function sliderStop(){
        clearInterval(rel_slider)
}





function FilterChange(e){
    document.getElementById('filter_form').submit()
}

let display=true
function searchClick(e){
    display?e.target.previousElementSibling.style='display:inline':e.target.previousElementSibling.style='display:none'
    display?e.target.setAttribute('src','https://staging.svgrepo.com/show/365893/x-thin.svg'):e.target.setAttribute('src','/media/navbar-footer_img/search_icon.svg')
    display = !display
    
}

function search_reset(){
    document.getElementById('search').value=''
    
}


// Products slider button
let slider_interval;

function pro_img_slider(e){

    let closestElement = e.target.closest('.pro_image') ||
                         e.target.closest('.rel_image') ||
                         e.target.closest('.trending_img') ||
                         e.target.closest('.pro_small_img');
    let pro_img = closestElement ? closestElement.querySelector('.pro_img_slider') : null;
    if (pro_img) {
        let img= pro_img.querySelector('img')
        let width = parseInt(window.getComputedStyle(img).width);
        
        
        clearInterval(slider_interval)
        slider_interval = setInterval(() => {
                if (pro_img.scrollLeft >= pro_img.scrollWidth-pro_img.clientWidth) {
                    pro_img.scrollLeft = 0;
                    
                } else {
                    pro_img.scrollLeft += width + 2;
                    console.log(pro_img.scrollLeft)
                }
        }, 1000);
    }
}

function pro_img_slider_stop(e) {
    console.log('stop slider')
    let closestElement = e.target.closest('.pro_image') ||
                         e.target.closest('.rel_image') ||
                         e.target.closest('.trending_img')||
                         e.target.closest('.pro_small_img');
    let pro_img = closestElement ? closestElement.querySelector('.pro_img_slider') : null;
    if (pro_img) {
        pro_img.scrollLeft = 0;
    }
    console.log(pro_img.scrollLeft)
    clearInterval(slider_interval);


    }
    

function place_reset(){
    document.getElementById('search_place').value=''
    
}


// Dark Mode on Site
// function dark_mode(){
//     const elements = document.querySelectorAll('*');


// elements.forEach((element) => {
//     const style = window.getComputedStyle(element);
//     const backgroundColor = style.backgroundColor;

//     if (backgroundColor === '#088395') {  
//         element.style.backgroundColor = 'white';
//     } 
//     else if (backgroundColor === 'rgb(255, 255, 255)') { 
//         element.style.backgroundColor = '#088395';
//     }
// });
// }
